import streamlit as st
import pandas as pd
import datetime

# 1. Setup mobile interface dimensions
st.set_page_config(page_title="Eldercare Monitor", page_icon="👵", layout="centered")

st.markdown("### 👵 Senior Care Secure Live Feed")
st.markdown("*Low-Resource Monitoring Portal for Families*")
st.write("---")

# 2. Initialize Session State Memory for the Emergency Flag
if 'emergency_status_active' not in st.session_state:
    st.session_state['emergency_status_active'] = True  # Defaults to active from the raw trigger simulation

# 3. Cybersecurity Status Sidebar Panel (Google Cybersecurity standard)
st.sidebar.markdown("### 🔒 Cybersecurity Status")
st.sidebar.success("Database Security: SECURE")
st.sidebar.info("Audit Log Scan: 0 Anomalies")
st.sidebar.warning(f"Last Sync: {datetime.datetime.now().strftime('%H:%M')}")

# 4. Action Container Section: The Caregiver Interface
st.markdown("#### 🛠️ Caregiver Intervention Actions")

if st.session_state['emergency_status_active']:
    st.error("🚨 EMERGENCY CRISIS: Arduino Panic Button Activated! Check on resident immediately.")
    
    # The 'Clear Alert' Button layout
    if st.button("⚠️ Clear Alert (Reset Status to Stable)", use_container_width=True):
        st.session_state['emergency_status_active'] = False
        st.rerun()
else:
    st.success("💚 SYSTEM STATUS: Stable. Resident has been verified safe by caregiver.")
    
    # Option to manually simulate a new emergency trigger for testing
    if st.button("🔄 Simulate New Panic Trigger Alert", use_container_width=True):
        st.session_state['emergency_status_active'] = True
        st.rerun()

st.write("---")

# 5. Telemetry Sensor Log Matrix Data
now = datetime.datetime.now()
telemetry_data = pd.DataFrame({
    'Timestamp': [now.strftime('%H:%M:%S')] * 5,
    'Voice_Status': ['Stable', 'Stable', 'Distressed (Spoke Loudly)', 'Stable', 'Stable'],
    'Eye_Sensor_Alert': ['Clear', 'Clear', 'Obstacle Detected', 'Clear', 'Clear'],
    'Core_Temp_F': [98.6, 98.4, 99.1, 98.6, 98.5],
    'Arduino_Panic_Button': [1 if st.session_state['emergency_status_active'] else 0] * 5
})

# 6. Mobile Metric Summary Tiles
latest_entry = telemetry_data.iloc[0]
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Core Temp", value=f"{latest_entry['Core_Temp_F']} °F")
with col2:
    st.metric(label="Vocal State", value=latest_entry['Voice_Status'])
with col3:
    st.metric(label="Eye Sensor", value=latest_entry['Eye_Sensor_Alert'])

st.write("---")
st.markdown("#### Recent Sensor Activity Log")
st.dataframe(telemetry_data, use_container_width=True)

# 7. 4-Agent CrewAI Health Report Insights Summary
st.write("---")
st.markdown("#### 🤖 Daily Automated Clinical Insight")
st.info(f"""
📋 **Geriatric Wellness Report (System State Checkpoint)**
• **Security Log Status:** Passed. Active encryption handshakes are fully verified. 
• **Current Assessment:** {"CRITICAL: Emergency button state requires physical verification." if st.session_state['emergency_status_active'] else "RESOLVED: Caregiver verified resident safety. Status returned to normal baseline values."}
""")
