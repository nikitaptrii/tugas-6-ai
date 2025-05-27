# Nama : Nikita Putri Prabowo
# NPM : 140810230010
# Kelas : B 
# Judul : Tugas 6 Praktikum AI

import streamlit as st
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import io

def get_colors(image, n_colors=5):
    image = image.resize((150, 150))  # Resize untuk efisiensi
    img_np = np.array(image).reshape(-1, 3)
    kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(img_np)
    colors = kmeans.cluster_centers_.astype(int)
    return colors

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

st.set_page_config(page_title="Color Picker", layout="centered")
st.title("🎨 Extract Dominant Colors from Image")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    with st.spinner("Extracting colors..."):
        colors = get_colors(image)
        st.subheader("🎨 Dominant Color Palette")

        cols = st.columns(len(colors))
        for i, col in enumerate(cols):
            rgb = tuple(colors[i])
            hex_code = rgb_to_hex(rgb)
            with col:
                st.color_picker(label="", value=hex_code, key=f"color_{i}")
                st.write(f"RGB: {rgb}")
                st.write(f"Hex: {hex_code}")
