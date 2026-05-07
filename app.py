"""
Chatbot: Anime y su Universo Cultural
Réplica en Python/Gradio del chatbot del libro de Filosofía pero con temática anime.
Requiere: pip install anthropic gradio
"""

import anthropic
import gradio as gr
import json
import re

# ── Configuración del cliente Anthropic ──────────────────────────────────────
client = anthropic.Anthropic()  # usa ANTHROPIC_API_KEY del entorno

SYSTEM_PROMPT = """Eres un experto en anime y cultura japonesa de animación, entrenado en un fragmento \
de un libro especializado sobre historia y cultura del anime (páginas 12-48). Respondes preguntas sobre:
- Historia y orígenes del anime (desde los años 1960)
- Géneros: Shonen, Shojo, Seinen, Josei, Isekai, Mecha, Slice of Life, etc.
- Estudios de animación legendarios: Studio Ghibli, MAPPA, Ufotable, Bones, Madhouse, A-1 Pictures
- Directores icónicos: Hayao Miyazaki, Makoto Shinkai, Satoshi Kon, Mamoru Oshii
- El impacto cultural global del anime
- Diferencias entre anime y manga

IMPORTANTE: Al responder, incluye siempre al final un bloque JSON con fragmentos simulados del PDF:

[FRAGMENTOS]
{"fragments": [
  {"id": 1, "score": 0.XXXX, "text": "fragmento relevante del contexto..."},
  {"id": 2, "score": 0.XXXX, "text": "segundo fragmento relevante..."}
]}
[/FRAGMENTOS]

Responde en español. Si la pregunta no es sobre anime, indícalo amablemente."""

# ── Preguntas de ejemplo ─────────────────────────────────────────────────────
EXAMPLE_QUESTIONS = [
    "¿Cuál es el origen del anime y cuándo surgió?",
    "¿Qué diferencia al shonen del shojo?",
    "¿Por qué Studio Ghibli es tan reconocido mundialmente?",
    "¿Qué es el isekai y cuáles son sus características?",
    "¿Cómo influenció el manga al estilo visual del anime?",
]

# ── Lógica de chat ────────────────────────────────────────────────────────────
def parse_fragments(raw: str) -> tuple[str, list[dict]]:
    """Separa el texto limpio de los fragmentos RAG embebidos."""
    match = re.search(r"\[FRAGMENTOS\](.*?)\[/FRAGMENTOS\]", raw, re.DOTALL)
    clean = re.sub(r"\[FRAGMENTOS\].*?\[/FRAGMENTOS\]", "", raw, flags=re.DOTALL).strip()
    fragments = []
    if match:
        try:
            fragments = json.loads(match.group(1).strip()).get("fragments", [])
        except json.JSONDecodeError:
            pass
    return clean, fragments


def format_fragments_md(fragments: list[dict]) -> str:
    """Convierte los fragmentos en Markdown para mostrar en Gradio."""
    if not fragments:
        return ""
    lines = ["---", "🔍 **Fragmentos recuperados del PDF**", ""]
    for f in fragments:
        score = f.get("score", "—")
        score_str = f"{score:.4f}" if isinstance(score, float) else str(score)
        lines.append(f"**Fragmento {f.get('id', '?')}** — score: `{score_str}`")
        lines.append(f"> {f.get('text', '')}")
        lines.append("")
    return "\n".join(lines)


def respond(user_message: str, history: list[list[str]]) -> tuple[list[list[str]], str]:
    """Llama a la API de Anthropic y devuelve la respuesta con fragmentos."""
    if not user_message.strip():
        return history, ""

    # Construir historial en formato Anthropic
    messages = []
    for human, assistant in history:
        messages.append({"role": "user", "content": human})
        messages.append({"role": "assistant", "content": assistant})
    messages.append({"role": "user", "content": user_message})

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        system=SYSTEM_PROMPT,
        messages=messages,
    )

    raw = response.content[0].text
    clean_text, fragments = parse_fragments(raw)
    fragments_md = format_fragments_md(fragments)

    full_response = clean_text
    if fragments_md:
        full_response += "\n\n" + fragments_md

    history.append([user_message, full_response])
    return history, ""


# ── CSS personalizado (estética anime: oscuro, sakura, violeta) ───────────────
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&family=Zen+Kaku+Gothic+New:wght@900&display=swap');

:root {
    --sakura: #FF6B9D;
    --ink: #1A1028;
    --panel: #211534;
    --panel-light: #2D1F47;
    --accent: #7C4DFF;
    --text: #F0E6FF;
    --muted: #B09CC8;
    --border: rgba(255,107,157,0.25);
}

body, .gradio-container {
    background: var(--ink) !important;
    font-family: 'Noto Sans JP', sans-serif !important;
    color: var(--text) !important;
}

/* Header */
.app-header {
    background: var(--panel);
    border-bottom: 1px solid var(--border);
    padding: 18px 24px;
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 0;
}

.app-header h1 {
    font-family: 'Zen Kaku Gothic New', sans-serif !important;
    font-size: 22px !important;
    font-weight: 900 !important;
    color: var(--text) !important;
    margin: 0 !important;
}

.app-header .subtitle {
    font-size: 12px;
    color: var(--muted);
    margin-top: 2px;
}

.badge {
    font-size: 11px;
    padding: 3px 10px;
    border-radius: 20px;
    font-weight: 500;
    display: inline-block;
    margin: 0 3px;
}

.badge-pink { color: #FF6B9D; border: 1px solid rgba(255,107,157,0.4); background: rgba(255,107,157,0.08); }
.badge-purple { color: #B39DFF; border: 1px solid rgba(124,77,255,0.4); background: rgba(124,77,255,0.08); }

/* Chatbot */
.chat-window { background: var(--ink) !important; border: 1px solid var(--border) !important; border-radius: 12px !important; }
.chat-window .message.bot { background: var(--panel-light) !important; border: 1px solid var(--border) !important; color: var(--text) !important; border-radius: 4px 14px 14px 14px !important; }
.chat-window .message.user { background: rgba(124,77,255,0.15) !important; border: 1px solid rgba(124,77,255,0.3) !important; color: var(--text) !important; border-radius: 14px 4px 14px 14px !important; }

/* Input */
textarea, input[type=text] {
    background: var(--panel-light) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    color: var(--text) !important;
    font-family: 'Noto Sans JP', sans-serif !important;
}
textarea:focus, input[type=text]:focus {
    border-color: var(--sakura) !important;
    box-shadow: 0 0 0 3px rgba(255,107,157,0.1) !important;
}

/* Buttons */
.gr-button-primary, button.primary {
    background: linear-gradient(135deg, #C93777, #7C4DFF) !important;
    border: none !important;
    color: white !important;
    border-radius: 10px !important;
    font-family: 'Noto Sans JP', sans-serif !important;
    font-weight: 700 !important;
}

.gr-button-secondary, button.secondary {
    background: var(--panel-light) !important;
    border: 1px solid var(--border) !important;
    color: var(--muted) !important;
    border-radius: 8px !important;
    font-size: 12px !important;
    font-family: 'Noto Sans JP', sans-serif !important;
}

.gr-button-secondary:hover { border-color: var(--sakura) !important; color: var(--sakura) !important; }

/* Sidebar / accordion */
.gr-accordion { background: var(--panel) !important; border: 1px solid var(--border) !important; border-radius: 10px !important; }
.gr-accordion > .label { color: var(--text) !important; font-weight: 700 !important; }

/* Labels and markdown */
label, .gr-label { color: var(--muted) !important; font-size: 13px !important; }
.gr-markdown p, .gr-markdown li { color: var(--muted) !important; font-size: 13px !important; }
.gr-markdown strong { color: #FFD6E8 !important; }
.gr-markdown blockquote { border-left: 3px solid var(--sakura) !important; padding-left: 10px; color: var(--muted) !important; font-size: 12px !important; }
.gr-markdown code { background: rgba(124,77,255,0.2) !important; color: #FF6B9D !important; padding: 1px 5px; border-radius: 4px; }
.gr-markdown hr { border-color: var(--border) !important; }
"""

# ── Interfaz Gradio ───────────────────────────────────────────────────────────
with gr.Blocks(css=CSS, title="Chatbot: Anime y su Universo Cultural") as demo:

    # ── Header ────────────────────────────────────────────────────────────────
    gr.HTML("""
    <div class="app-header">
        <span style="font-size:32px">🎌</span>
        <div style="flex:1">
            <h1>Chatbot: Anime y su Universo Cultural</h1>
            <div class="subtitle">Basado en fragmentos del libro de Historia del Anime (págs. 12–48)</div>
        </div>
        <div>
            <span class="badge badge-pink">Cultura Japonesa</span>
            <span class="badge badge-purple">RAG · PDF</span>
        </div>
    </div>
    """)

    with gr.Row():
        # ── Sidebar ───────────────────────────────────────────────────────────
        with gr.Column(scale=1, min_width=240):

            with gr.Accordion("📺 Sobre este documento", open=True):
                gr.Markdown("""
Este chatbot está entrenado con el fragmento del libro
**'Descubrir el Anime - Historia & Cultura'** (páginas 12-91).

**Temas principales:**
- Historia y orígenes del anime
- Géneros: Shonen, Shojo, Seinen, Isekai
- Estudios legendarios (Ghibli, MAPPA, Bones)
- El impacto cultural global del anime
""")

            with gr.Accordion("💡 Preguntas de ejemplo", open=True):
                gr.Markdown("Haz clic en una pregunta para usarla:")
                example_btns = []
                for q in EXAMPLE_QUESTIONS:
                    btn = gr.Button(q, variant="secondary", size="sm")
                    example_btns.append(btn)

        # ── Chat principal ────────────────────────────────────────────────────
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(
                value=[[None, "¡Konnichiwa! 🌸 Soy tu asistente experto en anime. "
                               "Puedo responder sobre historia, géneros, estudios y el "
                               "impacto cultural del anime. ¿Qué quieres saber? 🎌"]],
                label="",
                height=480,
                elem_classes=["chat-window"],
                show_label=False,
                avatar_images=(None, "https://em-content.zobj.net/source/twitter/376/cherry-blossom_1f338.png"),
            )

            with gr.Row():
                user_input = gr.Textbox(
                    placeholder="Escribe tu pregunta sobre anime...",
                    show_label=False,
                    scale=5,
                    lines=1,
                    max_lines=4,
                )
                send_btn = gr.Button("Enviar ➤", variant="primary", scale=1, min_width=90)

            clear_btn = gr.Button("🗑 Limpiar conversación", variant="secondary", size="sm")

    # ── Eventos ───────────────────────────────────────────────────────────────
    send_btn.click(respond, [user_input, chatbot], [chatbot, user_input])
    user_input.submit(respond, [user_input, chatbot], [chatbot, user_input])
    clear_btn.click(
        lambda: ([[None, "¡Konnichiwa! 🌸 Conversación reiniciada. ¿Sobre qué anime quieres hablar? 🎌"]], ""),
        outputs=[chatbot, user_input]
    )

    # Botones de ejemplo → rellenan el input
    for btn in example_btns:
        btn.click(lambda q=btn.value: q, outputs=user_input)


# ── Punto de entrada ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    demo.launch(share=False)
