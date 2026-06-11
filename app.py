import streamlit as st
import pandas as pd
import numpy as np

# --- 1. System Configuration ---
st.set_page_config(page_title="PetSOS", page_icon="🐾", layout="centered")

# --- 2. Apple Store Exact CSS Architecture + Ultimate Uploader Fix ---
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

        /* 2. Apple Store Hero Headings */
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

        /* 3. Segmented Control (Top Nav) */
        div[data-testid="stRadio"] > div {
            background-color: #E8E8ED !important;
            padding: 4px !important;
            border-radius: 12px !important;
            gap: 4px !important;
        }
        div[data-testid="stRadio"] div[role="radio"] div:first-child { display: none !important; }
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
        
        /* --- 🩹 ULTIMATE FIX: File Uploader Lock --- */
        div[data-testid="stFileUploader"] section {
            border: 1px dashed #D2D2D7 !important;
            background-color: #F5F5F7 !important;
            border-radius: 12px !important;
            padding: 15px !important;
        }
        div[data-testid="stFileUploader"] button {
            white-space: nowrap !important;
            width: max-content !important;
            min-width: 100px !important;
            margin: 0 auto !important;
            border-radius: 8px !important;
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

        /* Metric Styling override */
        div[data-testid="stMetricValue"] {
            font-size: 22px !important;
            font-weight: 700 !important;
            color: #1D1D1F !important;
        }
        div[data-testid="stMetricLabel"] {
            font-size: 13px !important;
            color: #86868B !important;
        }
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
        st.markdown("<div class='apple-subhero'>ดูแลสัตว์เลี้ยงที่คุณรัก<br>ด้วยข้อมูลและผู้เชี่ยวชาญ</div>", unsafe_allow_html=True)
        
        # --- Feature: Pet Basic Profile (Dashboard หน้าแรก) ---
        with st.container(border=True):
            st.markdown("<h3 style='margin-bottom:0px; font-size:22px; font-weight:700;'>🐶 ข้อมูลของน้องคูเปอร์ (Cooper)</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:#86868B; font-size:14px; margin-bottom:15px; font-weight:500;'>ข้อมูลพื้นฐานและสถานะสุขภาพวันนี้</p>", unsafe_allow_html=True)
            
            p1, p2, p3 = st.columns(3)
            p1.metric("สายพันธุ์", "โกลเด้นฯ")
            p2.metric("อายุ", "5 ปี 2 ด.")
            p3.metric("น้ำหนัก", "28.5 kg")
            
            st.markdown("""
                <div style='background-color:#E8F5E9; padding:10px; border-radius:10px; text-align:center; margin-top:5px;'>
                    <span style='color:#2E7D32; font-weight:600; font-size:14px;'>🟢 สถานะ: ร่าเริงปกติ (ไม่มีการแจ้งเตือนพฤติกรรม)</span>
                </div>
            """, unsafe_allow_html=True)

        st.write("<br>", unsafe_allow_html=True)
        st.markdown("<h3 style='font-size:22px; font-weight:700; text-align:center;'>บริการความช่วยเหลือ</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color:#86868B; font-size:14px; text-align:center; margin-bottom:20px;'>เลือกเครื่องมือตามระดับความฉุกเฉิน</p>", unsafe_allow_html=True)

        # --- Feature: Code Red ---
        with st.container(border=True):
            st.markdown("<h3 style='margin-bottom:0px; font-size:20px; font-weight:700;'>🚨 กรณีฉุกเฉินวิกฤต</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:#86868B; font-size:14px; margin-bottom:15px; font-weight:500;'>หมดสติ ชัก หรือหยุดหายใจ</p>", unsafe_allow_html=True)
            st.markdown("""<style>div:nth-child(1) > div > div > button { background-color: #FF3B30 !important; color: white !important; font-weight:600 !important; }</style>""", unsafe_allow_html=True)
            if st.button("🔴 ขอความช่วยเหลือด่วน (SOS)"):
                navigate('sos')
                st.rerun()

        # --- Feature: Triage Engine (Speed-Optimized) ---
        with st.container(border=True):
            st.markdown("<h3 style='margin-bottom:0px; font-size:20px; font-weight:700;'>🩺 ประเมินอาการเบื้องต้น</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:#86868B; font-size:14px; margin-bottom:15px; font-weight:500;'>แตะเพื่อประเมินผลทันที หรือพิมพ์อาการด้านล่าง</p>", unsafe_allow_html=True)
            
            # --- กลยุทธ์ One-Tap Symptom Chips ---
            st.markdown("<p style='font-size:14px; font-weight:600; margin-bottom:8px;'>อาการที่พบบ่อย (Quick Select)</p>", unsafe_allow_html=True)
            q1, q2 = st.columns(2)
            if q1.button("🤮 อาเจียน / ท้องเสีย", use_container_width=True):
                navigate('result')
                st.rerun()
            if q2.button("🤒 ซึม / ไม่กินอาหาร", use_container_width=True):
                navigate('result')
                st.rerun()
            
            q3, q4 = st.columns(2)
            if q3.button("🩸 เลือดออก / มีแผล", use_container_width=True):
                navigate('result')
                st.rerun()
            if q4.button("🦵 เดินขากะเผลก", use_container_width=True):
                navigate('result')
                st.rerun()

            st.markdown("<hr style='margin: 15px 0px; border-color: #E8E8ED;'>", unsafe_allow_html=True)
            
            # --- ส่วนสำหรับอาการอื่นๆ ที่ต้องพิมพ์ ---
            st.markdown("<p style='font-size:14px; font-weight:600; margin-bottom:4px;'>ระบุอาการด้วยตนเอง</p>", unsafe_allow_html=True)
            species = st.selectbox("ชนิดสัตว์เลี้ยง", ["สุนัข", "แมว", "สัตว์แปลก (Exotic)"], label_visibility="collapsed")
            user_input = st.text_input("อาการที่พบ", placeholder="เช่น ผื่นแดงตามหน้าท้อง...", label_visibility="collapsed")
            
            st.markdown("<p style='font-size:14px; font-weight:600; margin-bottom:4px; margin-top:10px;'>แนบรูปภาพ/วิดีโอ (ถ้ามี)</p>", unsafe_allow_html=True)
            st.file_uploader("แนบไฟล์", type=['png','jpg','mp4'], label_visibility="collapsed")
            
            st.write("")
            if st.button("ส่งข้อมูลให้ AI ประเมินผล", type="primary"):
                navigate('result')
                st.rerun()

        # --- Feature: AI Behavioral Insights Dashboard (B2C) ---
        with st.container(border=True):
            st.markdown("<h3 style='margin-bottom:0px; font-size:20px; font-weight:700;'>📊 สถิติพฤติกรรมเชิงลึก</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:#86868B; font-size:14px; margin-bottom:15px; font-weight:500;'>เครื่องมือแปลภาษาพฤติกรรมสัตว์</p>", unsafe_allow_html=True)
            if st.button("ดูรายงานพฤติกรรม ➡️"):
                navigate('insights')
                st.rerun()

    # ---------------- PAGE: AI INSIGHTS (Dashboard) ----------------
    elif st.session_state.page == 'insights':
        st.markdown("<div class='apple-hero'>AI Insights</div>", unsafe_allow_html=True)
        st.markdown("<div class='apple-subhero'>วิเคราะห์พฤติกรรมเชิงลึกของ Cooper</div>", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("<h3 style='font-size:20px; font-weight:700;'>📊 สถิติพฤติกรรม (รอบ 7 วัน)</h3>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            col1.metric("ความเครียด", "12 ครั้ง", "-15%")
            col2.metric("คุณภาพนอน", "8.5 ชม.", "+20%")
            col3.metric("ซึม/หลบมุม", "2 ครั้ง", "-5%")

            st.write("<br>", unsafe_allow_html=True)
            st.markdown("<p style='font-size:14px; font-weight:600;'>แนวโน้มความผิดปกติ (Anomaly Trend)</p>", unsafe_allow_html=True)
            
            chart_data = pd.DataFrame(
                np.random.randint(0, 10, size=(7, 2)),
                columns=['เดินวนกระวนกระวาย', 'เลียเท้าผิดปกติ'],
                index=['จ.', 'อ.', 'พ.', 'พฤ.', 'ศ.', 'ส.', 'อา.']
            )
            st.line_chart(chart_data)

        with st.container(border=True):
            st.markdown("<h3 style='font-size:18px; font-weight:700;'>🔔 Preventive Reminders</h3>", unsafe_allow_html=True)
            st.info("📅 ครบกำหนดหยอด Revolution ในอีก 3 วัน")

        st.write("<br>", unsafe_allow_html=True)
        if st.button("⬅️ กลับหน้าหลัก"):
            navigate('home')
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
    st.markdown("<div class='apple-subhero'>พื้นที่ปฏิบัติงานและบริหารจัดการคลินิก</div>", unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("<h3 style='font-size:20px; font-weight:700;'>📈 Clinic Economics Tracker</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color:#86868B; font-size:14px; margin-bottom:15px;'>สรุปผลประกอบการและเคสส่งต่อจากแพลตฟอร์ม</p>", unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns(3)
        c1.metric("เคสส่งต่อ", "42 เคส", "+12%")
        c2.metric("รายได้ Telemed", "฿14,700", "+8%")
        c3.metric("ปิดการขาย", "68%", "เยี่ยม")

    with st.container(border=True):
        st.markdown("<h3 style='font-size:20px; font-weight:700;'>📋 Live Triage Board</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color:#86868B; font-size:14px; margin-bottom:15px;'>คิวคนไข้รอรับบริการ (เรียลไทม์)</p>", unsafe_allow_html=True)
        
        triage_data = pd.DataFrame({
            'คิว': ['#012', '#013', '#014'],
            'ระดับ': ['🟧 สีส้ม', '🟨 สีเหลือง', '🟨 สีเหลือง'],
            'อาการ': ['อาเจียนต่อเนื่อง', 'ซึม ไม่กินอาหาร', 'เกาหูสะบัดหัว'],
            'รอคิว': ['04:12 น.', '11:30 น.', '14:05 น.']
        })
        st.table(triage_data)

    with st.container(border=True):
        st.markdown("<h3 style='font-size:20px; font-weight:700;'>สรุปข้อมูลผู้ป่วย (AI Summary)</h3>", unsafe_allow_html=True)
        st.info("เคส #012: คูเปอร์ (โกลเด้นฯ อายุ 5 ปี) - เสี่ยงภาวะ Gastritis")
        
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
