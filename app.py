import streamlit as st
import streamlit.components.v1 as components

# Mengatur konfigurasi halaman agar lebih lega
st.set_page_config(layout="wide")

# Judul aplikasi di Streamlit
st.title("Sistem Inventarisasi Aset LMAN via Streamlit")
st.write("Aplikasi web interaktif berikut di-render dari sebuah file HTML tunggal.")

# --- CSS KUSTOM UNTUK MEMPERLEBAR KONTEN ---
# Trik ini memaksa kontainer utama Streamlit untuk menggunakan lebar penuh.
st.markdown(
    """
    <style>
    .st-emotion-cache-1y4p8pa {
        max-width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Membuka dan membaca konten dari file HTML
try:
    with open('sistem.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Menampilkan konten HTML di dalam Streamlit
    # Mengatur tinggi ke 1200px untuk memberikan ruang yang cukup bagi aplikasi.
    # Scrolling='auto' (default) akan menampilkan scrollbar jika konten melebihi tinggi.
    components.html(html_content, height=1200, scrolling=True)

except FileNotFoundError:
    st.error("File 'sistem.html' tidak ditemukan. Pastikan file tersebut berada di direktori yang sama dengan skrip Streamlit Anda.")

# Informasi tambahan di bagian bawah
st.info("© 2024 By DOTI LMAN with 𖹭 𖹭 𖹭. Aplikasi ini dijalankan di dalam container Streamlit.")
