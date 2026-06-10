import streamlit as st
import pandas as pd
import numpy as np
import time

# --- 1. System Configuration & Apple Style ---
st.set_page_config(page_title="PetSOS Ecosystem", page_icon="🐾", layout="centered")

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;600&display=swap');
        html, body, [class*="css"], .stMarkdown {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Prompt", sans-serif !important;
        }
        .stButton > button {
            border-radius: 14px !important;
            font-weight: 600 !important;
            transition: all 0.2s ease-in-out !important;
        }
        button[kind="primary"] { background-color: #007AFF !important; color: white !important; }
        .sos-button > button {
            background-color: #FF3B30 !important;
            color: white !important;
            font-size: 24px !important;
            padding: 20px !important;
            border-radius: 20px !important;
        }
        div[data-testid="stAlert"] { border-radius: 16px !important; }
    </style>
""", unsafe_allow_html=True)

# --- 2. Session State Initialize ---
if 'page' not in st.session_state: st.session_state.page = 'b2c_home'
if 'triage_result' not in st.session_state: st.session_state.triage_result = None

# --- 3. Strategic Workspace Switcher (Sidebar for Investors) ---
st.sidebar.markdown("### 🖥️ Investor Control Panel")
user_role = st.sidebar.radio("สลับมุมมองระบบเพื่อตรวจงาน:", [
    "📱 ฝั่งผู้ใช้ทั่วไป (B2C Pet Parents)", 
    "🩺 ฝั่งสัตวแพทย์ (B2B Portal)", 
    "🌐 หลังบ้าน & Ecosystem (Phases 2-3)"
])

# ==========================================
# 1. ฝั่งผู้ใช้งานทั่วไป (Pet Parents - B2C App)
# ==========================================
if user_role == "📱 ฝั่งผู้ใช้ทั่วไป (B2C Pet Parents)":
    
    # --- One-Tap SOS Feature ---
    st.markdown("<h1 style='text-align: center;'>🐾 PetSOS Mobile</h1>", unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("### 🚨 [Feature 1] One-Tap SOS")
    st.caption("ปุ่มฉุกเฉินขนาดใหญ่สำหรับเคสวิกฤตสูงสุด (Code Red)")
    
    col_sos, _ = st.columns([2, 1])
    with col_sos:
        if st.button("🔴 ONE-TAP SOS (ฉุกเฉินวิกฤต)", use_container_width=True, type="secondary"):
            st.session_state.page = 'code_red_er'
            st.rerun()
            
    st.write("---")

    # Navigation Logic for B2C
    if st.session_state.page == 'b2c_home':
        st.markdown("### 🩺 [Feature 2] AI Triage Engine")
        st.write("ระบบวิเคราะห์อาการเบื้องต้นด้วย AI")
        
        species = st.selectbox("ชนิดสัตว์เลี้ยง", ["สุนัข", "แมว", "สัตว์แปลก (Exotic)"])
        user_input = st.text_input("พิมพ์อาการ หรืออธิบายสิ่งที่พบ:", placeholder="เช่น หมาซึม ไม่กินข้าวอ้วกเป็นฟอง")
        uploaded_file = st.file_uploader("📸 อัปโหลดรูปภาพอาการหรือคลิปวิดีโอสั้น (Optional)", type=['png','jpg','mp4'])
        
        if st.button("ส่งให้ AI ประเมินผล ➡️", type="primary", use_container_width=True):
            # Zero-Liability Emergency Routing Rule
            if "ชัก" in user_input or "หมดสติ" in user_input or "ไม่หายใจ" in user_input:
                st.session_state.page = 'code_red_er'
                st.rerun()
            else:
                st.session_state.triage_result = user_input
                st.session_state.page = 'triage_output'
                st.rerun()
                
        # --- [Feature 5] AI Health Timeline & Reminders ---
        st.write("---")
        st.markdown("### 📅 [Feature 5] AI Health Timeline & Reminders (Premium Driver)")
        st.info("💡 สมาชิกแบบ Premium จะได้รับการแจ้งเตือนอัตโนมัติผ่าน Line/Push Notification")
        
        mock_timeline = pd.DataFrame({
            'กำหนดการ': ['ฉีดวัคซีนรวมประจำปี', 'หยดยาป้องกันเห็บหมัด', 'ตรวจสุขภาพไต (สุนัขสูงวัย)'],
            'สถานะ': ['🔴 เลยกำหนด (วิกฤต)', '🟡 ถึงกำหนดสัปดาห์นี้', '🟢 วางแผนในอีก 3 เดือน']
        })
        st.table(mock_timeline)

    # --- [Feature 3] Zero-Liability Emergency Routing (Code Red Page) ---
    elif st.session_state.page == 'code_red_er':
        st.error("🚨 ระบบตรวจพบสภาวะวิกฤตสูงสุด (Code Red) ! ดำเนินการข้ามระบบ AI อัตโนมัติ เพื่อความปลอดภัยทางกฎหมาย")
        st.markdown("### 📍 [Feature 3] แผนที่โรงพยาบาลสัตว์ 24 ชม. ที่ใกล้ที่สุด")
        
        # Mock Map Center in Bangkok
        map_data = pd.DataFrame({
            'lat': [13.7367, 13.7456],
            'lon': [100.5331, 100.5210]
        })
        st.map(map_data)
        
        st.button("📞 โทรด่วนสปีกเกอร์โฟน: โรงพยาบาลสัตว์จุฬาฯ (02-XXX-XXXX)", type="primary", use_container_width=True)
        if st.button("⬅️ กลับหน้าหลัก", use_container_width=True):
            st.session_state.page = 'b2c_home'
            st.rerun()

    # --- [Feature 4 & 6] Triage Result, Telemed Gateway, and Payment ---
    elif st.session_state.page == 'triage_output':
        st.markdown("### ผลการวิเคราะห์จาก AI")
        st.warning("🟡 **ระดับสีเหลือง (Observe):** ความเร่งด่วนปานกลาง-ต่ำ")
        st.write(f"อาการที่วิเคราะห์: *{st.session_state.triage_result if st.session_state.triage_result else 'ซึม ไม่กินอาหาร'}*")
        
        st.write("---")
        st.markdown("### 💬 [Feature 4] Telemedicine Gateway")
        st.write("เชื่อมต่อสัตวแพทย์ออนไลน์เพื่อความสบายใจ")
        
        # Countdown simulation
        st.warning("⏳ สัตวแพทย์กำลังสแตนด์บายในคิว: กำลังรอสายประมาณ 12:45 นาที")
        
        if st.button("🎥 เข้าห้อง Video Call กับหมอ (จำลอง)", type="primary", use_container_width=True):
            st.success("🤖 ระบบเชื่อมต่อห้องสนทนาการแพทย์เสร็จสมบูรณ์ (Mockup Call Activated)")
            
        st.write("---")
        st.markdown("### 💳 [Feature 6] Payment & Subscription Manager")
        
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            st.write("**ระบบจ่ายรายครั้ง (Transactional)**")
            st.button("🪙 จ่ายค่า Telemed 350 THB/ครั้ง", use_container_width=True)
        with col_p2:
            st.write("**ระบบสมาชิก (Premium Subscription)**")
            st.button("✨ อัปเกรดพรีเมียม 299 THB/เดือน", type="primary", use_container_width=True)
            
        if st.button("⬅️ กลับหน้าหลัก", use_container_width=True):
            st.session_state.page = 'b2c_home'
            st.rerun()

# ==========================================
# 2. ฝั่งสัตวแพทย์และคลินิกพันธมิตร (B2B Portal)
# ==========================================
elif user_role == "🩺 ฝั่งสัตวแพทย์ (B2B Portal)":
    st.markdown("<h1>🩺 PetSOS Vet Portal</h1>", unsafe_allow_html=True)
    st.caption("ระบบบริหารจัดการเคสสำหรับสัตวแพทย์และคลินิกพันธมิตรเพื่อป้อนข้อมูล Medical-Grade Data")
    
    st.write("---")
    st.markdown("### 📊 [Feature 1] Vet Dashboard & AI Executive Summary")
    st.info("🩺 **เคสที่กำลังเข้าสู่ระบบ:** สุนัข พันธุ์โกลเด้น รีทรีฟเวอร์ (อายุ 5 ปี)")
    
    st.markdown("""
    > **AI Executive Summary (สรุปประวัติโดย AI):**
    > * ผู้ป่วยแจ้งว่าสัตว์เลี้ยงมีอาการอาเจียนเป็นฟองสีขาว 3 ครั้งในช่วง 6 ชั่วโมงที่ผ่านมา พฤติกรรมซึมลง 40% และไม่ยอมกินน้ำลายล่าสุด 
    > * **ข้อเสนอแนะสำหรับการวินิจฉัย:** คาดว่ามีภาวะ Gastritis เบื้องต้น ควรรีเช็กประวัติสิ่งแปลกปลอม (Foreign Body)
    """)
    
    st.write("---")
    st.markdown("### 🏷️ [Feature 2] Verified Data Labeling")
    st.write("บันทึกผลการตรวจเพื่อแปรสภาพข้อมูลเป็นสินทรัพย์ของบริษัท (Medical-Grade Data สำหรับขายบริษัทประกัน)")
    
    vet_diag = st.selectbox("สัตวแพทย์ยืนยันผลการวินิจฉัยขั้นสุดท้าย:", ["Gastritis (โรคกระเพาะอาหารอักเสบ)", "Foreign Body Obstruction (สิ่งแปลกปลอมอุดตัน)", "Parvovirus (ลำไส้อักเสบติดต่อ)"])
    if st.button("💾 บันทึกและยืนยันผลทางการแพทย์ (Verify Sign-Off)", type="primary"):
        st.success(f"บันทึกรหัสโรค {vet_diag} เข้าสู่ Secured Database เรียบร้อย ข้อมูลพร้อมส่งต่อให้พาร์ตเนอร์ประกันภัย")

    st.write("---")
    st.markdown("### 🔗 [Feature 3] Referral Tracking & Commission")
    st.write("ระบบติดตามยอดดาวน์โหลดของแต่ละคลินิกพันธมิตรเพื่อคำนวณส่วนแบ่ง")
    
    # Simple analytics layout
    col_v1, col_v2 = st.columns(2)
    with col_v1:
        st.metric(label="ยอดผู้สมัครผ่าน QR คลินิกนี้", value="142 ราย")
    with col_v2:
        st.metric(label="ค่าคอมมิชชันสะสมเดือนนี้", value="4,260 THB", delta="+15% จากเดือนที่แล้ว")
        
    st.button("📷 เจนเนอเรต QR Code ประจำคลินิก")

# ==========================================
# 3. ฝั่งระบบหลังบ้านและการเชื่อมต่อในอนาคต (Backend)
# ==========================================
elif user_role == "🌐 หลังบ้าน & Ecosystem (Phases 2-3)":
    st.markdown("<h1>🌐 Tech Stack & Ecosystem Future Architecture</h1>", unsafe_allow_html=True)
    st.caption("พิมพ์เขียวระบบหลังบ้านและการเชื่อมต่อข้อมูลเชิงกลยุทธ์เพื่อเข้าสู่เป้าหมายสร้างรายได้ระยะยาว")
    
    st.write("---")
    st.markdown("### 🛡️ [Feature 1] Insurance API Gateway (Phase 2)")
    st.write("ระบบดึงข้อมูลสุขภาพที่ผ่านการแพทย์ยืนยัน (Verified Data) เพื่อลดหย่อนเบี้ยประกันให้กับลูกค้า")
    
    insurance_mock = pd.DataFrame({
        'Partner ประกัน': ['🦺 AIA Pet Protect', '🛡️ Bangkok Insurance (BKI)', '🐾 Tip Pet Care'],
        'API Status': ['CONNECTED (Active)', 'READY TO TEST', 'DISCUSSING CONTRACT'],
        'อัตราการลดเบี้ยประกันเฉลี่ย': ['10%', '15%', 'TBD']
    })
    st.dataframe(insurance_mock, use_container_width=True)
    
    st.write("---")
    st.markdown("### ⌚ [Feature 2] Hardware Integration - Smart Collar (Phase 3)")
    st.write("โมดูลดึงข้อมูลแบบ Real-time จากปลอกคออัจฉริยะผ่านเทคโนโลยี Bluetooth / API")
    
    col_h1, col_h2, col_h3 = st.columns(3)
    with col_h1:
        st.metric(label="💓 ชีพจรเฉลี่ย (Heart Rate)", value="94 bpm", delta="ปกติ")
    with col_h2:
        st.metric(label="🌡️ อุณหภูมิร่างกาย (Body Temp)", value="38.6 °C", delta="ปกติ")
    with col_h3:
        st.metric(label="🐕 พฤติกรรมการนอน", value="-5%", delta="ซึมลงเล็กน้อย", delta_color="inverse")
        
    st.progress(0.85, text="ความเสถียรของสัญญาณเชื่อมต่อฮาร์ดแวร์จำลอง (API Sync Rate): 85%")
