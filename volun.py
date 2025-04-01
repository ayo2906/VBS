import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

volunteers_file = "C:/Users/ayomi/Desktop/VBS/_VBS 2025 Volunteer's Registration Form (Responses).xlsx"

volunteers_df = pd.read_excel(volunteers_file, header=0)

volunteers_df.columns = volunteers_df.columns.str.strip()

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