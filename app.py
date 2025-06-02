import cv2
import streamlit as st
import numpy as np
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Image Converter App", layout="centered")
st.title("🖼️ Image Converter App")

# Upload image
img_file = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])

# Mode selection
mode = st.radio("Choose image mode:", ["Color", "Black & White"])

# Resolution choice
resolution_type = st.radio("Choose resolution type:", ["Custom", "HD (1280x720)", "Full HD (1920x1080)"])

# Custom resolution sliders
if resolution_type == "Custom":
    w = st.slider("Select Width", min_value=100, max_value=1920, step=100, value=400)
    h = st.slider("Select Height", min_value=100, max_value=1080, step=100, value=400)
elif resolution_type == "HD (1280x720)":
    w, h = 1280, 720
elif resolution_type == "Full HD (1920x1080)":
    w, h = 1920, 1080

if img_file:
    # Read and decode the image
    file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if img is not None:
        # Resize to chosen resolution
        resized = cv2.resize(img, (w, h), interpolation=cv2.INTER_CUBIC)

        # Convert based on mode
        if mode == "Black & White":
            processed = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
            st.image(processed, channels="GRAY", caption="Black & White Image")
        else:
            processed = resized
            rgb_img = cv2.cvtColor(processed, cv2.COLOR_BGR2RGB)
            st.image(rgb_img, caption="Color Image")

        # Prepare download
        def convert_to_bytes(img_array):
            if len(img_array.shape) == 2:
                pil_img = Image.fromarray(img_array)
            else:
                pil_img = Image.fromarray(cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB))
            buf = BytesIO()
            pil_img.save(buf, format="PNG")
            byte_im = buf.getvalue()
            return byte_im

        st.download_button(
            label="📥 Download HD Image",
            data=convert_to_bytes(processed),
            file_name="converted_hd_image.png",
            mime="image/png"
        )
    else:
        st.error("Could not decode the image. Please try again.")
else:
    st.info("👆 Please upload an image to begin.")
