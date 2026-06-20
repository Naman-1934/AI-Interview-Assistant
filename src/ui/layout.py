import streamlit as st

PRIMARY = "#6C5CE7"
ACCENT = "#2DD4BF"
BG = "#0B0E14"
CARD = "#161B26"
BORDER = "#262C3B"
TEXT = "#E5E7EB"
MUTED = "#8B93A7"

STEPS = [
    {"key": "home", "label": "Home", "page": "app.py"},
    {"key": "resume", "label": "Resume", "page": "pages/1_Upload_Resume.py"},
    {"key": "interview", "label": "Interview", "page": "pages/2_Interview.py"},
    {"key": "scorecard", "label": "Scorecard", "page": "pages/3_Scorecard.py"},
]


def inject_base_css():
    css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&display=swap');

    [data-testid="stSidebar"] { display: none; }
    [data-testid="stSidebarCollapsedControl"] { display: none; }
    header[data-testid="stHeader"] { background: transparent; }
    [data-testid="stHeaderActionElements"] { display: none; }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: TEXT_COLOR;
    }

    .stApp {
        background: BG_COLOR;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1100px;
    }

    h1, h2, h3 {
        font-family: 'Space Grotesk', sans-serif !important;
        letter-spacing: -0.02em;
    }

    .navbar-brand-row {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 4px;
    }

    .navbar-brand-row span {
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        font-size: 1.3rem;
        color: TEXT_COLOR;
    }

    div[data-testid="stHorizontalBlock"] div[data-testid="stButton"] button[kind="secondary"] {
        border-radius: 999px;
        font-weight: 600;
        font-size: 0.9rem;
        border: 1px solid BORDER_COLOR;
        background: CARD_COLOR;
        color: MUTED_COLOR;
        padding: 0.5rem 0;
        width: 100%;
        transition: all 0.15s ease;
    }

    div[data-testid="stHorizontalBlock"] div[data-testid="stButton"] button[kind="secondary"]:hover {
        border-color: PRIMARY_COLOR;
        color: TEXT_COLOR;
    }

    div[data-testid="stHorizontalBlock"] div[data-testid="stButton"] button[kind="primary"] {
        border-radius: 999px;
        font-weight: 700;
        font-size: 0.9rem;
        border: none;
        background: PRIMARY_COLOR;
        color: white;
        padding: 0.5rem 0;
        width: 100%;
    }

    .app-card {
        background: CARD_COLOR;
        border: 1px solid BORDER_COLOR;
        border-radius: 16px;
        padding: 32px 36px;
        margin-bottom: 24px;
    }

    .eyebrow {
        font-family: 'Inter', sans-serif;
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: ACCENT_COLOR;
        margin-bottom: 6px;
    }

    .hero-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2.6rem;
        font-weight: 700;
        line-height: 1.15;
        letter-spacing: -0.02em;
        margin-bottom: 14px;
    }

    .hero-sub {
        font-size: 1.05rem;
        color: MUTED_COLOR;
        max-width: 640px;
        margin-bottom: 8px;
    }

    .step-card {
        background: BG_COLOR;
        border: 1px solid BORDER_COLOR;
        border-radius: 12px;
        padding: 20px;
        height: 100%;
    }

    .step-num {
        font-family: 'Space Grotesk', sans-serif;
        color: PRIMARY_COLOR;
        font-weight: 700;
        font-size: 1.1rem;
        margin-bottom: 8px;
    }

    .step-title {
        font-weight: 600;
        margin-bottom: 6px;
    }

    .step-desc {
        color: MUTED_COLOR;
        font-size: 0.88rem;
        line-height: 1.5;
    }

    div[data-testid="stVerticalBlock"] > div[data-testid="stElementContainer"]:has(div.app-card) {
        margin-bottom: 0;
    }
    </style>
    """

    css = css.replace("TEXT_COLOR", TEXT)
    css = css.replace("BG_COLOR", BG)
    css = css.replace("CARD_COLOR", CARD)
    css = css.replace("BORDER_COLOR", BORDER)
    css = css.replace("MUTED_COLOR", MUTED)
    css = css.replace("PRIMARY_COLOR", PRIMARY)
    css = css.replace("ACCENT_COLOR", ACCENT)

    st.markdown(css, unsafe_allow_html=True)


def render_navbar(active_key):
    st.markdown(
        '<div class="navbar-brand-row"><span>🤖 AI Interview Assistant</span></div>',
        unsafe_allow_html=True
    )

    cols = st.columns(len(STEPS))

    for i, step in enumerate(STEPS):
        with cols[i]:
            is_active = step["key"] == active_key
            if st.button(
                step["label"],
                key=f"nav_{step['key']}",
                type="primary" if is_active else "secondary",
                use_container_width=True
            ):
                if not is_active:
                    st.switch_page(step["page"])


def nav_buttons(current_key):
    """Back / Next buttons. Caller places this inside their own app-card div."""
    order = ["home", "resume", "interview", "scorecard"]
    idx = order.index(current_key)
    is_last_step = idx == len(order) - 1

    if is_last_step:
        # Scorecard: only show Back, no Next
        cols = st.columns([1, 2])
        with cols[0]:
            if st.button(f"← Back to {STEPS[idx - 1]['label']}", use_container_width=True, key=f"back_{current_key}"):
                st.switch_page(STEPS[idx - 1]["page"])
        return

    cols = st.columns([1, 1, 1])

    with cols[0]:
        if idx > 0:
            if st.button(f"← Back to {STEPS[idx - 1]['label']}", use_container_width=True, key=f"back_{current_key}"):
                st.switch_page(STEPS[idx - 1]["page"])

    with cols[2]:
        if st.button(f"{STEPS[idx + 1]['label']} →", type="primary", use_container_width=True, key=f"next_{current_key}"):
            st.switch_page(STEPS[idx + 1]["page"])