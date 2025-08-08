import streamlit as st
import streamlit.components.v1 as components

# --- KONFIGURASI HALAMAN ---
st.set_page_config(layout="wide")

# --- CSS KUSTOM UNTUK TAMPILAN PENUH ---
# Menghapus semua padding dari kontainer utama agar komponen HTML bisa melebar penuh.
st.markdown(
    """
    <style>
        /* Target the main block container and remove all padding */
        .block-container {
            padding: 0 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- MEMUAT DAN MENAMPILKAN HTML ---
try:
    # Pastikan nama file 'sistem_v0.2.html' sudah benar.
    with open('sistem.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Menampilkan konten HTML.
    components.html(html_content, height=1200, scrolling=True)

except FileNotFoundError:
    st.error("File 'sistem_v0.2.html' tidak ditemukan. Pastikan file tersebut berada di direktori yang sama dengan skrip Streamlit Anda.")
