import streamlit as st
import pandas as pd
import numpy as np

# --- 1. System Configuration & Clean Apple UI Architecture ---
st.set_page_config(page_title="PetSOS Ecosystem", page_icon="🐾", layout="centered")

# Advanced CSS Injection (ย้ายเมนูมาไว้ด้านบน + สไตล์พรีเมียมตัวเต็ม)
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&display=swap');
        
        html, body, .stApp, .stMarkdown, h1, h2, h3, p, label {
            font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Prompt", sans-serif !important;
            color: #1D1D1F;
        }
        
        .main { background-color: #F5F5F7 !important; }
        #MainMenu, footer, header { visibility: hidden; }

        /* Premium Apple Heading Style */
        .apple-hero-title {
            font-size: 42px !important;
            font-weight: 700 !important;
            letter-spacing: -1px !important;
            text-align: center;
            margin-bottom: 5px;
            color: #1D1D1F;
        }
        
        .apple-sub-title {
            font-size: 18px !important;
            font-weight: 400 !important;
            color: #86868B !important;
            text-align: center;
            margin-bottom: 25px;
        }

        .apple-section-title {
            font-size: 22px !important;
            font-weight: 600 !important;
            letter-spacing: -0.5px !important;
            margin-bottom: 15px;
        }

        /* --- 📱 โครงสร้างแผงควบคุมด้านบนสไตล์ Apple Segmented Control --- */
        div[data-testid="stRadio"] {
            background: #E8E8ED !important;
            padding: 6px !important;
            border-radius: 16px !important;
            margin-bottom: 30px !important;
        }
        div[data-testid="stRadio"] > label {
            display: none !important; /* ซ่อนหัวข้อตัวเลือกเพื่อความคลีน */
        }
        div[data-testid="stRadio"] > div {
            flex-direction: row !important;
            justify-content: space-around !important;
            gap: 10px !important;
        }
        div[data-testid="stRadio"] label p {
            font-weight: 500 !important;
            font-size: 14px !important;
            color: #1D1D1F !important;
        }

        /* Apple Cards */
        div[data-testid="stAlert"], div[data-testid="stMetric"] {
            background: rgba(255, 255, 255, 0.9) !important;
            backdrop-filter: blur(20px) !important;
            border-radius: 20px !important;
            border: 1px solid rgba(255, 255, 255, 0.5) !important;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.02) !important;
        }

        /* File Uploader บล็อกแก้บั๊ก */
        div[data-testid="stFileUploader"] section {
            background-color: #FFFFFF !important;
            border: 1px dashed #D2D2D7 !important;
            border-radius: 16px !important;
        }
        div[data-testid="stFileUploader"] button {
            border-radius: 10px !important;
            background-color: #F5F5F7 !important;
            color: #007AFF !important;
            border: none !important;
        }

        /* ปุ่มกดมาตรฐาน */
        .stButton > button {
            border-radius: 14px !important;
            font-weight: 500 !important;
            font-size: 15px !important;
            padding: 12px 24px !important;
            border: 1px solid #E8E8ED !important;
            background-color: #FFFFFF !important;
            color: #007AFF !important;
            transition: all 0.2s ease !important;
            width: 100% !important;
        }
        .stButton > button:hover { background-color: #F5F5F7 !important; }
        button[kind="primary"] { background-color: #007AFF !important; color: #FFFFFF !important; border: none !important; }
        button[kind="primary"]:hover { background-color: #0062CC !important; }

        /* SOS Button */
        .sos-container button {
            background: linear-gradient(135deg, #FF3B30 0%, #FF453A 100%) !important;
            color: white !important;
            border: none !important;
            font-size: 16px !important;
            font-weight: 600 !important;
            border-radius: 14px !important;
            box-shadow: 0 4px 15px rgba(255, 59, 48, 0.2) !important;
        }
        .sos-container button:hover { background: #E03126 !important; }
    </style>
""", unsafe_allow_html=True)

# --- 2. Session State Initialize ---
if 'page' not in st.session_state: st.session_state.page = 'b2c_home'
if 'triage_result' not in st.session_state: st.session_state.triage_result = None

# --- 3. Main Brand Header ---
st.markdown("<h1 class='apple-hero-title'>PetSOS</h1>", unsafe_allow_html=True)
st.markdown("<p class='apple-sub-title'>Platform Ecosystem Demonstration</p>", unsafe_allow_html=True)

# --- 4. Investor Top Navigation Bar (เห็นเด่นชัด 100% ด้านบนสุด) ---
st.markdown("<p style='font-weight:700; color:#86868B; font-size:11px; letter-spacing:1px; text-align:center; margin-bottom:5px;'>INVESTOR PLATFORM CONTROL</p>", unsafe_allow_html=True)
user_role = st.radio(
    "ตัวเลือกมุมมองระบบ:",
    ["📱 ฝั่งผู้ใช้ (B2C App)", "🩺 ฝั่งสัตวแพทย์ (B2B Portal)", "🌐 หลังบ้าน (Phases 2-3)"],
    horizontal=True
)
st.write("<br>", unsafe_allow_html=True)

# ==========================================
# 1. ฝั่งผู้ใช้งานทั่วไป (Pet Parents - B2C App)
# ==========================================
if user_role == "📱 ฝั่งผู้ใช้ (B2C App)":
    
    st.markdown("<p style='font-weight:600; font-size:14px; color:#86868B; margin-bottom:5px;'>[Feature 1] One-Tap SOS</p>", unsafe_allow_html=True)
    st.markdown("<div class='sos-container'>", unsafe_allow_html=True)
    if st.button("🔴 ONE-TAP SOS ขอความช่วยเหลือด่วน", use_container_width=True):
        st.session_state.page = 'code_red_er'
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)

    if st.session_state.page == 'b2c_home':
        st.markdown("<p class='apple-section-title'>[Feature 2] AI Triage Engine</p>", unsafe_allow_html=True)
        
        species = st.selectbox("ชนิดสัตว์เลี้ยงของคุณ", ["สุนัข", "แมว", "สัตว์แปลก (Exotic)"])
        user_input = st.text_input("ระบุอาการของสัตว์เลี้ยงอย่างกระชับ:", placeholder="เช่น สุนัขมีอาการชัก หรือ ซึมไม่กินอาหาร")
        uploaded_file = st.file_uploader("📸 แนบรูปภาพหรือวิดีโออาการสั้น (Optional)", type=['png','jpg','mp4'])
        
        st.write("<br>", unsafe_allow_html=True)
        if st.button("ส่งข้อมูลให้ AI ประเมินผล ➡️", type="primary", use_container_width=True):
            if any(word in user_input for word in ["ชัก", "หมดสติ", "ไม่หายใจ", "หยุดหายใจ"]):
                st.session_state.page = 'code_red_er'
                st.rerun()
            else:
                st.session_state.triage_result = user_input
                st.session_state.page = 'triage_output'
                st.rerun()
                
        st.write("<br><br>", unsafe_allow_html=True)
        st.markdown("<p class='apple-section-title'>[Feature 5] Health Timeline & Reminders</p>", unsafe_allow_html=True)
        
        mock_timeline = pd.DataFrame({
            'กำหนดการ': ['ฉีดวัคซีนรวมประจำปี', 'หยดยาป้องกันเห็บหมัด', 'ตรวจสุขภาพไต (สุนัขสูงวัย)'],
            'การตอบสนองระบบ': ['⚠️ เลยกำหนดการ', '🔔 ถึงกำหนดสัปดาห์นี้', '📅 วางแผนในอีก 3 เดือน']
        })
        st.table(mock_timeline)

    elif st.session_state.page == 'code_red_er':
        st.error("🚨 **ระบบตรวจพบสภาวะวิกฤตสูงสุด (Code Red)**\n\nเปิดระบบนำทางข้ามขั้นตอน AI ไปยังโรงพยาบาลที่ใกล้ที่สุดทันทีเพื่อความปลอดภัยสูงสุดและลดภาระทางกฎหมาย")
        st.markdown("<br><p class='apple-section-title'>📍 [Feature 3] โรงพยาบาลสัตว์ 24 ชม. ที่ใกล้ที่สุด</p>", unsafe_allow_html=True)
        
        map_data = pd.DataFrame({'lat': [13.7367, 13.7456], 'lon': [100.5331, 100.5210]})
        st.map(map_data)
        
        st.write("<br>", unsafe_allow_html=True)
        st.button("📞 โทรด่วน: โรงพยาบาลสัตว์จุฬาฯ (02-XXX-XXXX)", type="primary", use_container_width=True)
        if st.button("⬅️ กลับหน้าหลัก", use_container_width=True):
            st.session_state.page = 'b2c_home'
            st.rerun()

    elif st.session_state.page == 'triage_output':
        st.markdown("<p class='apple-section-title'>ผลการวิเคราะห์ระบบดิจิทัล</p>", unsafe_allow_html=True)
        st.warning("🟡 **ระดับสีเหลือง (Observe):** ความเร่งด่วนปานกลาง\n\nสามารถสังเกตอาการอย่างใกล้ชิด หรือรับคำปรึกษาจากสัตวแพทย์ผ่านระบบทางไกลเพื่อประเมินสถานการณ์")
        
        st.write("<br>", unsafe_allow_html=True)
        st.markdown("<p class='apple-section-title'>💬 [Feature 4] Telemedicine Gateway</p>", unsafe_allow_html=True)
        st.info("⏳ **ระบบนับเวลาถอยหลังระหว่างรอคิว:** สัตวแพทย์พร้อมให้บริการในอีก **12:45 นาที**")
        
        if st.button("🎥 เข้าสู่ห้องสนทนาและ Video Call กับแพทย์", type="primary", use_container_width=True):
            st.success("🤖 เชื่อมต่อระบบการแพทย์ทางไกลเสร็จสมบูรณ์ (Mockup Live Active)")
            
        st.write("<br><br>", unsafe_allow_html=True)
        st.markdown("<p class='apple-section-title'>💳 [Feature 6] Payment & Subscription Manager</p>", unsafe_allow_html=True)
        
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            st.write("**Pay-Per-Use**")
            st.button("จ่ายค่าปรึกษา 350 บาท", use_container_width=True)
        with col_p2:
            st.write("**PetSOS Premium**")
            st.button("สมัครสมาชิก 299.-/ด.", type="primary", use_container_width=True)
            
        st.write("<br>", unsafe_allow_html=True)
        if st.button("⬅️ กลับหน้าหลัก", use_container_width=True):
            st.session_state.page = 'b2c_home'
            st.rerun()

# ==========================================
# 2. ฝั่งสัตวแพทย์และคลินิกพันธมิตร (B2B Portal)
# ==========================================
elif user_role == "🩺 ฝั่งสัตวแพทย์ (B2B Portal)":
    st.markdown("<p class='apple-section-title'>📊 [Feature 1] Vet Dashboard & AI Executive Summary</p>", unsafe_allow_html=True)
    st.info("🩺 **Incoming Case:** สุนัข สายพันธุ์โกลเด้น รีทรีฟเวอร์ (อายุ 5 ปี)")
    
    st.markdown("""
    <div style='background-color:#FFFFFF; padding:20px; border-radius:16px; border:1px solid #E8E8ED; margin-bottom:20px;'>
        <p style='font-weight:600; margin-bottom:5px; color:#1D1D1F;'>AI Executive Summary (ประวัติซักอาการโดยละเอียดโดย AI):</p>
        <ul style='color:#424245; font-size:14px; padding-left:20px;'>
            <li>ผู้ป่วยแจ้งว่าสัตว์เลี้ยงมีอาการอาเจียนเป็นฟองสีขาว 3 ครั้งในช่วง 6 ชั่วโมงที่ผ่านมา</li>
            <li>ดัชนีพฤติกรรมลดลง 40% และปฏิเสธการกินน้ำลายล่าสุด</li>
            <li><b>Differential Diagnosis (ข้อเสนอแนะ):</b> มีโอกาสเกิดภาวะ Gastritis ควรรีเช็กสิ่งแปลกปลอมในกระเพาะอาหาร (Foreign Body)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p class='apple-section-title'>🏷️ [Feature 2] Verified Data Labeling</p>", unsafe_allow_html=True)
    vet_diag = st.selectbox("สัตวแพทย์ตรวจสอบและยืนยันรหัสโรคขั้นสุดท้าย:", ["Gastritis (โรคกระเพาะอาหารอักเสบ)", "Foreign Body Obstruction (สิ่งแปลกปลอมอุดตัน)", "Parvovirus (ลำไส้อักเสบติดต่อ)"])
    if st.button("💾 บันทึกและยืนยันผลการวินิจฉัย (Verify Sign-Off)", type="primary", use_container_width=True):
        st.success(f"โครงสร้างข้อมูลโรค {vet_diag} ถูกเข้ารหัสและจัดเก็บในระบบ Secured Database เรียบร้อย")

    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown("<p class='apple-section-title'>🔗 [Feature 3] Referral Tracking & Commission</p>", unsafe_allow_html=True)
    
    col_v1, col_v2 = st.columns(2)
    with col_v1: st.metric(label="ยอดผู้สมัครใช้งานผ่าน QR คลินิกนี้", value="142 ราย")
    with col_v2: st.metric(label="ค่าคอมมิชชันสะสมประจำเดือน", value="4,260 THB", delta="+15% MoM")
        
    st.button("📷 ดาวน์โหลดไฟล์ QR Code ประจำสถานพยาบาล", use_container_width=True)

# ==========================================
# 3. ฝั่งระบบหลังบ้านและการเชื่อมต่อในอนาคต (Backend)
# ==========================================
elif user_role == "🌐 หลังบ้าน (Phases 2-3)":
    st.markdown("<p class='apple-section-title'>🛡️ [Feature 1] Insurance API Gateway (Phase 2)</p>", unsafe_allow_html=True)
    
    insurance_mock = pd.DataFrame({
        'Partner ประกันภัย': ['🦺 AIA Pet Protect', '🛡️ Bangkok Insurance (BKI)', '🐾 Tip Pet Care'],
        'สถานะการต่อท่อ API': ['🟢 CONNECTED (Active)', '🟡 READY TO TEST', '⚪ IN DISCUSSION'],
        'ส่วนลดเบี้ยประกันให้ลูกค้า': ['10% Discount', '15% Discount', 'TBD']
    })
    st.dataframe(insurance_mock, use_container_width=True)
    
    st.write("<br><br>", unsafe_allow_html=True)
    st.markdown("<p class='apple-section-title'>⌚ [Feature 2] Hardware Integration - Smart Collar (Phase 3)</p>", unsafe_allow_html=True)
    
    col_h1, col_h2, col_h3 = st.columns(3)
    with col_h1: st.metric(label="💓 ชีพจรเฉลี่ย (Heart Rate)", value="94 bpm", delta="สภาวะปกติ")
    with col_h2: st.metric(label="🌡️ อุณหภูมิร่างกาย (Body Temp)", value="38.6 °C", delta="สภาวะปกติ")
    with col_h3: st.metric(label="🐕 ดัชนีกิจกรรมทางกาย", value="-5%", delta="ซึมลงเล็กน้อย", delta_color="inverse")
        
    st.progress(0.85, text="เสถียรภาพสัญญาณการซิงก์ข้อมูลอุปกรณ์ฮาร์ดแวร์จำลอง (API Sync Rate): 85%")
