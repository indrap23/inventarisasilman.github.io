import streamlit as st
import streamlit.components.v1 as components

# --- Konfigurasi halaman agar menggunakan layout lebar ---
st.set_page_config(layout="wide")

# --- CSS untuk menghapus padding di sekitar komponen HTML ---
st.markdown(
    """
    <style>
        .block-container {
            padding: 0 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Memuat dan menampilkan file HTML ---
try:
    with open('sistem.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Menampilkan konten HTML dengan tinggi yang cukup dan scrolling
    components.html(html_content, height=1200, scrolling=True)

except FileNotFoundError:
    st.error("File 'sistem_v0.2.html' tidak ditemukan. Pastikan file tersebut berada di direktori yang sama.")

