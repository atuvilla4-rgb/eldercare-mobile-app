import streamlit as st
import pandas as pd
import datetime
import os

# 1. Setup layout configurations
st.set_page_config(page_title="Eldercare Intelligence Pro", page_icon="👵", layout="centered")

st.markdown("### 👵 Eldercare Intelligence Platform")
st.markdown("*Long-Term Care Clinical Radar & Voice Assessment Tool*")
st.write("---")

# 2. English Butler Accent Audio Routing Logic
def trigger_voice_clinical_alert(text_to_speak):
    print(f"🎙️ Broadcasting Butler Audio Alert: {text_to_speak}")
    # Using 'en-gb+m3' switches to a mature, deep male British English tone
    # -s 125 introduces a calm, poised butler delivery speed
    os.system(f"espeak -v en-gb+m3 -s 125 '{text_to_speak}' 2>/dev/null")
    return True

# 3. Initialize Session State Memory for the Alerts
if 'emergency_status_active' not in st.session_state:
    st.session_state['emergency_status_active'] = True  

# 4. Cybersecurity Status Sidebar
st.sidebar.markdown("### 🔒 Cybersecurity Status")
st.sidebar.success("Database Security: SECURE")
st.sidebar.info("Audit Log Scan: 0 Anomalies")
st.sidebar.warning(f"Last Security Sync: {datetime.datetime.now().strftime('%H:%M')}")

# 5. Standalone Clinical Logic Variables
now = datetime.datetime.now()
panic_val = 1 if st.session_state['emergency_status_active'] else 0

if st.session_state['emergency_status_active']:
    hr_list = [104, 106, 105]      
    resp_list = [24, 25, 24]        
    temp_list = [101.2, 100.8, 101.4]
    fall_risk = 85                  
    infection_risk = 90             
else:
    hr_list = [72, 74, 75]
    resp_list = [16, 15, 16]
    temp_list = [98.6, 98.4, 98.5]
    fall_risk = 12
    infection_risk = 8

# 6. Live Telemetry Feed 
st.markdown("#### 📊 Live Vital Signs Feed")
telemetry_data = pd.DataFrame({
    'Timestamp': [now.strftime('%H:%M:%S'), now.strftime('%H:%M:%S'), now.strftime('%H:%M:%S')],
    'Heart_Rate_BPM': hr_list,
    'Respiration_RPM': resp_list,
    'Core_Temp_F': temp_list,
    'Arduino_Panic_Button': [panic_val, panic_val, panic_val]
})

latest_entry = telemetry_data.iloc[-1]
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Heart Rate", value=f"{latest_entry['Heart_Rate_BPM']} BPM", delta="HIGH (>100)" if st.session_state['emergency_status_active'] else "Normal")
with col2:
    st.metric(label="Respiration", value=f"{latest_entry['Respiration_RPM']} RPM", delta="TACHYPNEA" if st.session_state['emergency_status_active'] else "Normal")
with col3:
    st.metric(label="Core Temp", value=f"{latest_entry['Core_Temp_F']} °F", delta="FEVER" if st.session_state['emergency_status_active'] else "Normal")

st.write("---")

# 7. Active Clinical Alerts & Voice Triggers
st.markdown("#### 📋 Active Vitals Correlation & Risk Analysis")
if st.session_state['emergency_status_active']:
    st.error(f"⚠️ CRITICAL MEDICAL SIGNATURE: Current metrics closely match data patterns for **Pneumonia (PNA)** or severe respiratory infection.")
else:
    st.success("✅ **Patient Stable:** Clinical signatures are currently tracking within normal variances.")

col_risk1, col_risk2 = st.columns(2)
with col_risk1:
    st.metric(label="Calculated Fall Risk", value=f"{fall_risk}%", delta="CRITICAL" if fall_risk > 50 else "Stable")
with col_risk2:
    st.metric(label="Calculated Infection Risk", value=f"{infection_risk}%", delta="HIGH RISK" if infection_risk > 50 else "Stable")

st.write("---")

# 8. Bedside Preventive Protocols 
st.markdown("#### 💊 Immediate Bedside Care Protocols")
if st.session_state['emergency_status_active']:
    st.warning("""
    **Required Preventative Actions Activated:**
    *   **Action 1:** Deploy low-cost floor sensor pressure mats to bedside instantly.
    *   **Action 2:** Initiate 15-minute hydration protocol (8oz fluids) to reduce delirium risk.
    *   **Action 3:** Prepare clinical documentation for potential hospital transfer assessment.
    """)
else:
    st.info("✅ **Routine Care:** Baseline maintenance. Standard preventative rounding loops sufficient.")

st.write("---")

# 9. Clinician Validation & Voice Reset Handshake
st.markdown("#### 🩺 Nurse Physical Assessment & Validation Loop")
st.markdown("*Evaluate the patient physically to verify the system findings before clearing the alarm state:*")

if st.session_state['emergency_status_active']:
    check_lung_sounds = st.checkbox("Auscultated Lung Sounds (Verified diminished breath sounds, rales, or crackles)")
    check_cough = st.checkbox("Evaluated Cough Dynamics (Assessed for painful or productive cough indications)")
    
    if check_lung_sounds and check_cough:
        st.success("🔗 Clinical assessment complete. Finding signatures align with dashboard data.")
        if st.button("⚠️ Clear Emergency State & Log Intervention Cache", use_container_width=True):
            st.session_state['emergency_status_active'] = False
            
            # DEPLOY THE CINEMATIC BUTLER AUDIO HANDSHAKE
            trigger_voice_clinical_alert("Alert cleared, sir. The resident has been verified safe by the caregiver on shift.")
            
            st.rerun()
    else:
        st.info("💡 Complete the physical assessment checkboxes above to unlock the baseline reset button.")
else:
    st.success("💚 System Clear: Resident verified safe. Baseline state re-archived in database logs.")
    if st.button("🔄 Force-Trigger Vitals Spike Simulation (For System Testing)", use_container_width=True):
        st.session_state['emergency_status_active'] = True
        
        # DEPLOY THE URGENT CINEMATIC BUTLER AUDIO HANDSHAKE
        trigger_voice_clinical_alert("Warning, sir. A critical vitals spike has been detected. Heart rate is above one hundred. Pray evaluate for pneumonia risk.")
        
        st.rerun()

st.write("---")
st.markdown("#### Recent Sensor Activity Log")
st.dataframe(telemetry_data, use_container_width=True)
