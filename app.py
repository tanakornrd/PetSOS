import streamlit as st

# --- 1. System Configuration ---
st.set_page_config(page_title="PetSOS", page_icon="🐾", layout="centered", initial_sidebar_state="collapsed")

# --- 2. Apple-Style CSS Injection ---
st.markdown("""
    <style>
        /* Typography - Apple Native Feel & Thai Prompt Font */
        @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;600&display=swap');
        
        html, body, [class*="css"], .stMarkdown {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Prompt", sans-serif !important;
        }

        /* Clean whitespace and hidden elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Button Styling - Pill shape, smooth hover */
        .stButton > button {
            border-radius: 14px !important;
            font-weight: 600 !important;
            font-size: 16px !important;
            padding: 10px 24px !important;
            border: none !important;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05) !important;
            transition: all 0.2s ease-in-out !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1) !important;
        }

        .stButton > button:active {
            transform: scale(0.96);
        }

        /* Primary Button Color (Apple Blue) */
        button[kind="primary"] {
            background-color: #007AFF !important;
            color: white !important;
        }

        /* Callout / Alert Cards */
        div[data-testid="stAlert"] {
            border-radius: 16px !important;
            border: none !important;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04) !important;
        }
        
        /* Selectbox/Radio Styling */
        div[data-baseweb="select"] > div {
            border-radius: 12px !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- 3. Session State Management ---
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def go_to_page(page_name):
    st.session_state.page = page_name

# --- 4. Page 1: Home ---
if st.session_state.page == 'home':
    st.markdown("<h1 style='text-align: center; font-weight: 600; letter-spacing: -0.5px;'>🐾 PetSOS</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666; font-size: 18px; margin-bottom: 30px;'>ระบบคัดกรองความเร่งด่วนทางการแพทย์</p>", unsafe_allow_html=True)
    
    st.error("🚨 **Code Red:** หากสัตว์เลี้ยงหมดสติ ชัก หรือหยุดหายใจ กรุณารีบพาส่งโรงพยาบาลทันทีโดยไม่ต้องประเมิน")
    
    st.write("") # Spacer
    if st.button("🆘 เริ่มประเมินอาการฉุกเฉิน", type="primary", use_container_width=True):
        go_to_page('triage')

# --- 5. Page 2: Triage Form ---
elif st.session_state.page == 'triage':
    st.markdown("<h2 style='font-weight: 600;'>🩺 ประเมินอาการ</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #666;'>กรุณาเลือกข้อมูลที่ตรงกับสัตว์เลี้ยงของคุณมากที่สุด</p>", unsafe_allow_html=True)
    
    # Use Radio buttons instead of Selectbox for faster 1-tap mobile experience
    st.write("**1. สัตว์เลี้ยงของคุณคืออะไร?**")
    species = st.radio("ชนิดสัตว์เลี้ยง", ["🐶 สุนัข", "🐱 แมว", "🦜 สัตว์แปลก (Exotic)"], label_visibility="collapsed")
    
    st.write("")
    st.write("**2. อาการหลักที่พบ (อาการที่กังวลที่สุด)**")
    symptom = st.radio("อาการ", [
        "อาเจียนไม่หยุด / ถ่ายเหลว", 
        "ซึม ไม่กินอาหาร", 
        "หายใจหอบลำบาก / เหงือกซีด",
        "มีบาดแผลเลือดออก"
    ], label_visibility="collapsed")
    
    st.write("") # Spacer
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ ย้อนกลับ", use_container_width=True): 
            go_to_page('home')
    with col2:
        if st.button("ประเมินผล ➡️", type="primary", use_container_width=True):
            st.session_state.symptom = symptom
            go_to_page('result')

# --- 6. Page 3: Result ---
elif st.session_state.page == 'result':
    st.markdown("<h2 style='font-weight: 600;'>📊 ผลการประเมินเบื้องต้น</h2>", unsafe_allow_html=True)
    symptom = st.session_state.get('symptom', '')
    
    # Triage Logic Application
    if "หายใจหอบลำบาก" in symptom or "อาเจียนไม่หยุด" in symptom or "เลือดออก" in symptom:
        st.warning("⚠️ **ระดับสีส้ม (Urgent):** ความเสี่ยงสูง\n\nแนะนำให้ปรึกษาสัตวแพทย์อย่างเร่งด่วนเพื่อประเมินอาการอย่างละเอียด")
    else:
        st.info("🟡 **ระดับสีเหลือง (Observe):** ความเร่งด่วนต่ำ\n\nสามารถเฝ้าดูอาการที่บ้านได้ หรือปรึกษาแพทย์ผ่านระบบ Telemedicine เพื่อความสบายใจ")
        
    st.write("")
    st.success("✨ **PetSOS Premium**\n\nอัปเกรดวันนี้ รับสิทธิ์ปรึกษาสัตวแพทย์ทางไกล (Telemedicine) ฟรี 1 ครั้ง/เดือน")
    
    st.write("") # Spacer
    if st.button("กลับหน้าหลัก", use_container_width=True):
        st.session_state.symptom = ''
        go_to_page('home')
