import base64
import streamlit as st


def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(image_path, opacity=0.5, size="cover"):
    bg_image = get_base64_image(image_path)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: transparent;
        }}
        .stApp::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url("data:image/jpg;base64,{bg_image}");
            background-size: {size};
            background-position: center;
            background-repeat: no-repeat;
            opacity: {opacity};
            z-index: -1;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )