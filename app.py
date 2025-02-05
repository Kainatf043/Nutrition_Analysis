from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = """
    You are an expert nutritionist. Analyze the food items from the image
    and calculate the total calories. Provide details of each food item with its calories
    in the following format:

    🍕 Item 1 - X calories
    🥗 Item 2 - Y calories
    🍔 Item 3 - Z calories
    ----
    Total Calories: XXXX kcal
    """
    response = model.generate_content([prompt, image])
    return response.text

# Streamlit App UI Setup
st.set_page_config(page_title="Gemini Health App", layout="wide")

# Sidebar for File Upload
st.sidebar.header("📤 Upload Image")
uploaded_file = st.sidebar.file_uploader("Choose a food image...", type=["jpg", "jpeg", "png"])

st.title("🍽️ Gemini Health App- 🥗Nutrition Analysis")
#st.write("Upload a food image, and I'll estimate the total calories! 🥗🍕🍔")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='📸 Uploaded Image', use_container_width=True)

    
    if st.button("🔍 Analyze Calories"):
        response = get_gemini_response(image)
        
        # Display Response in a Chat Bubble
        st.markdown(f"""
        <div style="background-color:#f1f1f1; padding:10px; border-radius:10px;">
        <b>💬 Gemini:</b> {response}
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("Upload a food image, and I'll estimate the total calories! 🥗🍕🍔")
