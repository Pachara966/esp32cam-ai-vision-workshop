const $ = id => document.getElementById(id);

// ---------------------------------------------------------------------------
// Init
// ---------------------------------------------------------------------------

async function init() {
  await loadProviderInfo();
  await loadPresets();
}

async function loadProviderInfo() {
  try {
    const res = await fetch('/health');
    const data = await res.json();
    $('provider-display').value = data.vision_provider || 'unknown';
  } catch {
    $('provider-display').value = 'error — server not running?';
  }
}

async function loadPresets() {
  try {
    const res = await fetch('/prompts');
    const presets = await res.json();
    const sel = $('preset-select');
    presets.forEach(p => {
      const opt = document.createElement('option');
      opt.value = p.prompt;
      opt.textContent = `${p.name_th} / ${p.name_en}`;
      sel.appendChild(opt);
    });
    sel.addEventListener('change', () => {
      if (sel.value) $('prompt-text').value = sel.value;
    });
  } catch {
    console.warn('Could not load presets');
  }
}

// ---------------------------------------------------------------------------
// Capture from ESP32-CAM
// ---------------------------------------------------------------------------

async function captureAndAnalyze() {
  const camUrl = $('cam-url').value.trim();
  if (!camUrl) {
    setStatus('กรุณากรอก ESP32-CAM URL / Please enter the ESP32-CAM URL.', 'error');
    return;
  }

  const prompt = $('prompt-text').value.trim() ||
    'อธิบายสิ่งที่เห็นในภาพนี้ / Describe what you see in this image.';

  setStatus('<span class="spinner"></span>กำลังดึงภาพจากกล้องและวิเคราะห์… Fetching & analyzing…', '');
  setButtons(true);

  try {
    const res = await fetch('/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ cam_url: camUrl, prompt }),
    });
    const data = await res.json();

    if (!res.ok) {
      setStatus(`❌ Error: ${data.detail || res.statusText}`, 'error');
      return;
    }

    // Show live image from ESP32 capture URL
    const imgEl = $('captured-img');
    imgEl.src = camUrl.replace(/\/$/, '') + '/capture?t=' + Date.now();
    imgEl.style.display = 'block';
    $('img-info').textContent = `${(data.image_size_bytes / 1024).toFixed(1)} KB from ${camUrl}`;

    showResult(data);
    setStatus('✅ วิเคราะห์เสร็จสิ้น / Analysis complete.', 'ok');
  } catch (err) {
    setStatus(`❌ Network error: ${err.message}`, 'error');
  } finally {
    setButtons(false);
  }
}

// ---------------------------------------------------------------------------
// Upload
// ---------------------------------------------------------------------------

async function uploadAndAnalyze(input) {
  const file = input.files[0];
  if (!file) return;

  const prompt = $('prompt-text').value.trim() ||
    'อธิบายสิ่งที่เห็นในภาพนี้ / Describe what you see in this image.';

  // Preview the uploaded image immediately
  const imgEl = $('captured-img');
  imgEl.src = URL.createObjectURL(file);
  imgEl.style.display = 'block';
  $('img-info').textContent = `${(file.size / 1024).toFixed(1)} KB — ${file.name}`;

  setStatus('<span class="spinner"></span>กำลังวิเคราะห์… Analyzing…', '');
  setButtons(true);

  const form = new FormData();
  form.append('file', file);
  form.append('prompt', prompt);

  try {
    const res = await fetch('/analyze-upload', { method: 'POST', body: form });
    const data = await res.json();

    if (!res.ok) {
      setStatus(`❌ Error: ${data.detail || res.statusText}`, 'error');
      return;
    }
    showResult(data);
    setStatus('✅ วิเคราะห์เสร็จสิ้น / Analysis complete.', 'ok');
  } catch (err) {
    setStatus(`❌ Network error: ${err.message}`, 'error');
  } finally {
    setButtons(false);
    input.value = '';
  }
}

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

function showResult(data) {
  $('provider-badge').textContent = `Provider: ${data.provider}`;
  $('result-box').textContent = data.result;
}

function setStatus(html, cls) {
  const el = $('status');
  el.innerHTML = html;
  el.className = cls;
}

function setButtons(disabled) {
  $('btn-capture').disabled = disabled;
  $('btn-upload').disabled  = disabled;
}

// ---------------------------------------------------------------------------
// Boot
// ---------------------------------------------------------------------------

init();
