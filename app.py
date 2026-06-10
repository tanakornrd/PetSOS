import streamlit as st
import pandas as pd

# --- 1. System Configuration & Clean Apple Institutional Design ---
st.set_page_config(page_title="PetSOS Platform", page_icon="🐾", layout="centered")

# Global Minimalist CSS Styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&display=swap');
        
        /* Global Apple Typography Standard */
        html, body, .stApp, .stMarkdown, p, label, select, input {
            font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Prompt", sans-serif !important;
            color: #1D1D1F !important;
        }
        
        /* Clean Canvas Background */
        .stApp { background-color: #F5F5F7 !important; }
        
        /* Hide Infrastructure UI Noise */
        header, footer, #MainMenu { visibility: hidden !important; }
        
        /* Title Alignment */
        .apple-main-title {
            font-size: 34px !important;
            font-weight: 700 !important;
            letter-spacing: -0.8px !important;
            text-align: center;
            margin-top: 15px;
            margin-bottom: 2px;
        }
        .apple-main-subtitle {
            font-size: 16px !important;
            font-weight: 400 !important;
            color: #86868B !important;
            text-align: center;
            margin-bottom: 25px;
        }

        /* Micro-Labels for Features */
        .feature-context {
            font-size: 11px !important;
            font-weight: 600 !important;
            color: #86868B !important;
            letter-spacing: 0.5px !important;
            text-transform: uppercase;
            margin-bottom: 2px;
        }
        .block-heading {
            font-size: 19px !important;
            font-weight: 600 !important;
            letter-spacing: -0.3px !important;
            margin-top: 0px;
            margin-bottom: 10px;
        }

        /* Native Look Input Elements */
        div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {
            border-radius: 12px !important;
            border: 1px solid #D2D2D7 !important;
            background-color: #FFFFFF !important;
        }

        /* Apple UI Button Matrix */
        .stButton > button {
            border-radius: 12px !important;
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
        
        /* Primary Action Accent */
        button[kind="primary"] {
            background-color: #007AFF !important;
            color: #FFFFFF !important;
            border: none !important;
        }
        button[kind="primary"]:hover { background-color: #0062CC !important; }
        
        /* Metric Typography */
        div[data-testid="stMetricValue"] {
            font-size: 26px !important;
            font-weight: 600 !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- 2. Identity Branding ---
st.markdown("<h1 class='apple-main-title'>PetSOS</h1>", unsafe_allow_html=True)
st.markdown("<p class='apple-main-subtitle'>Ecosystem Demonstration Workspace</p>", unsafe_allow_html=True)

# --- 3. Robust Role Navigator (Dropdown Mechanism for Mobile) ---
current_workspace = st.selectbox(
    "เลือกหน้าต่างระบบนำเสนอ (Workspace View):",
    [
        "📱 ฝั่งเจ้าของสัตว์เลี้ยง (B2C Mobile App)", 
        "🩺 ฝั่งสัตวแพทย์พันธมิตร (B2B Portal)", 
        "🌐 โครงสร้างการเชื่อมต่อข้อมูลหลังบ้าน (Backend Infrastructure)"
    ]
)
st.write("---")


# ==========================================
# 1. ฝั่งผู้ใช้งานทั่วไป (B2C App)
# ==========================================
if current_workspace == "📱 ฝั่งเจ้าของสัตว์เลี้ยง (B2C Mobile App)":
    
    # Step Selector inside B2C to show sequential user journey cleanly
    b2c_step = st.selectbox(
        "ขั้นตอนในสัญญะการใช้งาน (User Journey Step):",
        [
            "ขั้นตอนที่ 1: หน้าแรก และการคัดกรองอาการเบื้องต้น",
            "ขั้นตอนที่ 2: หน้าจอวิกฤตความรับผิดชอบเป็นศูนย์ (Code Red)",
            "ขั้นตอนที่ 3: หน้าแสดงผลลัพธ์ และระบบการแพทย์ทางไกลพร้อมชำระเงิน"
        ]
    )
    st.write("<br>", unsafe_allow_html=True)

    # --- STEP 1: HOME & TRIAGE INTAKE (Features 1, 2, 5) ---
    if b2c_step == "ขั้นตอนที่ 1: หน้าแรก และการคัดกรองอาการเบื้องต้น":
        
        # Feature 1: One-Tap SOS
        with st.container(border=True):
            st.markdown("<p class='feature-context'>Feature 1 • One-Tap SOS</p>", unsafe_allow_html=True)
            st.markdown("<h3 class='block-heading'>ปุ่มขอความช่วยเหลือฉุกเฉิน</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:#666; font-size:14px; margin-bottom:15px;'>ระบบตัดวงจรการซักประวัติเพื่อนำทางไปยังโรงพยาบาลที่ใกล้ที่สุดทันทีเมื่อผู้ใช้เกิดความตื่นตระหนกสูงสุด</p>", unsafe_allow_html=True)
            if st.button("🚨 SOS Emergency Assistance", use_container_width=True):
                st.warning("ระบบจำลองตรวจพบการกดเหตุฉุกเฉิน กรุณาปรับแถบเลือกขั้นตอนด้านบนเป็น 'ขั้นตอนที่ 2' เพื่อตรวจงานหน้าจอส่งโรงพยาบาลด่วนครับ")
        
        st.write("<br>", unsafe_allow_html=True)
        
        # Feature 2: AI Triage Engine
        with st.container(border=True):
            st.markdown("<p class='feature-context'>Feature 2 • AI Triage Engine</p>", unsafe_allow_html=True)
            st.markdown("<h3 class='block-heading'>ระบบวิเคราะห์อาการดิจิทัล</h3>", unsafe_allow_html=True)
            
            species = st.selectbox("ชนิดของสัตว์เลี้ยง", ["สุนัข", "แมว", "สัตว์แปลก (Exotic)"])
            user_input = st.text_input("อธิบายอาการผิดปกติขั้นต้น:", placeholder="เช่น สุนัขมีอาการซึม ไม่กินอาหาร หรืออาเจียน")
            st.file_uploader("แนบรูปภาพหรือวิดีโออาการประกอบการวินิจฉษย (ถ้ามี)", type=['png','jpg','mp4'])
            
            if st.button("ส่งข้อมูลเพื่อประเมินผล ➡️", type="primary", use_container_width=True):
                st.success("บันทึกข้อมูลเข้าสู่การประเมินแล้ว กรุณาปรับแถบเลือกขั้นตอนด้านบนเป็น 'ขั้นตอนที่ 3' เพื่อตรวจสอบการจำลองผลลัพธ์ระดับสีเหลืองครับ")

        st.write("<br>", unsafe_allow_html=True)

        # Feature 5: AI Health Timeline & Reminders
        with st.container(border=True):
            st.markdown("<p class='feature-context'>Feature 5 • AI Health Timeline & Reminders</p>", unsafe_allow_html=True)
            st.markdown("<h3 class='block-heading'>แดชบอร์ดประวัติสุขภาพและการแจ้งเตือน</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:#86868B; font-size:13px; margin-bottom:12px;'>กลไกสำคัญในการรักษาฐานลูกค้าเพื่อผลักดันยอดสมัครสมาชิกระดับพรีเมียม (Premium Subscription Retention)</p>", unsafe_allow_html=True)
            
            mock_timeline = pd.DataFrame({
                'โปรแกรมการดูแลรักษา': ['การฉีดวัคซีนรวมประจำปี', 'การหยดยาป้องกันเห็บหมัดประจำเดือน', 'การตรวจคัดกรองโรคไตขั้นสูง'],
                'สถานะการแจ้งเตือน': ['🔴 เกินกำหนดเวลาบริการ', '🔔 ถึงกำหนดในสัปดาห์นี้', '📅 มีแผนการในอีก 3 เดือน']
            })
            st.table(mock_timeline)

    # --- STEP 2: CODE RED ROUTING (Feature 3) ---
    elif b2c_step == "ขั้นตอนที่ 2: หน้าจอวิกฤตความรับผิดชอบเป็นศูนย์ (Code Red)":
        with st.container(border=True):
            st.markdown("<p class='feature-context' style='color:#FF3B30;'>Feature 3 • Zero-Liability Emergency Routing</p>", unsafe_allow_html=True)
            st.markdown("<h3 class='block-heading' style='color:#FF3B30;'>ระบบจัดการกรณีวิกฤตสูงสุด (Code Red)</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:#1D1D1F; font-size:14px; margin-bottom:15px;'>อัลกอริทึมประเมินพบสภาวะเสี่ยงต่อสัญญาณชีพ ระบบข้ามขั้นตอน AI ทั้งหมดโดยอัตโนมัติ เพื่อนำทางไปยังสถานพยาบาลสัตว์ 24 ชั่วโมงที่ใกล้ที่สุดเพื่อลดภาระความรับผิดชอบทางกฎหมายของแพลตฟอร์ม</p>", unsafe_allow_html=True)
            
            # Map simulation
            map_data = pd.DataFrame({'lat': [13.7367, 13.7456], 'lon': [100.5331, 100.5210]})
            st.map(map_data)
            
            st.write("<br>", unsafe_allow_html=True)
            st.button("📞 ติดต่อสายด่วนโรงพยาบาลสัตว์วิกฤตทันที", type="primary", use_container_width=True)

    # --- STEP 3: OUTPUT, TELEMED & PAYMENT (Features 4, 6) ---
    elif b2c_step == "ขั้นตอนที่ 3: หน้าแสดงผลลัพธ์ และระบบการแพทย์ทางไกลพร้อมชำระเงิน":
        
        with st.container(border=True):
            st.markdown("<p class='feature-context'>Triage Evaluation Output</p>", unsafe_allow_html=True)
            st.markdown("<h3 class='block-heading'>ผลการประเมิน: ระดับสีเหลือง (Observe)</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:#424245; font-size:14px;'>อาการสัตว์เลี้ยงพ้นขีดอันตรายฉุกเฉินเฉียบพลัน แนะนำให้สังเกตพฤติกรรมอย่างใกล้ชิด หรือนัดหมายแพทย์ผ่านระบบการแพทย์ทางไกลเพื่อคลายความกังวล</p>", unsafe_allow_html=True)

        st.write("<br>", unsafe_allow_html=True)

        # Feature 4: Telemedicine Gateway
        with st.container(border=True):
            st.markdown("<p class='feature-context'>Feature 4 • Telemedicine Gateway</p>", unsafe_allow_html=True)
            st.markdown("<h3 class='block-heading'>ระบบการแพทย์ทางไกลสัตวแพทย์ออนไลน์</h3>", unsafe_allow_html=True)
            st.markdown("<div style='background:#FFF9E6; padding:10px; border-radius:8px; text-align:center; font-size:13px; font-weight:500; color:#B45309; margin-bottom:15px;'>⏳ ระยะเวลารอสายสัตวแพทย์สแตนด์บาย: 12:45 นาที</div>", unsafe_allow_html=True)
            st.button("🎥 เข้าสู่ห้องสนทนาและเปิดระบบ Video Call กับแพทย์", type="primary", use_container_width=True)

        st.write("<br>", unsafe_allow_html=True)

        # Feature 6: Payment & Subscription Manager
        with st.container(border=True):
            st.markdown("<p class='feature-context'>Feature 6 • Payment & Subscription Manager</p>", unsafe_allow_html=True)
            st.markdown("<h3 class='block-heading'>กลไกการแปลงเป็นรายได้ (Monetization Model)</h3>", unsafe_allow_html=True)
            
            col_m1, col_m2 = st.columns(2)
            with col_m1:
                st.markdown("<p style='font-size:14px; font-weight:600; margin-bottom:2px;'>Pay-Per-Use</p><span style='font-size:12px; color:#86868B;'>ยอดชำระค่ารักษาคำนวณรายครั้ง</span>", unsafe_allow_html=True)
                st.button("ชำระค่าบริการ 350 บาท", use_container_width=True)
            with col_m2:
                st.markdown("<p style='font-size:14px; font-weight:600; margin-bottom:2px;'>Premium Membership</p><span style='font-size:12px; color:#86868B;'>ยอดสมัครระบบรายเดือนพรีเมียม</span>", unsafe_allow_html=True)
                st.button("สมัครสมาชิก 299.-/ด.", type="primary", use_container_width=True)


# ==========================================
# 2. ฝั่งสัตวแพทย์ (B2B Portal)
# ==========================================
elif current_workspace == "🩺 ฝั่งสัตวแพทย์พันธมิตร (B2B Portal)":
    
    # Feature 1: Vet Dashboard
    with st.container(border=True):
        st.markdown("<p class='feature-context'>Feature 1 • Vet Dashboard & AI Executive Summary</p>", unsafe_allow_html=True)
        st.markdown("<h3 class='block-heading'>พื้นที่ปฏิบัติงานซักประวัติสัตวแพทย์</h3>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:13px; color:#86868B; margin-bottom:12px;'>ผู้ป่วยรอการตรวจ: สุนัข สายพันธุ์โกลเด้น รีทรีฟเวอร์ (อายุ 5 ปี)</p>", unsafe_allow_html=True)
        
        st.markdown("""
        <div style='background:#F5F5F7; padding:16px; border-radius:12px; margin-bottom:5px; font-size:14px; line-height:1.5; color:#1D1D1F;'>
            <b>บทสรุปประวัติโดยย่อยจาก AI (AI Executive Summary):</b><br>
            • สัตว์เลี้ยงมีอาการอาเจียนเป็นฟองสีขาว 3 ครั้งในรอบระยะเวลา 6 ชั่วโมงที่ผ่านมา<br>
            • ดัชนีกิจกรรมลดลงอย่างมีนัยสำคัญราว 40% และปฏิเสธการดื่มน้ำลายล่าสุด<br>
            • ข้อเสนอแนะทางการแพทย์เบื้องต้น: มีความเสี่ยงต่อภาวะ Gastritis ควรรีเช็กสิ่งแปลกปลอมอุดตันในทางเดินอาหาร
        </div>
        """, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)

    # Feature 2: Verified Data Labeling
    with st.container(border=True):
        st.markdown("<p class='feature-context'>Feature 2 • Verified Data Labeling</p>", unsafe_allow_html=True)
        st.markdown("<h3 class='block-heading'>การลงนามรับรองชุดข้อมูลทางการแพทย์</h3>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:13px; color:#86868B; margin-bottom:12px;'>ระบบล็อกผลวินิจฉัยเพื่อแปลงข้อมูลเป็น Medical-grade Data Asset สำหรับสร้างมูลค่าส่งต่อธุรกิจกลุ่มประกันภัย</p>", unsafe_allow_html=True)
        
        vet_choice = st.selectbox("การวินิจฉัยและรับรองรหัสโรคขั้นสุดท้าย:", ["Gastritis (โรคกระเพาะอาหารอักเสบ)", "Foreign Body Obstruction (สิ่งแปลกปลอมอุดตัน)", "Parvovirus (ลำไส้อักเสบติดต่อ)"])
        if st.button("บันทึกและอนุมัติการรับรองแพทย์ (Verify Sign-Off)", type="primary", use_container_width=True):
            st.success("โครงสร้างชุดข้อมูลได้รับการอนุมัติและจัดเก็บในระบบความปลอดภัยสูงเรียบร้อยแล้ว")

    st.write("<br>", unsafe_allow_html=True)

    # Feature 3: Referral Tracking
    with st.container(border=True):
        st.markdown("<p class='feature-context'>Feature 3 • Referral Tracking & Commission</p>", unsafe_allow_html=True)
        st.markdown("<h3 class='block-heading'>สถิติและผลประโยชน์พาร์ตเนอร์สถานพยาบาล</h3>", unsafe_allow_html=True)
        
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.metric(label="ยอดผู้สมัครงานผ่านรหัส QR คลินิกนี้", value="142 ราย")
        with col_c2:
            st.metric(label="ค่าส่วนแบ่งคอมมิชชันสะสมเดือนนี้", value="4,260 THB")
        st.write("<br>", unsafe_allow_html=True)
        st.button("ดาวน์โหลดไฟล์ระบบรหัส QR Code ประจำสถานพยาบาล", use_container_width=True)


# ==========================================
# 3. ฝั่งระบบหลังบ้าน (Backend Infrastructure)
# ==========================================
elif current_workspace == "🌐 โครงสร้างการเชื่อมต่อข้อมูลหลังบ้าน (Backend Infrastructure)":
    
    # Feature 1: Insurance API Gateway
    with st.container(border=True):
        st.markdown("<p class='feature-context'>Phase 2 • Insurance API Gateway</p>", unsafe_allow_html=True)
        st.markdown("<h3 class='block-heading'>สถาปัตยกรรมเชื่อมต่อข้อมูลกลุ่มพันธมิตรประกันภัย</h3>", unsafe_allow_html=True)
        
        api_table = pd.DataFrame({
            'ชื่อหน่วยงานประกันภัยพาร์ตเนอร์': ['AIA Pet Protect', 'Bangkok Insurance (BKI)', 'Tip Pet Care'],
            'สถานะช่องสัญญาณ Gateway': ['Connected (Active)', 'Ready to Test', 'In Discussion'],
            'ส่วนลดเบี้ยประกันภัยส่งมอบให้ลูกค้า': ['10%', '15%', 'TBD']
        })
        st.table(api_table)

    st.write("<br>", unsafe_allow_html=True)

    # Feature 2: Hardware Integration
    with st.container(border=True):
        st.markdown("<p class='feature-context'>Phase 3 • Hardware Integration (Smart Collar)</p>", unsafe_allow_html=True)
        st.markdown("<h3 class='block-heading'>โมดูลซิงก์ข้อมูลอุปกรณ์สวมใส่อัจฉริยะแบบ Real-time</h3>", unsafe_allow_html=True)
        
        col_i1, col_i2, col_i3 = st.columns(3)
        with col_i1: st.metric(label="อัตราเต้นหัวใจสัตว์เลี้ยง", value="94 bpm")
        with col_i2: st.metric(label="อุณหภูมิร่างกายเฉลี่ย", value="38.6 °C")
        with col_i3: st.metric(label="ดัชนีการเคลื่อนไหวทางกาย", value="-5%")
            
        st.write("<br>", unsafe_allow_html=True)
        st.progress(0.85, text="เสถียรภาพการซิงก์ชุดข้อมูลสัญญาณฮาร์ดแวร์จำลอง (API Sync Rate): 85%")
