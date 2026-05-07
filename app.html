<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Chatbot: El Mundo del Anime</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Zen+Kaku+Gothic+New:wght@400;700;900&display=swap" rel="stylesheet">
<style>
  :root {
    --sakura: #FF6B9D;
    --sakura-light: #FFD6E8;
    --sakura-dark: #C93777;
    --ink: #1A1028;
    --ink-mid: #2E2040;
    --ink-soft: #3D2E55;
    --panel: #211534;
    --panel-light: #2D1F47;
    --accent: #7C4DFF;
    --accent-glow: rgba(124, 77, 255, 0.3);
    --gold: #FFD700;
    --cyan: #00E5FF;
    --text-primary: #F0E6FF;
    --text-secondary: #B09CC8;
    --text-muted: #7A6A95;
    --border: rgba(255,107,157,0.2);
    --border-hover: rgba(255,107,157,0.5);
    --score-color: #FF6B9D;
    --fragment-bg: rgba(255,107,157,0.05);
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: 'Noto Sans JP', sans-serif;
    background: var(--ink);
    color: var(--text-primary);
    display: flex;
    height: 100vh;
    overflow: hidden;
  }

  /* ── SIDEBAR ── */
  #sidebar {
    width: 260px;
    min-width: 260px;
    background: var(--panel);
    border-right: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    overflow-y: auto;
    padding: 20px 16px;
    gap: 20px;
    position: relative;
  }

  #sidebar::before {
    content: '';
    position: absolute;
    top: 0; right: 0;
    width: 1px;
    height: 100%;
    background: linear-gradient(to bottom, transparent, var(--sakura), transparent);
    opacity: 0.4;
  }

  .toggle-sidebar {
    position: absolute;
    top: 12px; right: 12px;
    background: none;
    border: none;
    color: var(--text-muted);
    font-size: 18px;
    cursor: pointer;
    transition: color 0.2s;
  }
  .toggle-sidebar:hover { color: var(--sakura); }

  .sidebar-section { display: flex; flex-direction: column; gap: 10px; }

  .sidebar-title {
    font-family: 'Zen Kaku Gothic New', sans-serif;
    font-weight: 700;
    font-size: 13px;
    color: var(--text-primary);
    letter-spacing: 0.05em;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .sidebar-title .icon-wrapper {
    width: 28px; height: 28px;
    background: linear-gradient(135deg, var(--sakura-dark), var(--accent));
    border-radius: 6px;
    display: flex; align-items: center; justify-content: center;
    font-size: 14px;
  }

  .sidebar-desc {
    font-size: 12px;
    color: var(--text-secondary);
    line-height: 1.6;
  }

  .sidebar-desc strong { color: var(--sakura-light); font-weight: 500; }

  .topic-list { list-style: none; display: flex; flex-direction: column; gap: 6px; }

  .topic-list li {
    font-size: 12px;
    color: var(--text-secondary);
    padding: 6px 10px;
    border-radius: 6px;
    border: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 8px;
    background: rgba(255,107,157,0.04);
    cursor: default;
    transition: border-color 0.2s, background 0.2s;
  }

  .topic-list li:hover {
    border-color: var(--border-hover);
    background: rgba(255,107,157,0.08);
  }

  .topic-list li::before {
    content: '✦';
    color: var(--sakura);
    font-size: 10px;
    flex-shrink: 0;
  }

  .tip-box {
    background: rgba(124,77,255,0.1);
    border: 1px solid rgba(124,77,255,0.3);
    border-radius: 8px;
    padding: 10px 12px;
    font-size: 12px;
    color: var(--text-secondary);
    line-height: 1.5;
  }

  .question-list { list-style: none; display: flex; flex-direction: column; gap: 6px; counter-reset: q; }

  .question-list li {
    counter-increment: q;
    font-size: 12px;
    color: var(--text-secondary);
    padding: 7px 10px 7px 28px;
    border-radius: 6px;
    border: 1px solid var(--border);
    cursor: pointer;
    transition: all 0.2s;
    position: relative;
    line-height: 1.4;
  }

  .question-list li::before {
    content: counter(q);
    position: absolute;
    left: 8px;
    color: var(--sakura);
    font-weight: 700;
    font-size: 11px;
  }

  .question-list li:hover {
    border-color: var(--sakura);
    color: var(--text-primary);
    background: rgba(255,107,157,0.08);
    transform: translateX(2px);
  }

  /* ── MAIN AREA ── */
  #main {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    position: relative;
  }

  /* Decorative BG pattern */
  #main::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image:
      radial-gradient(circle at 80% 10%, rgba(124,77,255,0.06) 0%, transparent 50%),
      radial-gradient(circle at 20% 80%, rgba(255,107,157,0.06) 0%, transparent 50%);
    pointer-events: none;
  }

  /* ── HEADER ── */
  #header {
    padding: 24px 32px 20px;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 16px;
    background: rgba(33,21,52,0.6);
    backdrop-filter: blur(8px);
    flex-shrink: 0;
  }

  .header-icon {
    width: 48px; height: 48px;
    background: linear-gradient(135deg, var(--sakura-dark) 0%, var(--accent) 100%);
    border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    font-size: 24px;
    box-shadow: 0 0 20px rgba(255,107,157,0.3);
    flex-shrink: 0;
  }

  #header h1 {
    font-family: 'Zen Kaku Gothic New', sans-serif;
    font-weight: 900;
    font-size: 22px;
    color: var(--text-primary);
    letter-spacing: -0.02em;
  }

  #header .subtitle {
    font-size: 12px;
    color: var(--text-muted);
    margin-top: 2px;
  }

  .header-badges {
    margin-left: auto;
    display: flex;
    gap: 8px;
  }

  .badge {
    font-size: 11px;
    padding: 4px 10px;
    border-radius: 20px;
    border: 1px solid;
    font-weight: 500;
    letter-spacing: 0.03em;
  }

  .badge-pink {
    color: var(--sakura);
    border-color: rgba(255,107,157,0.4);
    background: rgba(255,107,157,0.08);
  }

  .badge-purple {
    color: #B39DFF;
    border-color: rgba(124,77,255,0.4);
    background: rgba(124,77,255,0.08);
  }

  /* ── MESSAGES ── */
  #messages {
    flex: 1;
    overflow-y: auto;
    padding: 24px 32px;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  #messages::-webkit-scrollbar { width: 4px; }
  #messages::-webkit-scrollbar-track { background: transparent; }
  #messages::-webkit-scrollbar-thumb { background: rgba(255,107,157,0.3); border-radius: 2px; }

  .msg {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    animation: fadeUp 0.3s ease;
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(8px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .msg-avatar {
    width: 34px; height: 34px;
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 16px;
    flex-shrink: 0;
    margin-top: 2px;
  }

  .msg-avatar.user-av {
    background: linear-gradient(135deg, #3D2E55, #5C4080);
    border: 1px solid rgba(255,107,157,0.3);
    font-size: 13px;
    font-weight: 700;
    color: var(--sakura-light);
  }

  .msg-avatar.bot-av {
    background: linear-gradient(135deg, var(--sakura-dark), var(--accent));
    box-shadow: 0 0 12px rgba(255,107,157,0.35);
  }

  .msg-content {
    flex: 1;
    background: var(--panel-light);
    border: 1px solid var(--border);
    border-radius: 4px 14px 14px 14px;
    padding: 12px 16px;
    font-size: 14px;
    color: var(--text-primary);
    line-height: 1.7;
    max-width: 760px;
  }

  .msg-content.user-msg {
    background: rgba(124,77,255,0.12);
    border-color: rgba(124,77,255,0.25);
    border-radius: 14px 4px 14px 14px;
    margin-left: auto;
  }

  .msg.user { flex-direction: row-reverse; }
  .msg.user .msg-content { margin-left: auto; margin-right: 0; }

  /* ── FRAGMENTS ── */
  .fragments-toggle {
    display: flex;
    align-items: center;
    gap: 8px;
    cursor: pointer;
    font-size: 13px;
    font-weight: 500;
    color: var(--cyan);
    margin-top: 10px;
    padding: 6px 0;
    border-top: 1px solid var(--border);
    user-select: none;
    transition: opacity 0.2s;
  }

  .fragments-toggle:hover { opacity: 0.8; }

  .fragments-toggle .chevron {
    font-size: 10px;
    transition: transform 0.2s;
  }

  .fragments-toggle.open .chevron { transform: rotate(90deg); }

  .fragments-body { display: none; margin-top: 10px; }
  .fragments-body.open { display: flex; flex-direction: column; gap: 10px; }

  .fragment-card {
    background: var(--fragment-bg);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 12px 14px;
  }

  .fragment-header {
    font-size: 12px;
    font-weight: 700;
    color: var(--text-secondary);
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .score {
    color: var(--score-color);
    font-family: 'Noto Sans JP', monospace;
    font-size: 12px;
  }

  .fragment-text {
    font-size: 12px;
    color: var(--text-secondary);
    line-height: 1.65;
  }

  .fragment-divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 8px 0 0;
  }

  /* ── TYPING INDICATOR ── */
  .typing-dots {
    display: flex;
    gap: 4px;
    align-items: center;
    padding: 4px 0;
  }

  .typing-dots span {
    width: 6px; height: 6px;
    background: var(--sakura);
    border-radius: 50%;
    animation: bounce 1.2s infinite;
  }

  .typing-dots span:nth-child(2) { animation-delay: 0.2s; }
  .typing-dots span:nth-child(3) { animation-delay: 0.4s; }

  @keyframes bounce {
    0%, 80%, 100% { transform: translateY(0); opacity: 0.5; }
    40% { transform: translateY(-5px); opacity: 1; }
  }

  /* ── INPUT AREA ── */
  #input-area {
    padding: 16px 32px 20px;
    border-top: 1px solid var(--border);
    background: rgba(33,21,52,0.7);
    backdrop-filter: blur(8px);
    flex-shrink: 0;
  }

  .input-wrapper {
    display: flex;
    align-items: center;
    gap: 10px;
    background: var(--panel-light);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 6px 6px 6px 16px;
    transition: border-color 0.2s, box-shadow 0.2s;
  }

  .input-wrapper:focus-within {
    border-color: rgba(255,107,157,0.5);
    box-shadow: 0 0 0 3px rgba(255,107,157,0.08);
  }

  #user-input {
    flex: 1;
    background: none;
    border: none;
    outline: none;
    color: var(--text-primary);
    font-family: 'Noto Sans JP', sans-serif;
    font-size: 14px;
    line-height: 1.5;
    resize: none;
    max-height: 120px;
    overflow-y: auto;
  }

  #user-input::placeholder { color: var(--text-muted); }

  #send-btn {
    width: 36px; height: 36px;
    background: linear-gradient(135deg, var(--sakura-dark), var(--accent));
    border: none;
    border-radius: 10px;
    cursor: pointer;
    display: flex; align-items: center; justify-content: center;
    transition: transform 0.15s, box-shadow 0.15s;
    flex-shrink: 0;
    color: white;
    font-size: 16px;
  }

  #send-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 0 14px rgba(255,107,157,0.4);
  }

  #send-btn:active { transform: scale(0.97); }

  /* ── DIVIDER ── */
  .section-divider {
    height: 1px;
    background: linear-gradient(to right, transparent, var(--border), transparent);
    margin: 4px 0;
  }

  /* ── SCROLLBAR SIDEBAR ── */
  #sidebar::-webkit-scrollbar { width: 3px; }
  #sidebar::-webkit-scrollbar-track { background: transparent; }
  #sidebar::-webkit-scrollbar-thumb { background: rgba(255,107,157,0.2); border-radius: 2px; }
</style>
</head>
<body>

<!-- SIDEBAR -->
<aside id="sidebar">
  <button class="toggle-sidebar" onclick="toggleSidebar()" title="Cerrar panel">《</button>

  <!-- About -->
  <div class="sidebar-section">
    <div class="sidebar-title">
      <span class="icon-wrapper">📺</span>
      Sobre este documento
    </div>
    <p class="sidebar-desc">
      Este chatbot está entrenado con el fragmento del libro
      <strong>'Descubrir el Anime - Historia &amp; Cultura'</strong> (páginas 12-48).
    </p>
  </div>

  <div class="section-divider"></div>

  <!-- Temas -->
  <div class="sidebar-section">
    <div class="sidebar-title" style="font-size:12px; color:var(--text-secondary);">Temas principales:</div>
    <ul class="topic-list">
      <li>Historia y orígenes del anime</li>
      <li>Géneros: Shonen, Shojo, Seinen, Isekai</li>
      <li>Estudios legendarios (Ghibli, MAPPA, Bones)</li>
      <li>El impacto cultural global del anime</li>
    </ul>
  </div>

  <div class="section-divider"></div>

  <!-- Preguntas de ejemplo -->
  <div class="sidebar-section">
    <div class="sidebar-title" style="font-size:12px; color: var(--text-secondary);">💡 Preguntas de ejemplo</div>
    <div class="tip-box">Copia y pega alguna de estas preguntas en el chat:</div>
    <ul class="question-list" id="example-questions">
      <li onclick="useQuestion(this)">¿Cuál es el origen del anime y cuándo surgió?</li>
      <li onclick="useQuestion(this)">¿Qué diferencia al shonen del shojo?</li>
      <li onclick="useQuestion(this)">¿Por qué Studio Ghibli es tan reconocido mundialmente?</li>
      <li onclick="useQuestion(this)">¿Qué es el isekai y cuáles son sus características?</li>
      <li onclick="useQuestion(this)">¿Cómo influenció el manga al estilo visual del anime?</li>
    </ul>
  </div>
</aside>

<!-- MAIN -->
<main id="main">

  <!-- Header -->
  <header id="header">
    <div class="header-icon">🎌</div>
    <div>
      <h1>Chatbot: Anime y su Universo Cultural</h1>
      <div class="subtitle">Basado en fragmentos del libro de Historia del Anime</div>
    </div>
    <div class="header-badges">
      <span class="badge badge-pink">Cultura Japonesa</span>
      <span class="badge badge-purple">RAG · PDF</span>
    </div>
  </header>

  <!-- Messages -->
  <div id="messages">
    <!-- Initial bot message -->
    <div class="msg bot">
      <div class="msg-avatar bot-av">🌸</div>
      <div class="msg-content">
        ¡Konnichiwa! Soy tu asistente experto en anime. Puedo responder preguntas sobre historia, géneros, estudios de animación, personajes icónicos y el impacto cultural del anime en el mundo. ¿Qué quieres saber? 🎌
      </div>
    </div>
  </div>

  <!-- Input -->
  <div id="input-area">
    <div class="input-wrapper">
      <textarea
        id="user-input"
        placeholder="Escribe tu pregunta sobre anime..."
        rows="1"
        onkeydown="handleKey(event)"
        oninput="autoResize(this)"
      ></textarea>
      <button id="send-btn" onclick="sendMessage()" title="Enviar">➤</button>
    </div>
  </div>

</main>

<script>
const API_URL = "https://api.anthropic.com/v1/messages";

const SYSTEM_PROMPT = `Eres un experto en anime y cultura japonesa de animación, entrenado en un fragmento de un libro especializado sobre historia y cultura del anime (páginas 12-48). Respondes preguntas sobre:
- Historia y orígenes del anime (desde los años 1960)
- Géneros: Shonen, Shojo, Seinen, Josei, Isekai, Mecha, Slice of Life, etc.
- Estudios de animación legendarios: Studio Ghibli, MAPPA, Ufotable, Bones, Madhouse, A-1 Pictures
- Directores icónicos: Hayao Miyazaki, Makoto Shinkai, Satoshi Kon, Mamoru Oshii
- El impacto cultural global del anime
- Diferencias entre anime y manga

IMPORTANTE: Cuando respondas, SIEMPRE incluye al final un bloque JSON con los fragmentos recuperados. Usa este formato exacto:

[FRAGMENTOS]
{"fragments": [{"id": 1, "score": 0.XXXX, "text": "fragmento relevante del contexto..."}, {"id": 2, "score": 0.XXXX, "text": "segundo fragmento relevante..."}]}
[/FRAGMENTOS]

Responde en español. Si la pregunta no está relacionada con anime, indica amablemente que solo puedes responder sobre ese tema.`;

let conversationHistory = [];
let isLoading = false;

async function sendMessage() {
  const input = document.getElementById('user-input');
  const text = input.value.trim();
  if (!text || isLoading) return;

  input.value = '';
  autoResize(input);
  appendMessage('user', text);

  conversationHistory.push({ role: 'user', content: text });

  isLoading = true;
  const typingId = appendTyping();

  try {
    const res = await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 1000,
        system: SYSTEM_PROMPT,
        messages: conversationHistory
      })
    });

    const data = await res.json();
    removeTyping(typingId);

    const fullText = data.content?.[0]?.text || 'Lo siento, no pude procesar tu pregunta.';

    // Parse fragments
    const fragmentMatch = fullText.match(/\[FRAGMENTOS\]([\s\S]*?)\[\/FRAGMENTOS\]/);
    let cleanText = fullText.replace(/\[FRAGMENTOS\][\s\S]*?\[\/FRAGMENTOS\]/g, '').trim();
    let fragments = [];

    if (fragmentMatch) {
      try {
        const parsed = JSON.parse(fragmentMatch[1].trim());
        fragments = parsed.fragments || [];
      } catch(e) {}
    }

    appendBotMessage(cleanText, fragments);
    conversationHistory.push({ role: 'assistant', content: fullText });

  } catch(err) {
    removeTyping(typingId);
    appendBotMessage('Error al conectar con la API. Intenta de nuevo.', []);
  }

  isLoading = false;
}

function appendMessage(role, text) {
  const msgs = document.getElementById('messages');
  const div = document.createElement('div');
  div.className = `msg ${role}`;

  const av = document.createElement('div');
  av.className = `msg-avatar ${role === 'user' ? 'user-av' : 'bot-av'}`;
  av.textContent = role === 'user' ? 'Tú' : '🌸';

  const content = document.createElement('div');
  content.className = `msg-content ${role === 'user' ? 'user-msg' : ''}`;
  content.textContent = text;

  div.appendChild(av);
  div.appendChild(content);
  msgs.appendChild(div);
  msgs.scrollTop = msgs.scrollHeight;
}

function appendBotMessage(text, fragments) {
  const msgs = document.getElementById('messages');
  const div = document.createElement('div');
  div.className = 'msg bot';

  const av = document.createElement('div');
  av.className = 'msg-avatar bot-av';
  av.textContent = '🌸';

  const content = document.createElement('div');
  content.className = 'msg-content';
  content.style.cssText = 'white-space: pre-wrap;';
  content.textContent = text;

  if (fragments.length > 0) {
    const toggleId = 'frag-' + Date.now();

    const toggle = document.createElement('div');
    toggle.className = 'fragments-toggle';
    toggle.id = toggleId + '-toggle';
    toggle.innerHTML = `<span class="chevron">▶</span> 🔍 Fragmentos recuperados del PDF`;
    toggle.onclick = () => {
      const body = document.getElementById(toggleId + '-body');
      const tog = document.getElementById(toggleId + '-toggle');
      body.classList.toggle('open');
      tog.classList.toggle('open');
    };

    const body = document.createElement('div');
    body.className = 'fragments-body open';
    body.id = toggleId + '-body';

    // Toggle starts open (matches reference design)
    toggle.classList.add('open');

    fragments.forEach((f, i) => {
      const card = document.createElement('div');
      card.className = 'fragment-card';
      card.innerHTML = `
        <div class="fragment-header">
          <span>Fragmento ${f.id || i+1}</span>
          <span>—</span>
          <span class="score">score: ${typeof f.score === 'number' ? f.score.toFixed(4) : f.score}</span>
        </div>
        <div class="fragment-text">${escapeHtml(f.text)}</div>
      `;
      if (i < fragments.length - 1) {
        const hr = document.createElement('hr');
        hr.className = 'fragment-divider';
        body.appendChild(card);
        body.appendChild(hr);
      } else {
        body.appendChild(card);
      }
    });

    content.appendChild(toggle);
    content.appendChild(body);
  }

  div.appendChild(av);
  div.appendChild(content);
  msgs.appendChild(div);
  msgs.scrollTop = msgs.scrollHeight;
}

function appendTyping() {
  const msgs = document.getElementById('messages');
  const id = 'typing-' + Date.now();
  const div = document.createElement('div');
  div.className = 'msg bot';
  div.id = id;
  div.innerHTML = `
    <div class="msg-avatar bot-av">🌸</div>
    <div class="msg-content">
      <div class="typing-dots">
        <span></span><span></span><span></span>
      </div>
    </div>`;
  msgs.appendChild(div);
  msgs.scrollTop = msgs.scrollHeight;
  return id;
}

function removeTyping(id) {
  const el = document.getElementById(id);
  if (el) el.remove();
}

function handleKey(e) {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
}

function autoResize(el) {
  el.style.height = 'auto';
  el.style.height = Math.min(el.scrollHeight, 120) + 'px';
}

function useQuestion(el) {
  const input = document.getElementById('user-input');
  input.value = el.textContent.trim();
  autoResize(input);
  input.focus();
}

function toggleSidebar() {
  const sb = document.getElementById('sidebar');
  sb.style.display = sb.style.display === 'none' ? 'flex' : 'none';
}

function escapeHtml(text) {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}
</script>
</body>
</html>
