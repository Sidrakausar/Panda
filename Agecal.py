import streamlit as st
from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

st.title("Age Calculator")

birth_date = st.date_input("Enter your birth date")

if st.button("Calculate Age"):
    if birth_date:
        age = calculate_age(birth_date)
        st.success(f"Your age is {age} years old.")
    else:
        st.warning("Please enter a valid birth date.")
