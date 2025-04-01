import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
participants_file = "C:/Users/ayomi/Desktop/VBS/Participants (Responses).xlsx"
volunteers_file = "C:/Users/ayomi/Desktop/VBS/_VBS 2025 Volunteer's Registration Form (Responses).xlsx"

participants_df = pd.read_excel(participants_file, header=0)
volunteers_df = pd.read_excel(volunteers_file, header=0)

# Clean column names
participants_df.columns = participants_df.columns.str.strip()
volunteers_df.columns = volunteers_df.columns.str.strip()

# Debugging: Print column names
#st.write("Columns in Participants DataFrame:", participants_df.columns)
#st.write("Columns in Volunteers DataFrame:", volunteers_df.columns)

# Ensure 'Age' column exists
if 'Age' in participants_df.columns:
    # Age Group Distribution
    age_bins = [3, 5, 7, 9, 12, 17]
    age_labels = ['3-5', '6-7', '8-9', '10-12', '13-17']
    participants_df['Age Group'] = pd.cut(participants_df['Age'], bins=age_bins, labels=age_labels, right=True)
    age_counts = participants_df['Age Group'].value_counts().sort_index()
else:
    age_counts = pd.Series()

# Streamlit App
st.title("VBS 2025 Data Analysis")

# Create tabs
tab1, tab2 = st.tabs(["Participants Analysis", "Volunteers Analysis"])

with tab1:
    st.header("Participants Analysis")

    # Age Group Distribution
    st.subheader("Age Group Distribution")
    st.bar_chart(age_counts)

    # Name of Church Analysis
    if 'Name of Church' in participants_df.columns:
        st.subheader("Church Distribution")
        church_counts = participants_df['Name of Church'].value_counts()
        st.bar_chart(church_counts)

    # Medical Condition/Allergy Overview
    if 'Please state any Medical Condition or Allergy' in participants_df.columns:
        st.subheader("Medical Conditions / Allergies")
        medical_counts = participants_df['Please state any Medical Condition or Allergy'].value_counts()
        st.bar_chart(medical_counts)
        st.write(participants_df[['First Name', 'Surname', 'Please state any Medical Condition or Allergy']].dropna())

    # Sex Distribution
    if 'Sex' in participants_df.columns:
        st.subheader("Gender Distribution")
        gender_counts = participants_df['Sex'].value_counts()
        st.bar_chart(gender_counts)

    # Excursion Preference
    if 'Will you like to go on the Excursion during VBS?' in participants_df.columns:
        st.subheader("Excursion Preference")
        excursion_counts = participants_df['Will you like to go on the Excursion during VBS?'].value_counts()
        st.bar_chart(excursion_counts)

with tab2:
    st.header("Volunteers Analysis")
    if {'First Name', 'Surname', 'Department / Class Kindly indicate the class / department you would like to volunteer in.'}.issubset(volunteers_df.columns):
        # Volunteer Department Distribution
        st.subheader("Volunteer Department Distribution")
        volunteer_counts = volunteers_df['Department / Class Kindly indicate the class / department you would like to volunteer in.'].value_counts()
        st.bar_chart(volunteer_counts)
        st.write(volunteers_df[['First Name', 'Surname', 'Department / Class Kindly indicate the class / department you would like to volunteer in.']])
        
        # Volunteer Count per Department
        st.subheader("Number of Volunteers per Department")
        fig, ax = plt.subplots()
        volunteer_counts.plot(kind='bar', ax=ax, color='skyblue')
        ax.set_ylabel("Number of Volunteers")
        ax.set_xlabel("Department / Class")
        ax.set_title("Volunteers per Department")
        st.pyplot(fig)

        # Display Volunteers List
        st.subheader("List of Volunteers")
        st.dataframe(volunteers_df[['First Name', 'Surname', 'Department / Class Kindly indicate the class / department you would like to volunteer in.']])