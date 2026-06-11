import streamlit as st
import pandas as pd

# --- 1. System Configuration ---
st.set_page_config(page_title="PetSOS", page_icon="🐾", layout="centered")

# --- 2. Precision CSS Injection (Apple Store Clone & Bug Fixes) ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@400;500;600;700&display=swap');
        
        /* Typography Standard */
        html, body, .stApp, .stMarkdown, p, span, h1, h2, h3, h4, label {
            font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Prompt", sans-serif !important;
            color: #1D1D1F;
        }
        
        .stApp { background-color: #F5F5F7 !important; }
        header, footer, #MainMenu { visibility: hidden !important; }

        /* --- Apple Store Top Navigation --- */
        .apple-nav-title {
            font-size: 42px;
            font-weight: 700;
            letter-spacing: -0.02em;
            text-align: center;
            margin-top: 10px;
            margin-bottom: 5px;
        }
        .apple-nav-subtitle {
            font-size: 18px;
            font-weight: 500;
            color: #86868B;
            text-align: center;
            margin-bottom: 20px;
        }
        
        /* Styling the Radio button to look like a clean Apple Menu */
        div.row-widget.stRadio > div {
            background-color: #E8E8ED;
            padding: 6px;
            border-radius: 14px;
            display: flex;
            justify-content: center;
            gap: 10px;
        }
        
        /* --- Card Architecture --- */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #FFFFFF !important;
            border-radius: 20px !important;
            border: none !important;
            box-shadow: 0 4px 15px rgba(0,0,0,0.03) !important;
            padding: 10px !important;
            margin-bottom: 15px;
        }

        /* --- Inputs & Text Fields --- */
        div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {
            border-radius: 12px !important;
            border: 1px solid #D2D2D7 !important;
            background-color: #F5F5F7 !important;
        }
        
        /* --- 🩹 SURGICAL FIX: File Uploader --- */
        /* เราจะปรับแค่กรอบด้านนอก และปล่อยให้ปุ่มด้านในทำงานตาม Native ของ Streamlit เพื่อกันบั๊กซ้อนทับ */
        div[data-testid="stFileUploader"] section {
            border: 1px dashed #D2D2D7 !important;
            background-color: #FAFAFA !important;
            border-radius: 14px !important;
            padding: 15px !important;
        }
        /* ลบคำสั่งที่ไปบังคับปุ่มด้านในของ File Uploader ทิ้งทั้งหมด */

        /* --- Global Button Styling --- */
        /* เจาะจงเฉพาะปุ่มมาตรฐาน (stButton) เพื่อไม่ให้กระทบปุ่มอัปโหลดไฟล์ */
        div[data-testid="stButton"] > button {
            border-radius: 14px !important;
            font-weight: 500 !important;
            font-size: 15px !important;
            padding: 12px 24px !important;
            background-color: #F5F5F7 !important;
            color: #007AFF !important;
            border: none !important;
            width: 100% !important;
            transition: transform 0.1s ease;
        }
        div[data-testid="stButton"] > button:hover { 
            background-color: #E8E8ED !important; 
            transform: scale(0.98);
        }
        
        /* Primary Button Accent */
        div[data-testid="stButton"] > button[kind="primary"] {
            background-color: #007AFF !important;
            color: white !important;
        }
        div[data-testid="stButton"] > button[kind="primary"]:hover { 
            background-color: #0062CC !important; 
        }
    </style>
""", unsafe_allow_html=True)

# --- 3. State Management (Routing & Navigation) ---
if 'workspace' not in st.session_state:
    st.session_state.workspace = '📱 ฝั่งผู้ใช้ (B2C)'
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def navigate(page_name):
    st.session_state.page = page_name

# --- 4. Top Navigation Bar (Apple Store Style) ---
st.markdown("<div class='apple-nav-title'>PetSOS</div>", unsafe_allow_html=True)
st.markdown("<div class='apple-nav-subtitle'>ระบบนิเวศแพลตฟอร์มการแพทย์สำหรับสัตว์เลี้ยง</div>", unsafe_allow_html=True)

selected_workspace = st.radio(
    "เลือกหน้าต่างการประเมิน:",
    ['📱 ฝั่งผู้ใช้ (B2C)', '🩺 สัตวแพทย์ (B2B)', '🌐 หลังบ้าน (Backend)'],
    horizontal=True,
    label_visibility="collapsed"
)
st.write("<br>", unsafe_allow_html=True)

# ==========================================
# WORKSPACE 1: B2C App (Pet Parents)
# ==========================================
if selected_workspace == '📱 ฝั่งผู้ใช้ (B2C)':
    
    # ---------------- PAGE: HOME ----------------
    if st.session_state.page == 'home':
        st.markdown("<h3 style='font-size:24px; font-weight:700; text-align:center;'>บริการของเรา</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color:#86868B; text-align:center; margin-bottom:20px;'>เลือกความช่วยเหลือที่คุณต้องการในขณะนี้</p>", unsafe_allow_html=True)

        # Feature: Code Red
        with st.container(border=True):
            st.markdown("<h3 style='margin-bottom:0px; font-size:20px;'>🚨 กรณีฉุกเฉินวิกฤต</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:#86868B; font-size:14px; margin-bottom:15px;'>หากสัตว์เลี้ยงหมดสติ ชัก หรือหยุดหายใจ</p>", unsafe_allow_html=True)
            # Custom style injection specifically for SOS Button
            st.markdown("""<style>div:nth-child(1) > div > div > button { background-color: #FF3B30 !important; color: white !important; font-weight:600 !important;}</style>""", unsafe_allow_html=True)
            if st.button("🔴 ขอความช่วยเหลือด่วน (SOS)"):
                navigate('sos')
                st.rerun()

        # Feature: Triage Engine
        with st.container(border=True):
            st.markdown("<h3 style='margin-bottom:0px; font-size:20px;'>🩺 ประเมินอาการเบื้องต้น</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:#86868B; font-size:14px; margin-bottom:15px;'>ให้ AI ช่วยคัดกรองความเร่งด่วนทางการแพทย์</p>", unsafe_allow_html=True)
            
            st.markdown("<p style='font-size:13px; font-weight:600; margin-bottom:4px;'>ชนิดสัตว์เลี้ยง</p>", unsafe_allow_html=True)
            species = st.selectbox("ชนิดสัตว์เลี้ยง", ["สุนัข", "แมว", "สัตว์แปลก (Exotic)"], label_visibility="collapsed")
            
            st.markdown("<p style='font-size:13px; font-weight:600; margin-bottom:4px; margin-top:10px;'>อาการที่พบ</p>", unsafe_allow_html=True)
            user_input = st.text_input("อาการที่พบ", placeholder="เช่น ซึม อาเจียน หรือ ไม่กินอาหาร", label_visibility="collapsed")
            
            st.markdown("<p style='font-size:13px; font-weight:600; margin-bottom:4px; margin-top:10px;'>แนบรูปภาพ/วิดีโอ (ถ้ามี)</p>", unsafe_allow_html=True)
            st.file_uploader("แนบไฟล์", type=['png','jpg','mp4'], label_visibility="collapsed")
            
            st.write("")
            if st.button("ส่งข้อมูลให้ AI ประเมินผล ➡️", type="primary"):
                navigate('result')
                st.rerun()

    # ---------------- PAGE: SOS (Code Red) ----------------
    elif st.session_state.page == 'sos':
        st.markdown("<h2 style='font-size:32px; font-weight:700; color:#FF3B30; text-align:center;'>Code Red</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color:#86868B; text-align:center; margin-bottom:20px;'>ระบบนำทางฉุกเฉินไปยังโรงพยาบาลที่ใกล้ที่สุด</p>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("<h3 style='font-size:18px;'>📍 โรงพยาบาลสัตว์จุฬาลงกรณ์</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:#86868B; font-size:14px;'>ห่างจากตำแหน่งของคุณ 2.4 กม.</p>", unsafe_allow_html=True)
            
            map_data = pd.DataFrame({'lat': [13.7367], 'lon': [100.5331]})
            st.map(map_data)
            
            st.markdown("""<style>div[data-testid="stButton"] button { background-color: #FF3B30 !important; color: white !important; font-weight: bold !important; }</style>""", unsafe_allow_html=True)
            st.button("📞 โทรสายด่วนทันที")
            
        st.write("<br>", unsafe_allow_html=True)
        if st.button("⬅️ ย้อนกลับ"):
            navigate('home')
            st.rerun()

    # ---------------- PAGE: RESULT ----------------
    elif st.session_state.page == 'result':
        st.markdown("<h2 style='font-size:32px; font-weight:700; text-align:center;'>ผลการประเมิน</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color:#86868B; text-align:center; margin-bottom:20px;'>คำแนะนำทางการแพทย์โดย AI Triage</p>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("<h3 style='font-size:20px; color:#F59E0B;'>🟡 ระดับสีเหลือง (Observe)</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:#424245; font-size:15px; margin-bottom:15px;'>อาการพ้นขีดอันตรายเฉียบพลัน แนะนำให้สังเกตอาการ หรือปรึกษาสัตวแพทย์ทางไกล</p>", unsafe_allow_html=True)
            st.button("🎥 เข้าห้องสนทนากับแพทย์ (รอคิว 12 นาที)", type="primary")
            
        st.markdown("<h3 style='font-size:20px; font-weight:600; margin-top:20px;'>ตัวเลือกเพิ่มเติม</h3>", unsafe_allow_html=True)
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

# ==========================================
# WORKSPACE 2: B2B Portal (Veterinary)
# ==========================================
elif selected_workspace == '🩺 สัตวแพทย์ (B2B)':
    st.markdown("<h3 style='font-size:24px; font-weight:700; text-align:center;'>Vet Dashboard</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:#86868B; text-align:center; margin-bottom:20px;'>พื้นที่ปฏิบัติงานสัตวแพทย์</p>", unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("<h3 style='font-size:18px;'>ข้อมูลผู้ป่วย (AI Summary)</h3>", unsafe_allow_html=True)
        st.info("สุนัข สายพันธุ์โกลเด้น รีทรีฟเวอร์ (อายุ 5 ปี) - เสี่ยงภาวะ Gastritis")
        
        vet_choice = st.selectbox("ยืนยันผลการวินิจฉัยเพื่อบันทึก Medical Data", ["Gastritis", "Foreign Body Obstruction", "Parvovirus"])
        if st.button("อนุมัติรับรองข้อมูล (Sign-Off)", type="primary"):
            st.success("บันทึกข้อมูลสำเร็จ")

# ==========================================
# WORKSPACE 3: Backend
# ==========================================
elif selected_workspace == '🌐 หลังบ้าน (Backend)':
    st.markdown("<h3 style='font-size:24px; font-weight:700; text-align:center;'>Infrastructure</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:#86868B; text-align:center; margin-bottom:20px;'>การเชื่อมต่อ API และ Hardware</p>", unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("<h3 style='font-size:18px;'>Insurance API Gateway</h3>", unsafe_allow_html=True)
        api_table = pd.DataFrame({'พันธมิตรประกันภัย': ['AIA Pet Protect', 'BKI'], 'สถานะ': ['Connected', 'Testing']})
        st.table(api_table)
