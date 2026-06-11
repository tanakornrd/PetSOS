import streamlit as st
import pandas as pd

# --- 1. System Configuration ---
st.set_page_config(page_title="PetSOS", page_icon="🐾", layout="centered")

# --- 2. Advanced CSS Injection (Apple Store Clone) ---
# เจาะจงแก้สไตล์การ์ดผ่าน Native Border ของ Streamlit เพื่อหลีกเลี่ยง TypeError
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@400;500;600;700&display=swap');
        
        html, body, .stApp, .stMarkdown, p, span, h1, h2, h3, h4, label {
            font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Prompt", sans-serif !important;
            color: #1D1D1F;
        }
        
        .stApp { background-color: #F5F5F7 !important; }
        header, footer, #MainMenu { visibility: hidden !important; }

        /* Apple Store Typography */
        .apple-hero {
            font-size: 48px;
            font-weight: 700;
            letter-spacing: -0.02em;
            line-height: 1.1;
            margin-bottom: 12px;
        }
        .apple-subhero {
            font-size: 22px;
            font-weight: 600;
            color: #86868B;
            line-height: 1.3;
            margin-bottom: 25px;
        }
        .apple-link {
            color: #007AFF;
            font-size: 17px;
            font-weight: 400;
            text-decoration: none;
            display: block;
            margin-bottom: 10px;
        }
        .apple-link:hover { text-decoration: underline; }
        
        .section-header {
            font-size: 24px;
            font-weight: 600;
            letter-spacing: -0.01em;
            margin-top: 20px;
            margin-bottom: 15px;
        }
        .section-header span { color: #86868B; }

        /* Apple Card Styling (Targeting Streamlit's native container border) */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #FFFFFF !important;
            border-radius: 22px !important;
            border: none !important;
            box-shadow: 0 4px 20px rgba(0,0,0,0.04) !important;
            padding: 5px !important;
            transition: transform 0.2s ease;
            margin-bottom: 15px;
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:hover {
            transform: scale(1.01);
        }

        /* Native Look Forms & Buttons */
        div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {
            border-radius: 12px !important;
            border: 1px solid #D2D2D7 !important;
            background-color: #F5F5F7 !important;
        }
        
        .stButton > button {
            border-radius: 14px !important;
            font-weight: 500 !important;
            font-size: 15px !important;
            padding: 12px 24px !important;
            background-color: #F5F5F7 !important;
            color: #007AFF !important;
            border: none !important;
            width: 100% !important;
        }
        .stButton > button:hover { background-color: #E8E8ED !important; }
        
        button[kind="primary"] {
            background-color: #007AFF !important;
            color: white !important;
        }
        button[kind="primary"]:hover { background-color: #0062CC !important; }
    </style>
""", unsafe_allow_html=True)

# --- 3. Page Routing Logic (State Management) ---
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def navigate(page_name):
    st.session_state.page = page_name

# ==========================================
# PAGE 1: Home (Apple Store Layout)
# ==========================================
if st.session_state.page == 'home':
    # Hero Section
    st.markdown("<div class='apple-hero'>PetSOS</div>", unsafe_allow_html=True)
    st.markdown("<div class='apple-subhero'>คือที่ที่ดีที่สุดในการดูแลรักษาสัตว์เลี้ยง<br>ที่คุณรัก</div>", unsafe_allow_html=True)
    
    st.markdown("<a href='#' class='apple-link'>สอบถามกับ Specialist ↗</a>", unsafe_allow_html=True)
    st.markdown("<a href='#' class='apple-link'>ค้นหาโรงพยาบาลสัตว์ 24 ชม. ↗</a>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("<div class='section-header'>บริการของเรา <span>เลือกความช่วยเหลือที่คุณต้องการ</span></div>", unsafe_allow_html=True)

    # Card 1: SOS (Code Red)
    with st.container(border=True):
        st.markdown("<h3 style='margin-bottom:0px; font-size:20px;'>🚨 กรณีฉุกเฉินวิกฤต</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color:#86868B; font-size:14px; margin-bottom:15px;'>หากสัตว์เลี้ยงหมดสติ ชัก หรือหยุดหายใจ</p>", unsafe_allow_html=True)
        # Custom inline style for SOS button logic
        st.markdown("""<style>div:nth-child(1) > div > div > button { background-color: #FF3B30 !important; color: white !important; }</style>""", unsafe_allow_html=True)
        if st.button("🔴 ขอความช่วยเหลือด่วน (SOS)"):
            navigate('sos')
            st.rerun()

    # Card 2: AI Triage Engine
    with st.container(border=True):
        st.markdown("<h3 style='margin-bottom:0px; font-size:20px;'>🩺 ประเมินอาการเบื้องต้น</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color:#86868B; font-size:14px; margin-bottom:15px;'>ให้ AI ช่วยคัดกรองความเร่งด่วนทางการแพทย์</p>", unsafe_allow_html=True)
        
        species = st.selectbox("ชนิดสัตว์เลี้ยง", ["สุนัข", "แมว", "สัตว์แปลก (Exotic)"])
        user_input = st.text_input("อาการที่พบ", placeholder="เช่น ซึม อาเจียน หรือ ไม่กินอาหาร")
        st.file_uploader("แนบรูปภาพ/วิดีโอ (ถ้ามี)", type=['png','jpg','mp4'])
        
        if st.button("ส่งข้อมูลให้ AI ประเมินผล ➡️", type="primary"):
            navigate('result')
            st.rerun()

# ==========================================
# PAGE 2: Code Red (Emergency)
# ==========================================
elif st.session_state.page == 'sos':
    st.markdown("<div class='apple-hero' style='color:#FF3B30;'>Code Red</div>", unsafe_allow_html=True)
    st.markdown("<div class='apple-subhero'>ระบบนำทางฉุกเฉินไปยังโรงพยาบาล<br>ที่ใกล้ที่สุด</div>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("<h3 style='font-size:18px;'>📍 โรงพยาบาลสัตว์จุฬาลงกรณ์</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color:#86868B; font-size:14px;'>ห่างจากตำแหน่งของคุณ 2.4 กม.</p>", unsafe_allow_html=True)
        
        map_data = pd.DataFrame({'lat': [13.7367], 'lon': [100.5331]})
        st.map(map_data)
        
        st.markdown("""<style>div[data-testid="stButton"] button { background-color: #FF3B30 !important; color: white !important; font-weight: bold !important; }</style>""", unsafe_allow_html=True)
        st.button("📞 โทรสายด่วนทันที")
        
    st.write("<br>", unsafe_allow_html=True)
    if st.button("⬅️ ยกเลิกและกลับหน้าหลัก"):
        navigate('home')
        st.rerun()

# ==========================================
# PAGE 3: Result & Telemed
# ==========================================
elif st.session_state.page == 'result':
    st.markdown("<div class='apple-hero'>ผลการประเมิน</div>", unsafe_allow_html=True)
    st.markdown("<div class='apple-subhero'>คำแนะนำทางการแพทย์โดย AI Triage</div>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("<h3 style='font-size:20px; color:#F59E0B;'>🟡 ระดับสีเหลือง (Observe)</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color:#424245; font-size:15px; margin-bottom:15px;'>อาการพ้นขีดอันตรายเฉียบพลัน แนะนำให้สังเกตอาการ หรือปรึกษาสัตวแพทย์ทางไกล</p>", unsafe_allow_html=True)
        st.button("🎥 เข้าห้องสนทนากับแพทย์ (รอคิว 12 นาที)", type="primary")
        
    st.markdown("<div class='section-header'>ตัวเลือกเพิ่มเติม</div>", unsafe_allow_html=True)
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<p style='font-weight:600; font-size:14px; margin-bottom:0;'>ปรึกษารายครั้ง</p>", unsafe_allow_html=True)
            st.button("ชำระ 350฿")
        with col2:
            st.markdown("<p style='font-weight:600; font-size:14px; margin-bottom:0;'>สมัคร Premium</p>", unsafe_allow_html=True)
            st.button("รายเดือน 299฿", type="primary")

    st.write("<br>", unsafe_allow_html=True)
    if st.button("⬅️ กลับหน้าหลัก"):
        navigate('home')
        st.rerun()
