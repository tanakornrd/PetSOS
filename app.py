import streamlit as st
import pandas as pd

# --- 1. System Configuration & Apple Web Aesthetic ---
st.set_page_config(page_title="PetSOS Platform", page_icon="🐾", layout="centered")

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&display=swap');
        
        /* Global Apple Typography & Color Grid */
        html, body, .stApp, .stMarkdown, p, label, select, input {
            font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Prompt", sans-serif !important;
            color: #1D1D1F !important;
        }
        
        .main { background-color: #F5F5F7 !important; }
        #MainMenu, footer, header { visibility: hidden; }

        /* Apple Product Page Typography */
        .apple-title {
            font-size: 40px !important;
            font-weight: 700 !important;
            letter-spacing: -1px !important;
            text-align: center;
            color: #1D1D1F !important;
            margin-top: 10px;
        }
        
        .apple-subtitle {
            font-size: 18px !important;
            font-weight: 400 !important;
            color: #86868B !important;
            text-align: center;
            margin-bottom: 30px;
        }

        .feature-tag {
            font-size: 11px !important;
            font-weight: 600 !important;
            color: #86868B !important;
            letter-spacing: 0.5px !important;
            text-transform: uppercase;
            margin-bottom: 4px;
        }

        .section-title {
            font-size: 22px !important;
            font-weight: 600 !important;
            letter-spacing: -0.5px !important;
            color: #1D1D1F !important;
            margin-bottom: 12px;
        }

        /* Segmented Control (Top Nav Tabs) */
        div[data-testid="stRadio"] {
            background: #E8E8ED !important;
            padding: 4px !important;
            border-radius: 12px !important;
            margin-bottom: 25px !important;
        }
        div[data-testid="stRadio"] > label { display: none !important; }
        div[data-testid="stRadio"] > div {
            flex-direction: row !important;
            justify-content: space-around !important;
        }
        div[data-testid="stRadio"] label p {
            font-weight: 500 !important;
            font-size: 13px !important;
            color: #1D1D1F !important;
        }

        /* Apple Premium Card Structure */
        .apple-card {
            background: #FFFFFF !important;
            border-radius: 18px !important;
            border: 1px solid #E8E8ED !important;
            padding: 24px !important;
            margin-bottom: 20px !important;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.01) !important;
        }

        /* Specialized Red Line Card for Code Red */
        .code-red-card {
            background: #FFFFFF !important;
            border-radius: 18px !important;
            border-left: 4px solid #FF3B30 !important;
            border-top: 1px solid #E8E8ED !important;
            border-right: 1px solid #E8E8ED !important;
            border-bottom: 1px solid #E8E8ED !important;
            padding: 24px !important;
            margin-bottom: 20px !important;
        }

        /* Native Look Forms & Inputs */
        div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {
            border-radius: 10px !important;
            border: 1px solid #D2D2D7 !important;
            background-color: #FFFFFF !important;
        }

        /* Button Refactoring */
        .stButton > button {
            border-radius: 10px !important;
            font-weight: 500 !important;
            font-size: 14px !important;
            padding: 10px 20px !important;
            border: 1px solid #D2D2D7 !important;
            background-color: #FFFFFF !important;
            color: #007AFF !important;
            transition: all 0.15s ease !important;
            width: 100% !important;
        }
        .stButton > button:hover { background-color: #F5F5F7 !important; }
        
        button[kind="primary"] {
            background-color: #007AFF !important;
            color: #FFFFFF !important;
            border: none !important;
        }
        button[kind="primary"]:hover { background-color: #0062CC !important; }

        /* SOS Custom Pill Button */
        .sos-btn button {
            background-color: #FF3B30 !important;
            color: #FFFFFF !important;
            border: none !important;
            font-size: 15px !important;
            font-weight: 600 !important;
            border-radius: 10px !important;
        }
        .sos-btn button:hover { background-color: #D7261E !important; }
        
        /* Metric Adjustments */
        div[data-testid="stMetricValue"] {
            font-size: 28px !important;
            font-weight: 600 !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- 2. Initialize Workflow State ---
if 'b2c_journey_state' not in st.session_state: 
    st.session_state.b2c_journey_state = 'Overview'

# --- 3. Platform Identity ---
st.markdown("<h1 class='apple-title'>PetSOS</h1>", unsafe_allow_html=True)
st.markdown("<p class='apple-subtitle'>Medical Decision Support & Ecosystem Platform</p>", unsafe_allow_html=True)

# --- 4. Investor Top Navigation Control Panel ---
st.markdown("<p style='font-weight:700; color:#86868B; font-size:10px; letter-spacing:1px; text-align:center; margin-bottom:6px;'>INVESTOR INTERFACE SELECTOR</p>", unsafe_allow_html=True)
user_role = st.radio(
    "Interface Selector",
    ["B2C App (Pet Parents)", "B2B Portal (Veterinary)", "Backend Infrastructure"],
    horizontal=True
)
st.write("<br>", unsafe_allow_html=True)


# ==========================================
# 1. ฝั่งผู้ใช้งานทั่วไป (B2C App)
# ==========================================
if user_role == "B2C App (Pet Parents)":
    
    # Investor Journey Simulation Bar
    st.markdown("<div style='background:#E8E8ED; padding:10px; border-radius:12px; margin-bottom:20px; text-align:center;'>", unsafe_allow_html=True)
    st.markdown("<span style='font-size:12px; font-weight:600; color:#666;'>ตัวเลือกจำลองสถานะแอปเพื่อตรวจงานเฟส B2C:</span>", unsafe_allow_html=True)
    col_s1, col_s2, col_s3 = st.columns(3)
    with col_s1:
        if st.button("หน้าแรก & ตรวจอาการ", type="secondary" if st.session_state.b2c_journey_state != 'Overview' else "primary"):
            st.session_state.b2c_journey_state = 'Overview'
            st.rerun()
    with col_s2:
        if st.button("เคสฉุกเฉิน (Code Red)", type="secondary" if st.session_state.b2c_journey_state != 'CodeRed' else "primary"):
            st.session_state.b2c_journey_state = 'CodeRed'
            st.rerun()
    with col_s3:
        if st.button("ผลวิเคราะห์ & Telemed", type="secondary" if st.session_state.b2c_journey_state != 'TriageOutput' else "primary"):
            st.session_state.b2c_journey_state = 'TriageOutput'
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    # --- STATE: OVERVIEW (Features 1, 2, 5) ---
    if st.session_state.b2c_journey_state == 'Overview':
        
        # Feature 1: One-Tap SOS
        st.markdown("<div class='apple-card'>", unsafe_allow_html=True)
        st.markdown("<p class='feature-tag'>Feature 1 • One-Tap SOS</p>", unsafe_allow_html=True)
        st.markdown("<p class='section-title'>ขอความช่วยเหลือฉุกเฉิน</p>", unsafe_allow_html=True)
        st.markdown("<p style='color:#666; font-size:14px; margin-bottom:15px;'>ระบบตัดวงจรเข้าสู่โหมดกู้ชีพทันทีเมื่อผู้ใช้งานอยู่ในสภาวะตื่นตระหนก</p>", unsafe_allow_html=True)
        st.markdown("<div class='sos-btn'>", unsafe_allow_html=True)
        if st.button("SOS Emergency Assistance", use_container_width=True):
            st.session_state.b2c_journey_state = 'CodeRed'
            st.rerun()
        st.markdown("</div></div>", unsafe_allow_html=True)
        
        # Feature 2: AI Triage Engine
        st.markdown("<div class='apple-card'>", unsafe_allow_html=True)
        st.markdown("<p class='feature-tag'>Feature 2 • AI Triage Engine</p>", unsafe_allow_html=True)
        st.markdown("<p class='section-title'>ระบบคัดกรองอาการดิจิทัล</p>", unsafe_allow_html=True)
        
        species = st.selectbox("ชนิดสัตว์เลี้ยง", ["สุนัข", "แมว", "สัตว์แปลก (Exotic)"])
        user_input = st.text_input("ระบุอาการพื้นฐานอย่างกระชับ", placeholder="เช่น ซึม อาเจียน หรือ ไม่กินอาหารมาราว 2 วัน")
        st.file_uploader("แนบหลักฐานรูปภาพหรือคลิปวิดีโอประกอบ (ถ้ามี)", type=['png','jpg','mp4'])
        
        st.write("<br>", unsafe_allow_html=True)
        if st.button("ส่งข้อมูลประเมินผล", type="primary", use_container_width=True):
            st.session_state.b2c_journey_state = 'TriageOutput'
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Feature 5: AI Health Timeline & Reminders
        st.markdown("<div class='apple-card'>", unsafe_allow_html=True)
        st.markdown("<p class='feature-tag'>Feature 5 • AI Health Timeline & Reminders</p>", unsafe_allow_html=True)
        st.markdown("<p class='section-title'>บันทึกสุขภาพและการแจ้งเตือน</p>", unsafe_allow_html=True)
        st.markdown("<p style='color:#86868B; font-size:14px; margin-bottom:15px;'>กลไกหลักในการขับเคลื่อนยอดผู้สมัครสมาชิกระดับพรีเมียม (Premium Subscription Retention)</p>", unsafe_allow_html=True)
        
        mock_timeline = pd.DataFrame({
            'โปรแกรมการดูแล': ['วัคซีนรวมประจำปี', 'หยดยาป้องกันเห็บหมัด', 'ตรวจประเมินค่าไตขั้นสูง'],
            'การแจ้งเตือนระบบ': ['เกินกำหนดเวลา', 'ถึงกำหนดสัปดาห์นี้', 'วางแผนในอีก 3 เดือน']
        })
        st.table(mock_timeline)
        st.markdown("</div>", unsafe_allow_html=True)

    # --- STATE: CODE RED (Feature 3) ---
    elif st.session_state.b2c_journey_state == 'CodeRed':
        st.markdown("<div class='code-red-card'>", unsafe_allow_html=True)
        st.markdown("<p class='feature-tag' style='color:#FF3B30;'>Feature 3 • Zero-Liability Emergency Routing</p>", unsafe_allow_html=True)
        st.markdown("<p class='section-title' style='color:#FF3B30;'>ระบบนำทางกรณีวิกฤตสูงสุด (Code Red)</p>", unsafe_allow_html=True)
        st.markdown("<p style='color:#1D1D1F; font-size:14px;'>อัลกอริทึมประเมินพบสภาวะเสี่ยงต่อชีวิต ระบบตัดหน้าจอข้ามขั้นตอน AI ทั้งหมดโดยอัตโนมัติ เพื่อเข้าสู่โหมดนำทางสถานพยาบาลที่ใกล้ที่สุดในทันที</p>", unsafe_allow_html=True)
        
        # Map simulation
        map_data = pd.DataFrame({'lat': [13.7367, 13.7456], 'lon': [100.5331, 100.5210]})
        st.map(map_data)
        
        st.write("<br>", unsafe_allow_html=True)
        st.button("โทรสายด่วนสถานพยาบาล 24 ชั่วโมง", type="primary", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # --- STATE: TRIAGE OUTPUT (Features 4, 6) ---
    elif st.session_state.b2c_journey_state == 'TriageOutput':
        
        st.markdown("<div class='apple-card'>", unsafe_allow_html=True)
        st.markdown("<p class='feature-tag'>Triage Result Output</p>", unsafe_allow_html=True)
        st.markdown("<p class='section-title'>ผลการประเมิน: ระดับสีเหลือง (Observe)</p>", unsafe_allow_html=True)
        st.markdown("<p style='color:#424245; font-size:14px;'>อาการพ้นขีดอันตรายฉุกเฉินเฉียบพลัน แนะนำให้สังเกตอาการอย่างใกล้ชิด หรือทำการนัดหมายแพทย์ผ่านระบบการแพทย์ทางไกล</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Feature 4: Telemedicine Gateway
        st.markdown("<div class='apple-card'>", unsafe_allow_html=True)
        st.markdown("<p class='feature-tag'>Feature 4 • Telemedicine Gateway</p>", unsafe_allow_html=True)
        st.markdown("<p class='section-title'>ระบบการแพทย์ทางไกล</p>", unsafe_allow_html=True)
        st.markdown("<div style='background:#F5F5F7; padding:12px; border-radius:8px; margin-bottom:15px; text-align:center; font-size:14px; font-weight:500; color:#FF9500;'>ระยะเวลารอสายโดยประมาณ: 12:45 นาที</div>", unsafe_allow_html=True)
        st.button("เข้าสู่ห้องสนทนาทางการแพทย์ (Video Call)", type="primary", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Feature 6: Payment & Subscription Manager
        st.markdown("<div class='apple-card'>", unsafe_allow_html=True)
        st.markdown("<p class='feature-tag'>Feature 6 • Payment & Subscription Manager</p>", unsafe_allow_html=True)
        st.markdown("<p class='section-title'>โครงสร้างการสร้างรายได้ (Monetization Model)</p>", unsafe_allow_html=True)
        
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.markdown("<p style='font-size:14px; font-weight:600; margin-bottom:2px;'>Transactional Pay</p><span style='font-size:12px; color:#86868B;'>ปรึกษารายครั้ง</span>", unsafe_allow_html=True)
            st.button("ชำระเงิน 350 THB", use_container_width=True)
        with col_m2:
            st.markdown("<p style='font-size:14px; font-weight:600; margin-bottom:2px;'>Premium Subscription</p><span style='font-size:12px; color:#86868B;'>รายเดือนสมาชิก</span>", unsafe_allow_html=True)
            st.button("สมัครสมาชิก 299 THB", type="primary", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# 2. ฝั่งสัตวแพทย์ (B2B Portal)
# ==========================================
elif user_role == "B2B Portal (Veterinary)":
    
    # Feature 1: Vet Dashboard
    st.markdown("<div class='apple-card'>", unsafe_allow_html=True)
    st.markdown("<p class='feature-tag'>Feature 1 • Vet Dashboard & AI Executive Summary</p>", unsafe_allow_html=True)
    st.markdown("<p class='section-title'>พื้นที่ทำงานการวินิจฉัยพาร์ตเนอร์คลินิก</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:13px; color:#86868B; margin-bottom:12px;'>เคสรอตรวจ: สุนัข สายพันธุ์โกลเด้น รีทรีฟเวอร์ (อายุ 5 ปี)</p>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background:#F5F5F7; padding:16px; border-radius:12px; margin-bottom:15px; font-size:14px; line-height:1.5;'>
        <b>AI Executive Summary (ประวัติย่อยโดย AI):</b><br>
        • สัตว์เลี้ยงอาเจียนเป็นฟองสีขาว 3 ครั้งในรอบ 6 ชั่วโมงที่ผ่านมา<br>
        • พฤติกรรมซึมลงอย่างมีนัยสำคัญ และปฏิเสธการทานน้ำลายล่าสุด<br>
        • ข้อเสนอแนะเบื้องต้น: มีความเสี่ยงภาวะ Gastritis ควรรีเช็กสิ่งแปลกปลอมในกระเพาะอาหาร
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Feature 2: Verified Data Labeling
    st.markdown("<div class='apple-card'>", unsafe_allow_html=True)
    st.markdown("<p class='feature-tag'>Feature 2 • Verified Data Labeling</p>", unsafe_allow_html=True)
    st.markdown("<p class='section-title'>การรับรองชุดข้อมูลเกรดทางการแพทย์</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:13px; color:#86868B; margin-bottom:12px;'>ระบบล็อกผลตรวจเพื่อนำไปใช้คำนวณเบี้ยประกันร่วมกับพาร์ตเนอร์ธุรกิจ (B2B Medical Data Asset)</p>", unsafe_allow_html=True)
    
    vet_choice = st.selectbox("ผลการวินิจฉัยสิ้นสุดโดยสัตวแพทย์", ["Gastritis (โรคกระเพาะอาหารอักเสบ)", "Foreign Body Obstruction (สิ่งแปลกปลอมอุดตัน)", "Parvovirus (ลำไส้อักเสบติดต่อ)"])
    if st.button("อนุมัติและลงนามรับรองข้อมูล (Verify Sign-Off)", type="primary", use_container_width=True):
        st.success("ลงทะเบียนรหัสโรคเข้าสู่ฐานข้อมูลความปลอดภัยสูงเรียบร้อย")
    st.markdown("</div>", unsafe_allow_html=True)

    # Feature 3: Referral Tracking
    st.markdown("<div class='apple-card'>", unsafe_allow_html=True)
    st.markdown("<p class='feature-tag'>Feature 3 • Referral Tracking & Commission</p>", unsafe_allow_html=True)
    st.markdown("<p class='section-title'>ระบบติดตามและคำนวณผลประโยชน์พาร์ตเนอร์</p>", unsafe_allow_html=True)
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.metric(label="จำนวนดาวน์โหลดผ่าน QR ประจำคลินิก", value="142 ราย")
    with col_v2:
        st.metric(label="ค่าคอมมิชชันสะสมเดือนปัจจุบัน", value="4,260 THB")
    st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# 3. ฝั่งระบบหลังบ้าน (Backend Infrastructure)
# ==========================================
elif user_role == "Backend Infrastructure":
    
    # Feature 1: Insurance API Gateway
    st.markdown("<div class='apple-card'>", unsafe_allow_html=True)
    st.markdown("<p class='feature-tag'>Phase 2 • Insurance API Gateway</p>", unsafe_allow_html=True)
    st.markdown("<p class='section-title'>โครงสร้างเชื่อมต่อข้อมูลพาร์ตเนอร์ประกันภัย</p>", unsafe_allow_html=True)
    
    api_table = pd.DataFrame({
        'Partner กลุ่มประกันภัย': ['AIA Pet Protect', 'Bangkok Insurance (BKI)', 'Tip Pet Care'],
        'สถานะการเชื่อมต่อ Gateway': ['Connected (Active)', 'Ready to Test', 'In Discussion'],
        'ส่วนลดเบี้ยประกันภัยฐานราก': ['10%', '15%', 'TBD']
    })
    st.table(api_table)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Feature 2: Hardware Integration
    st.markdown("<div class='apple-card'>", unsafe_allow_html=True)
    st.markdown("<p class='feature-tag'>Phase 3 • Hardware Integration (Smart Collar)</p>", unsafe_allow_html=True)
    st.markdown("<p class='section-title'>โมดูลซิงก์ข้อมูลอุปกรณ์สวมใส่ผ่าน API</p>", unsafe_allow_html=True)
    
    col_i1, col_i2, col_i3 = st.columns(3)
    with col_i1:
        st.metric(label="อัตราการเต้นของหัวใจ", value="94 bpm")
    with col_i2:
        st.metric(label="อุณหภูมิร่างกายเฉลี่ย", value="38.6 °C")
    with col_i3:
        st.metric(label="ดัชนีพฤติกรรมการเคลื่อนไหว", value="-5%")
        
    st.progress(0.85, text="ความเสถียรของช่องสัญญาณจำลองฮาร์ดแวร์ (API Sync Rate): 85%")
    st.markdown("</div>", unsafe_allow_html=True)
