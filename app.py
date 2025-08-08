import streamlit as st
import streamlit.components.v1 as components

# --- KONFIGURASI HALAMAN ---
st.set_page_config(layout="wide")

# --- JUDUL APLIKASI ---
st.title("Sistem Inventarisasi Aset LMAN")
st.write("Aplikasi web interaktif berikut di-render dari sebuah file HTML tunggal di dalam kontainer Streamlit.")

# --- CSS KUSTOM YANG LEBIH STABIL ---
# Selector ini menargetkan elemen utama halaman secara lebih umum,
# sehingga tidak akan terpengaruh oleh perubahan nama kelas otomatis dari Streamlit.
st.markdown(
    """
    <style>
        .main .block-container {
            max-width: 100%;
            padding-top: 2rem;
            padding-right: 2rem;
            padding-left: 2rem;
            padding-bottom: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# --- MEMUAT DAN MENAMPILKAN HTML ---
# Membuka dan membaca konten dari file HTML.
try:
    with open('sistem.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Menampilkan konten HTML di dalam Streamlit.
    components.html(html_content, height=1200, scrolling=True)

except FileNotFoundError:
    st.error("File 'sistem.html' tidak ditemukan. Pastikan file tersebut berada di direktori yang sama dengan skrip Streamlit Anda.")

# --- FOOTER ---
st.info("© 2025 LMAN. Hak Cipta Dilindungi.")
