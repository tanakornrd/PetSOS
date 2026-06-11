import streamlit as st
import pandas as pd

# --- 1. System Configuration ---
st.set_page_config(page_title="PetSOS", page_icon="🐾", layout="centered")

# --- 2. Apple Store Exact CSS Architecture ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@400;500;600;700&display=swap');
        
        /* 1. Global Typography & Background */
        html, body, .stApp, .stMarkdown, p, span, h1, h2, h3, h4, label {
            font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Prompt", sans-serif !important;
            color: #1D1D1F;
        }
        .stApp { background-color: #F5F5F7 !important; }
        header, footer, #MainMenu { visibility: hidden !important; }

        /* 2. Apple Store Hero Headings (อิงจากภาพอ้างอิง) */
        .apple-hero {
            font-size: 46px;
            font-weight: 700;
            letter-spacing: -1.5px;
            line-height: 1.1;
            margin-bottom: 8px;
            color: #1D1D1F;
        }
        .apple-subhero {
            font-size: 22px;
            font-weight: 600;
            color: #86868B;
            line-height: 1.3;
            margin-bottom: 25px;
            letter-spacing: -0.5px;
        }

        /* 3. Segmented Control (ทำแถบด้านบนให้เหมือน Apple iOS Menu) */
        div[data-testid="stRadio"] > div {
            background-color: #E8E8ED !important;
            padding: 4px !important;
            border-radius: 12px !important;
            gap: 4px !important;
        }
        /* ซ่อนวงกลม Radio ออกเพื่อให้ดูเป็นปุ่มกด */
        div[data-testid="stRadio"] div[role="radio"] div:first-child {
            display: none !important;
        }
        div[data-testid="stRadio"] div[role="radio"] {
            padding: 8px 12px !important;
            border-radius: 8px !important;
            background-color: transparent !important;
            transition: all 0.2s ease !important;
        }
        div[data-testid="stRadio"] div[role="radio"][aria-checked="true"] {
            background-color: #FFFFFF !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05) !important;
        }
        div[data-testid="stRadio"] label p {
            font-weight: 600 !important;
            font-size: 14px !important;
            margin: 0 !important;
            color: #1D1D1F !important;
        }

        /* 4. White Card Containers */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #FFFFFF !important;
            border-radius: 18px !important;
            border: 1px solid #D2D2D7 !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.03) !important;
            padding: 15px !important;
            margin-bottom: 20px !important;
        }

        /* 5. Inputs & Dropdowns */
        div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {
            border-radius: 12px !important;
            border: 1px solid #D2D2D7 !important;
            background-color: #F5F5F7 !important;
        }
        
        /* --- 🩹 SURGICAL FIX: File Uploader (แก้บั๊กฟอนต์ซ้อน) --- */
        /* แต่งเฉพาะกรอบนอก ไม่แตะปุ่มข้างในเด็ดขาด */
        div[data-testid="stFileUploader"] section {
            border: 1px dashed #D2D2D7 !important;
            background-color: #F5F5F7 !important;
            border-radius: 12px !important;
            padding: 15px !important;
        }

        /* 6. Standard Apple Buttons */
        div[data-testid="stButton"] > button {
            border-radius: 12px !important;
            font-weight: 500 !important;
            font-size: 15px !important;
            padding: 10px 20px !important;
            background-color: #F5F5F7 !important;
            color: #007AFF !important;
            border: none !important;
            width: 100% !important;
        }
        div[data-testid="stButton"] > button:hover { background-color: #E8E8ED !important; }
        
        div[data-testid="stButton"] > button[kind="primary"] {
            background-color: #007AFF !important;
            color: white !important;
        }
        div[data-testid="stButton"] > button[kind="primary"]:hover { background-color: #0062CC !important; }
    </style>
""", unsafe_allow_html=True)

# --- 3. State Management (Routing & Navigation) ---
if 'workspace' not in st.session_state:
    st.session_state.workspace = '📱 B2C (ผู้ใช้)'
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def navigate(page_name):
    st.session_state.page = page_name

# --- 4. TOP NAVIGATION (Segmented Control) ---
# แถบเลือกสลับหน้าต่างที่ออกแบบใหม่ให้เป็นปุ่มแคปซูลสไตล์ Apple
selected_workspace = st.radio(
    "Select Workspace:",
    ['📱 B2C (ผู้ใช้)', '🩺 B2B (คลินิก)', '🌐 Backend'],
    horizontal=True,
    label_visibility="collapsed"
)
st.write("<br>", unsafe_allow_html=True)

# ==========================================
# WORKSPACE 1: B2C App (Pet Parents)
# ==========================================
if selected_workspace == '📱 B2C (ผู้ใช้)':
    
    # ---------------- PAGE: HOME ----------------
    if st.session_state.page == 'home':
        st.markdown("<div class='apple-hero'>PetSOS</div>", unsafe_allow_html=True)
        st.markdown("<div class='apple-subhero'>คือที่ที่ดีที่สุดในการดูแล<br>สัตว์เลี้ยงที่คุณรัก</div>", unsafe_allow_html=True)
        st.write("<br>", unsafe_allow_html=True)

        # Feature: Code Red
        with st.container(border=True):
            st.markdown("<h3 style='margin-bottom:0px; font-size:22px; font-weight:700;'>🚨 กรณีฉุกเฉินวิกฤต</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:#86868B; font-size:15px; margin-bottom:15px; font-weight:500;'>หากสัตว์เลี้ยงหมดสติ ชัก หรือหยุดหายใจ</p>", unsafe_allow_html=True)
            st.markdown("""<style>div:nth-child(1) > div > div > button { background-color: #FF3B30 !important; color: white !important; font-weight:600 !important; }</style>""", unsafe_allow_html=True)
            if st.button("🔴 ขอความช่วยเหลือด่วน (SOS)"):
                navigate('sos')
                st.rerun()

        # Feature: Triage Engine
        with st.container(border=True):
            st.markdown("<h3 style='margin-bottom:0px; font-size:22px; font-weight:700;'>🩺 ประเมินอาการเบื้องต้น</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:#86868B; font-size:15px; margin-bottom:15px; font-weight:500;'>ให้ AI ช่วยคัดกรองความเร่งด่วนทางการแพทย์</p>", unsafe_allow_html=True)
            
            st.markdown("<p style='font-size:14px; font-weight:600; margin-bottom:4px;'>ชนิดสัตว์เลี้ยง</p>", unsafe_allow_html=True)
            species = st.selectbox("ชนิดสัตว์เลี้ยง", ["สุนัข", "แมว", "สัตว์แปลก (Exotic)"], label_visibility="collapsed")
            
            st.markdown("<p style='font-size:14px; font-weight:600; margin-bottom:4px; margin-top:10px;'>อาการที่พบ</p>", unsafe_allow_html=True)
            user_input = st.text_input("อาการที่พบ", placeholder="เช่น ซึม อาเจียน หรือ ไม่กินอาหาร", label_visibility="collapsed")
            
            st.markdown("<p style='font-size:14px; font-weight:600; margin-bottom:4px; margin-top:10px;'>แนบรูปภาพ/วิดีโอ (ถ้ามี)</p>", unsafe_allow_html=True)
            st.file_uploader("แนบไฟล์", type=['png','jpg','mp4'], label_visibility="collapsed")
            
            st.write("")
            if st.button("ส่งข้อมูลให้ AI ประเมินผล", type="primary"):
                navigate('result')
                st.rerun()

    # ---------------- PAGE: SOS (Code Red) ----------------
    elif st.session_state.page == 'sos':
        st.markdown("<div class='apple-hero' style='color:#FF3B30;'>Code Red</div>", unsafe_allow_html=True)
        st.markdown("<div class='apple-subhero'>ระบบนำทางฉุกเฉินไปยัง<br>โรงพยาบาลที่ใกล้ที่สุด</div>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("<h3 style='font-size:20px; font-weight:700;'>📍 โรงพยาบาลสัตว์จุฬาลงกรณ์</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:#86868B; font-size:15px; font-weight:500;'>ห่างจากตำแหน่งของคุณ 2.4 กม.</p>", unsafe_allow_html=True)
            
            map_data = pd.DataFrame({'lat': [13.7367], 'lon': [100.5331]})
            st.map(map_data)
            
            st.markdown("""<style>div[data-testid="stButton"] button { background-color: #FF3B30 !important; color: white !important; font-weight: 600 !important; }</style>""", unsafe_allow_html=True)
            st.button("📞 โทรสายด่วนทันที")
            
        st.write("<br>", unsafe_allow_html=True)
        if st.button("⬅️ ยกเลิกและย้อนกลับ"):
            navigate('home')
            st.rerun()

    # ---------------- PAGE: RESULT ----------------
    elif st.session_state.page == 'result':
        st.markdown("<div class='apple-hero'>ผลการประเมิน</div>", unsafe_allow_html=True)
        st.markdown("<div class='apple-subhero'>คำแนะนำทางการแพทย์โดย<br>AI Triage</div>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("<h3 style='font-size:22px; font-weight:700; color:#F59E0B;'>🟡 ระดับสีเหลือง</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:#424245; font-size:15px; margin-bottom:15px; font-weight:500;'>ความเร่งด่วนปานกลาง แนะนำให้สังเกตอาการอย่างใกล้ชิด หรือปรึกษาสัตวแพทย์ทางไกล</p>", unsafe_allow_html=True)
            st.button("🎥 เข้าห้องสนทนากับแพทย์ (รอคิว 12 นาที)", type="primary")
            
        st.markdown("<h3 style='font-size:20px; font-weight:700; margin-top:20px;'>บริการเพิ่มเติม</h3>", unsafe_allow_html=True)
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("<p style='font-weight:600; font-size:14px; margin-bottom:2px;'>ปรึกษารายครั้ง</p>", unsafe_allow_html=True)
                st.button("ชำระ 350฿")
            with col2:
                st.markdown("<p style='font-weight:600; font-size:14px; margin-bottom:2px;'>สมัคร Premium</p>", unsafe_allow_html=True)
                st.button("รายเดือน 299฿", type="primary")

        st.write("<br>", unsafe_allow_html=True)
        if st.button("⬅️ กลับหน้าหลัก"):
            navigate('home')
            st.rerun()

# ==========================================
# WORKSPACE 2: B2B Portal (Veterinary)
# ==========================================
elif selected_workspace == '🩺 B2B (คลินิก)':
    st.markdown("<div class='apple-hero'>Vet Portal</div>", unsafe_allow_html=True)
    st.markdown("<div class='apple-subhero'>พื้นที่ปฏิบัติงานสัตวแพทย์พันธมิตร</div>", unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("<h3 style='font-size:20px; font-weight:700;'>ข้อมูลผู้ป่วย (AI Summary)</h3>", unsafe_allow_html=True)
        st.info("สุนัข สายพันธุ์โกลเด้น รีทรีฟเวอร์ (อายุ 5 ปี) - เสี่ยงภาวะ Gastritis")
        
        st.markdown("<p style='font-size:14px; font-weight:600; margin-bottom:4px;'>ยืนยันผลการวินิจฉัย</p>", unsafe_allow_html=True)
        vet_choice = st.selectbox("ยืนยันผลการวินิจฉัย", ["Gastritis", "Foreign Body Obstruction", "Parvovirus"], label_visibility="collapsed")
        
        st.write("")
        if st.button("อนุมัติและบันทึกข้อมูล (Sign-Off)", type="primary"):
            st.success("บันทึกข้อมูล Medical-grade สำเร็จ")

# ==========================================
# WORKSPACE 3: Backend
# ==========================================
elif selected_workspace == '🌐 Backend':
    st.markdown("<div class='apple-hero'>Infrastructure</div>", unsafe_allow_html=True)
    st.markdown("<div class='apple-subhero'>สถาปัตยกรรมการเชื่อมต่อ<br>API & Hardware</div>", unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("<h3 style='font-size:20px; font-weight:700;'>Insurance API Gateway</h3>", unsafe_allow_html=True)
        api_table = pd.DataFrame({'พันธมิตรประกันภัย': ['AIA Pet Protect', 'BKI'], 'สถานะ': ['Connected', 'Testing']})
        st.table(api_table)
