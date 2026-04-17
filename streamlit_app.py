import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Capacitación · Protocolo de Soporte YOM",
    page_icon="🕵️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit chrome for a clean training experience
st.markdown(
    """
    <style>
    #MainMenu, header, footer, [data-testid="stToolbar"] { display: none !important; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    iframe { border: none !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "capacitacion.html"
html_content = html_path.read_text(encoding="utf-8")

st.components.v1.html(html_content, height=900, scrolling=True)
