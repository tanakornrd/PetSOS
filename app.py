import streamlit as st
import pandas as pd

# --- 1. System Configuration & Clean Canvas Base ---
st.set_page_config(layout="centered")

# Surgical CSS Injection for Apple Aesthetic
st.markdown("""
    <style>
        /* Typography: Apple Standard Font (SF Pro-like) */
        @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&display=swap');
        html, body, .stApp, .stMarkdown, p, span, h1, h2, h3, h4, h5, h6 {
            font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Prompt", sans-serif !important;
            color: #1D1D1F;
        }

        /* Platform Base: Apple Canvas Background */
        .stApp {
            background-color: #F5F5F7 !important;
        }

        /* 🖼️ Card-based Layout: Defining Container Styles */
        .apple-card {
            background-color: #FFFFFF;
            border-radius: 20px;
            border: 1px solid #E8E8ED;
            padding: 25px;
            margin-bottom: 25px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        }

        /* Defining Upload Area as an " Institutional Card " */
        .apple-upload-card {
            background-color: #FFFFFF;
            border-radius: 16px;
            border: 2px dashed #D2D2D7;
            padding: 20px;
            text-align: center;
            margin-top: 10px;
        }

        /* 📝 Typography Classes for Premium Look */
        .apple-hero-title {
            font-size: 40px;
            font-weight: 700;
            letter-spacing: -1px;
            text-align: left;
            margin-bottom: 5px;
        }
        .apple-hero-subtitle {
            font-size: 18px;
            font-weight: 400;
            color: #86868B;
            text-align: left;
            margin-bottom: 40px;
        }
        .apple-section-title {
            font-size: 20px;
            font-weight: 600;
            color: #1D1D1F;
            margin-bottom: 15px;
            letter-spacing: -0.2px;
        }
        .apple-field-label {
            font-size: 14px;
            font-weight: 600;
            color: #1D1D1F;
            margin-bottom: 6px;
        }
        .apple-placeholder-label {
            color: #86868B;
        }

        /* 🔘 Native Look Buttons & Elements */
        /* Formatting the dropdown */
        .stSelectbox > div > div > div {
            border-radius: 12px;
            border: 1px solid #D2D2D7;
            padding: 12px;
            background-color: #F5F5F7;
        }

        /* Formatting the text input */
        .stTextInput > div > div > input {
            border-radius: 12px;
            border: 1px solid #D2D2D7;
            padding: 12px;
        }

        /* Formatting General Buttons */
        .stButton > button {
            border-radius: 12px;
            font-weight: 500;
            padding: 12px 24px;
            transition: all 0.15s ease-in-out;
            width: 100%;
        }
        .stButton > button:hover {
            transform: translateY(-1px);
        }

        /* Institutional Style formatting for SOS Button */
        .sos-button > button {
            background-color: #FF3B30 !important;
            color: white !important;
            border: none !important;
            font-weight: 700 !important;
        }
        .sos-button > button:hover {
            background-color: #E03126 !important;
        }

        /* Apple UI primary accent formatting for Action Button */
        .action-button > button {
            background-color: #007AFF !important;
            color: white !important;
            border: none !important;
            font-weight: 600 !important;
        }
        .action-button > button:hover {
            background-color: #0062CC !important;
        }

        /* Formatting file uploader area */
        .stFileUploader section > button {
            background-color: #007AFF;
            color: white;
            border-radius: 12px;
        }

        /* Hide unnecessary system elements for clean Institutional Look */
        header {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 2. Identity Area ---
# Creating the hero title structure inspired by apple.com
st.markdown("<h1 class='apple-hero-title'>PetSOS</h1>", unsafe_allow_html=True)
st.markdown("<p class='apple-hero-subtitle'>Medical Decision Support & Triage Platform</p>", unsafe_allow_html=True)

# --- 3. Feature 1: One-Tap SOS Card ---
# Formatting it as a distinct premium card
with st.container(css_classes=["apple-card", "sos-button"]):
    st.markdown("<h2 class='apple-section-title'>Feature 1 • One-Tap SOS</h2>", unsafe_allow_html=True)
    
    # Keeping the original functionality of the SOS button
    if st.button("🔴 ONE-TAP SOS ขอความช่วยเหลือด่วน"):
        st.error("🆘 SOS ACTIVATED - Emergency support is on the way.")

# --- 4. Feature 2: AI Triage Engine Card ---
# Formatting as a larger distinct premium card
with st.container(css_classes=["apple-card"]):
    st.markdown("<h2 class='apple-section-title'>Feature 2 • AI Triage Engine</h2>", unsafe_allow_html=True)

    # 📝 Input Fields with native Apple look formatting
    st.markdown("<p class='apple-field-label'>ชนิดสัตว์เลี้ยงของคุณ</p>", unsafe_allow_html=True)
    st.selectbox("Select Pet Type", ["สุนัข", "แมว", "สัตว์แปลก (Exotic)"], label_visibility="collapsed")
    
    st.markdown("<p class='apple-field-label'>ระบุอาการของสัตว์เลี้ยงอย่างกระชับ:</p>", unsafe_allow_html=True)
    st.text_input("Enter Pet Symptom", placeholder="เช่น สุนัขมีอาการชักและหมดสติ หรือ ซึมไม่กินอาหาร", label_visibility="collapsed")

    # 📷 Institutional Style formatting for Upload Area Card
    st.markdown("<p class='apple-field-label'>📷 แนบรูปภาพหรือวิดีโออาการสั้นเพื่อเพิ่มความแม่นยำ (Optional)</p>", unsafe_allow_html=True)
    with st.container(css_classes=["apple-upload-card"]):
        # Header text inside the card
        st.markdown("<p style='font-size: 14px; font-weight: 500; text-align: center;'>Upload (Optional)</p>", unsafe_allow_html=True)
        # Detailed instruction text inside the card
        st.markdown("<p style='font-size: 12px; color: #86868B; text-align: center;'>200MB per file • PNG, JPG, MP4</p>", unsafe_allow_html=True)
        # Original file uploader function, collapses its own label to let the Card Header take precedence
        st.file_uploader("Select symptom file", label_visibility="collapsed")

# --- 5. Action Button ---
# Primary action button with Apple blue styling
st.markdown("<div class='action-button'>", unsafe_allow_html=True)
if st.button("ส่งข้อมูลให้ AI ประเมินผล ➡️", type="primary"):
    st.success("🤖 Information submitted. AI is processing the triage.")
st.markdown("</div>", unsafe_allow_html=True)
