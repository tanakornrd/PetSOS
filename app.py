import streamlit as st

# ตั้งค่าหน้าเพจ
st.set_page_config(page_title="PetSOS Mockup", page_icon="🐾", layout="centered")

# ระบบจัดการหน้า (Session State)
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def go_to_page(page_name):
    st.session_state.page = page_name

# ----------------- หน้า 1: Home (The Trigger) -----------------
if st.session_state.page == 'home':
    st.title("🐾 PetSOS")
    st.markdown("### แผนที่นำทางยามวิกฤต สำหรับพ่อแม่สัตว์เลี้ยง")
    st.info("ระบบคัดกรองความเร่งด่วนทางการแพทย์ (AI Triage Protocol)")
    
    st.error("🚨 **คำเตือน:** หากสัตว์เลี้ยงหมดสติ ชัก หรือหยุดหายใจ (Code Red) กรุณารีบพาส่งโรงพยาบาลทันทีโดยไม่ต้องรอประเมิน")
    
    st.write("---")
    st.markdown("<h4 style='text-align: center;'>สัตว์เลี้ยงของคุณมีอาการผิดปกติใช่หรือไม่?</h4>", unsafe_allow_html=True)
    
    # ปุ่มแดงใหญ่ ดึงดูดสายตาคนกำลังแพนิก
    if st.button("🆘 เริ่มประเมินอาการฉุกเฉิน", type="primary", use_container_width=True):
        go_to_page('triage')

# ----------------- หน้า 2: Triage Form (The Engage) -----------------
elif st.session_state.page == 'triage':
    st.title("🩺 ประเมินอาการ (AI Triage)")
    st.write("กรุณาตอบคำถามเบื้องต้นเพื่อให้ระบบประเมินระดับความฉุกเฉิน")
    
    # แบบฟอร์มจำลองการทำงานของ AI
    species = st.selectbox("1. สัตว์เลี้ยงของคุณคืออะไร?", ["สุนัข", "แมว", "สัตว์แปลก (Exotic)"])
    symptom = st.selectbox("2. อาการหลักที่พบ (เลือกอาการที่หนักที่สุด)", 
                           ["เลือกอาการ...", 
                            "อาเจียนไม่หยุด / ถ่ายเหลวรุนแรง", 
                            "ซึม ไม่กินอาหาร", 
                            "มีบาดแผลเล็กน้อย / ขากะเผลก", 
                            "หายใจหอบลำบาก / เหงือกซีด"])
    duration = st.slider("3. มีอาการมานานแค่ไหนแล้ว (ชั่วโมง)?", 1, 48, 1)

    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ ย้อนกลับ", use_container_width=True):
            go_to_page('home')
    with col2:
        if st.button("ประเมินผล ➡️", type="primary", use_container_width=True):
            if symptom != "เลือกอาการ...":
                st.session_state.symptom = symptom
                go_to_page('result')
            else:
                st.warning("กรุณาเลือกอาการก่อนทำการประเมิน")

# ----------------- หน้า 3: Result (The Exit & Monetization) -----------------
elif st.session_state.page == 'result':
    st.title("📊 ผลการประเมินเบื้องต้น")
    symptom = st.session_state.get('symptom', '')
    
    # Logic จำลองการจัด Category สี
    if symptom == "หายใจหอบลำบาก / เหงือกซีด" or symptom == "อาเจียนไม่หยุด / ถ่ายเหลวรุนแรง":
        st.warning("⚠️ **ระดับสีส้ม (Orange): ความเสี่ยงสูง**")
        st.write("อาการของน้องค่อนข้างน่าเป็นห่วง แนะนำให้ปรึกษาสัตวแพทย์อย่างเร่งด่วน หรือเตรียมตัวนำส่งสถานพยาบาล")
        st.button("📞 วิดีโอคอลกับสัตวแพทย์ (รอคิว 5 นาที)", type="primary", use_container_width=True)
        
    elif symptom == "ซึม ไม่กินอาหาร" or symptom == "มีบาดแผลเล็กน้อย / ขากะเผลก":
        st.info("🟡 **ระดับสีเหลือง (Yellow): ความเร่งด่วนต่ำ**")
        st.write("อาการยังไม่เข้าขั้นวิกฤต แนะนำให้ปรึกษาสัตวแพทย์ผ่านระบบ Telemedicine เพื่อประเมินซ้ำและรับคำแนะนำการปฐมพยาบาล")
        st.button("💬 ปรึกษาสัตวแพทย์ทางไกล", use_container_width=True)
        
    else:
        st.success("🟢 **ระดับสีเขียว (Green): ไม่เร่งด่วน**")
        st.write("สามารถสังเกตอาการที่บ้านได้ 24-48 ชั่วโมง หากอาการไม่ดีขึ้นกรุณาติดต่อสัตวแพทย์")
        
    st.write("---")
    # จุดทำเงิน: เสนอขาย Subscription ตอนที่ลูกค้าโล่งใจแล้ว
    st.markdown("💡 **อยากดูแลน้องให้มั่นใจกว่าเดิมไหม?**")
    st.success("สมัคร PetSOS Premium วันนี้ รับสิทธิ์ปรึกษาแพทย์ฟรี 1 ครั้ง/เดือน และระบบ AI Health Timeline ดูแลสุขภาพระยะยาว")
    st.button("✨ ดูรายละเอียด Premium", use_container_width=True)
    
    st.write(" ")
    if st.button("กลับหน้าหลัก", use_container_width=True):
        st.session_state.symptom = ''
        go_to_page('home')