import streamlit as st
import streamlit.components.v1 as components

# Mengatur konfigurasi halaman agar lebih lega
st.set_page_config(layout="wide")



# Membuka dan membaca konten dari file HTML
try:
    with open('sistem.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Menampilkan konten HTML di dalam Streamlit
    # Mengatur tinggi ke 1200px untuk memberikan ruang yang cukup bagi aplikasi.
    # Scrolling='auto' (default) akan menampilkan scrollbar jika konten melebihi tinggi.
    components.html(html_content)
