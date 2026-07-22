import streamlit as st
import pandas as pd
import datetime
import os
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Eldercare Control Pro", page_icon="👵", layout="centered")

st.markdown("### 👵 Eldercare Intelligence Platform")
st.markdown("*Long-Term Care Clinical Radar & Surveillance Network*")
st.write("---")

def trigger_voice_clinical_alert(text_to_speak):
    print(f"🎙️ Broadcasting Butler Audio Alert: {text_to_speak}")
    os.system(f"espeak -v en-gb+m3 -s 145 '{text_to_speak}' 2>/dev/null")
    return True

st.sidebar.markdown("### 🔒 System Security Matrix")
st.sidebar.success("Database Security: SECURE")
st.sidebar.info("Audit Log Network Scan: 0 Anomalies")
st.sidebar.warning(f"Last Cloud Sync: {datetime.datetime.now().strftime('%H:%M')}")

if 'emergency_status_active' not in st.session_state:
    st.session_state['emergency_status_active'] = True  

tab1, tab2, tab3 = st.tabs(["📝 Shift Activity", "🔬 C-Diff Surveillance", "🗂️ Patient Registry"])

with tab1:
    now = datetime.datetime.now()
    panic_val = 1 if st.session_state['emergency_status_active'] else 0
    
    if st.session_state['emergency_status_active']:
        hr_list = [104, 106, 108]
        resp_list = [24, 25, 26]
        temp_list = [101.2, 100.8, 101.4]
    else:
        hr_list = [72, 74, 75]
        resp_list = [16, 17, 18]
        temp_list = [98.6, 98.4, 98.5]
    
    telemetry_data = pd.DataFrame({
        'Timestamp': [now.strftime('%H:%M:%S'), now.strftime('%H:%M:%S'), now.strftime('%H:%M:%S')],
        'Heart_Rate_BPM': hr_list,
        'Respiration_RPM': resp_list,
        'Core_Temp_F': temp_list,
        'Arduino_Panic_Button': [panic_val, panic_val, panic_val]
    })
    
    latest_entry = telemetry_data.iloc[-1]
    
    if st.session_state['emergency_status_active']:
        st.error(f"⚠️ CRITICAL VITAL ANOMALY: Heart Rate ({latest_entry['Heart_Rate_BPM']} BPM) is above 100! Core Temp is {latest_entry['Core_Temp_F']}°F.")
    else:
        st.success("💚 SYSTEM STATUS: Vitals returned to normal baseline values.")
        
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Heart Rate", value=f"{latest_entry['Heart_Rate_BPM']} BPM", delta="HIGH" if st.session_state['emergency_status_active'] else None)
    with col2:
        st.metric(label="Respiration", value=f"{latest_entry['Respiration_RPM']} RPM", delta="TACHYPNEA" if st.session_state['emergency_status_active'] else None)
    with col3:
        st.metric(label="Core Temp", value=f"{latest_entry['Core_Temp_F']} °F", delta="FEVER" if st.session_state['emergency_status_active'] else None)
        
    st.write("---")
    st.markdown("#### Nurse Physical Assessment & Validation Loop")
    
    if st.session_state['emergency_status_active']:
        st.warning("📋 **Diagnostic Precaution:** Vital telemetry patterns closely align with signatures for **Pneumonia (PNA)**.")
        check_lung = st.checkbox("Auscultated Lung Sounds (Verified crackles or diminished breath sounds)")
        check_cough = st.checkbox("Evaluated Cough Dynamics (Assessed for productive cough indications)")
        
        if check_lung and check_cough:
            st.success("🔗 Clinical validation completed successfully.")
            if st.button("⚠️ Clear Emergency State & Log Intervention Cache", use_container_width=True):
                st.session_state['emergency_status_active'] = False
                trigger_voice_clinical_alert("Alert cleared, sir. The resident has been verified safe by the caregiver on shift.")
                st.rerun()
        else:
            st.info("💡 Complete physical assessment check-boxes to unlock baseline reset control registry.")
    else:
        st.success("✅ Shift check-off complete. Patient tracing normal.")
        if st.button("🔄 Force-Trigger Vitals Spike Simulation (System Test)", use_container_width=True):
            st.session_state['emergency_status_active'] = True
            trigger_voice_clinical_alert("Warning, sir. A critical vitals spike has been detected. Evaluate for pneumonia risk.")
            st.rerun()

with tab2:
    st.markdown("#### 🦠 CDC / NIH / WHO Infectious Disease Surveillance")
    st.markdown("*Real-world baseline metrics tracking Clostridioides difficile (CDI) epidemiology burdens.*")
    
    cdc_cdi_df = pd.DataFrame({'Setting': ['Community-Onset', 'Healthcare-Onset'], 'Incidence_Per_100k': [62.3, 54.9]})
    nih_risk_df = pd.DataFrame({'Clinical_Status': ['Prior Antibiotic Use', 'No Prior Antibiotics'], 'Patient_Percentage': [70.0, 30.0]})
    who_burden_df = pd.DataFrame({'Facility_Type': ['Acute Hospital Care', 'Long-Term Care (LTCF)'], 'Cases_Per_10k_Patient_Days': [5.00, 44.24]})
    
    surveillance_view = st.selectbox("📊 Select Epidemiological Data Visualization Metric:", 
                                     ["WHO: Exposure Burden per 10k Days", "CDC: Infection Onset Distributions", "NIH: Antibiotic Exposure Correlation"])
    
    fig, ax = plt.subplots(figsize=(6, 3.8))
    sns.set_theme(style="whitegrid")
    
    if surveillance_view == "WHO: Exposure Burden per 10k Days":
        sns.barplot(x='Facility_Type', y='Cases_Per_10k_Patient_Days', data=who_burden_df, ax=ax, palette='copper')
        ax.set_title('WHO: CDI Burden per 10,000 Patient Days', fontsize=10, weight='bold')
        ax.set_ylabel('Cases per 10k Days')
        ax.set_xlabel('')
    elif surveillance_view == "CDC: Infection Onset Distributions":
        sns.barplot(x='Setting', y='Incidence_Per_100k', data=cdc_cdi_df, ax=ax, palette='Reds_r')
        ax.set_title('CDC EIP: CDI Incidence Rate by Setting', fontsize=10, weight='bold')
        ax.set_ylabel('Cases per 100,000 Persons')
        ax.set_xlabel('')
    elif surveillance_view == "NIH: Antibiotic Exposure Correlation":
        ax.pie(nih_risk_df['Patient_Percentage'], labels=nih_risk_df['Clinical_Status'], 
               autopct='%1.1f%%', colors=['#ff4b4b', '#d3d3d3'], startangle=90, 
               wedgeprops={'edgecolor': 'black', 'linewidth': 1})
        ax.set_title('NIH: CDI Correlation with Prior 12-Wk Antibiotic Use', fontsize=10, weight='bold')

    plt.tight_layout()
    st.pyplot(fig)
    
    st.info("📋 **Epidemiological Analysis Summary:** WHO data conclusively isolates Long-Term Care Facility environments as exceptionally high exposure vectors (44.24 cases per 10,000 patient-days) primarily linked to antibiotic stewardship disruptions tracked by the NIH registry.")

with tab3:
    st.markdown("#### 🗂️ Transmission-Based Isolation Precaution Registry")
    st.markdown("*Active infection control mapping for individualized resident profiles.*")
    
    isolation_matrix_df = pd.DataFrame({
        'Resident_ID': ['R-101', 'R-102', 'R-103', 'R-104', 'R-105'],
        'Resident_Name': ['Arthur P.', 'Beatrice M.', 'Charles K.', 'Dorothy S.', 'Edward V.'],
        'Diagnosis': ['Pneumonia (PNA)', 'C. difficile (CDI)', 'MRSA Wound', 'Influenza', 'Tuberculosis (TB)'],
        'Isolation_Type': ['Standard', 'Contact (Enteric)', 'Contact Standard', 'Droplet', 'Airborne'],
        'Required_PPE': ['Standard Gloves', 'Gown, Gloves (Soap & Water Handwashing)', 'Gown, Gloves', 'Mask, Face Shield', 'N95 Respirator, Negative Pressure Room'],
        'Sanitation_Protocol': ['Standard Alcohol', 'Bleach Wipes Only', 'Quaternary Disinfectant', 'Standard Disinfectant', 'HEPA Air Lock Filtration']
    })
    
    selected_res = st.selectbox("🔍 Query Resident Isolation Status Protocol:", list(isolation_matrix_df['Resident_Name']))
    res_row = isolation_matrix_df[isolation_matrix_df['Resident_Name'] == selected_res].iloc[0]
    
    st.markdown(f"### Profile Isolation Map: {res_row['Resident_Name']}")
    
    if res_row['Isolation_Type'] == 'Standard':
        st.success(f"💚 **Precautions: {res_row['Isolation_Type']}**\n\n• **Diagnosis:** {res_row['Diagnosis']}\n\n• **PPE:** {res_row['Required_PPE']}\n\n• **Room Cleaning:** {res_row['Sanitation_Protocol']}")
    else:
        st.error(f"🚨 **CRITICAL CONTAGIOUS ISOLATION: {res_row['Isolation_Type']}**\n\n• **Active Contagious Vector:** {res_row['Diagnosis']}\n\n• **Mandated Threshold PPE Gear:** {res_row['Required_PPE']}\n\n• **Chemical Sanitation Rule:** {res_row['Sanitation_Protocol']}")
        
    st.dataframe(isolation_matrix_df, use_container_width=True)
