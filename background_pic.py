import base64
import streamlit as st


def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(image_path, opacity=0.5, overlay_color="255, 255, 255", size="cover"):
    bg_image = get_base64_image(image_path)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image:
                linear-gradient(rgba({overlay_color}, {opacity}), rgba({overlay_color}, {opacity})),
                url("data:image/jpg;base64,{bg_image}");
            background-size: {size};
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )