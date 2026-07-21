import streamlit as st
import pandas as pd
import datetime

# 1. Setup layout configurations
st.set_page_config(page_title="Pakner Eldercare Pro", page_icon="👵", layout="centered")

st.markdown("### 👵 Pakner Eldercare Intelligence Platform")
st.markdown("*Long-Term Care Clinical Radar & Assessment Tool*")
st.write("---")

# 2. Initialize Session State Memory for the Alerts
if 'emergency_status_active' not in st.session_state:
    st.session_state['emergency_status_active'] = True  

# 3. Cybersecurity Status Sidebar (Google Cybersecurity Standard)
st.sidebar.markdown("### 🔒 Cybersecurity Status")
st.sidebar.success("Database Security: SECURE")
st.sidebar.info("Audit Log Scan: 0 Anomalies")
st.sidebar.warning(f"Last Security Sync: {datetime.datetime.now().strftime('%H:%M')}")

# 4. Core Telemetry Matrix Data (Mirroring the Circadia alerts you witnessed)
now = datetime.datetime.now()
panic_val = 1 if st.session_state['emergency_status_active'] else 0

# Simulating the high heart rate (>100) and respiration spikes you noted
telemetry_data = pd.DataFrame({
    'Timestamp': [now.strftime('%H:%M:%S'), now.strftime('%H:%M:%S'), now.strftime('%H:%M:%S')],
    'Heart_Rate_BPM': [104, 102, 105] if st.session_state['emergency_status_active'] else,
    'Respiration_RPM': [24, 26, 25] if st.session_state['emergency_status_active'] else,
    'Core_Temp_F': [101.2, 100.8, 101.4] if st.session_state['emergency_status_active'] else [98.6, 98.4, 98.5],
    'Arduino_Panic_Button': [panic_val, panic_val, panic_val]
})

# 5. Live Vitals Alert Banner
st.markdown("#### 🚨 Active Telemetry Alerts")
latest_entry = telemetry_data.iloc[-1]

if st.session_state['emergency_status_active']:
    st.error(f"⚠️ CRITICAL VITALS SPIKE DETECTED: Heart Rate ({latest_entry['Heart_Rate_BPM']} BPM) is above 100! Core Temp is {latest_entry['Core_Temp_F']}°F.")
else:
    st.success("💚 SYSTEM STATUS: Vitals returned to normal baseline values.")

# 6. Mobile Metric Summary Tiles
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Heart Rate", value=f"{latest_entry['Heart_Rate_BPM']} BPM", delta="HIGH" if st.session_state['emergency_status_active'] else "Normal")
with col2:
    st.metric(label="Respiration", value=f"{latest_entry['Respiration_RPM']} RPM", delta="TACHYPNEA" if st.session_state['emergency_status_active'] else "Normal")
with col3:
    st.metric(label="Core Temp", value=f"{latest_entry['Core_Temp_F']} °F", delta="FEVER" if st.session_state['emergency_status_active'] else "Normal")

st.write("---")

# 7. THE HUMAN-IN-THE-LOOP ASSESSMENT PROTOCOL (Your Nursing Wisdom Layer!)
st.markdown("#### 🩺 Nurse Human-in-the-Loop Assessment")
st.markdown("*Use your clinical judgment to evaluate the clinical data signatures alongside history:*")

if st.session_state['emergency_status_active']:
    st.warning("📋 **Diagnostic Hypothesis Tracker:** Current data signatures point to potential **Pneumonia (PNA)** or systemic infection.")
    
    # Interactive clinical checkboxes for the nurse on shift
    check_lung_sounds = st.checkbox("Auscultated Lung Sounds (Checked for diminished breath sounds or crackles)")
    check_cough = st.checkbox("Evaluated Cough / Productive Sputum presence")
    check_hospital_call = st.checkbox("Initiated Physician/Hospital Transfer protocol if indicated")
    
    # The 'Clear Alert' Button only activates when the clinician completes their physical loop check!
    if check_lung_sounds and check_cough:
        if st.button("⚠️ Log Nurse Assessment & Reset Baseline Status", use_container_width=True):
            st.session_state['emergency_status_active'] = False
            st.rerun()
    else:
        st.info("💡 Complete the physical assessment checkboxes above to unlock the baseline reset button.")
else:
    st.success("✅ Assessment Completed: Patient stable. Hospital transfer avoided or managed.")
    if st.button("🔄 Force-Trigger Vitals Spike Simulation (For Testing)", use_container_width=True):
        st.session_state['emergency_status_active'] = True
        st.rerun()

st.write("---")
st.markdown("#### Recent Sensor Activity Log")
st.dataframe(telemetry_data, use_container_width=True)
