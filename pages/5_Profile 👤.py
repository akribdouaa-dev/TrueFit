import streamlit as st
import json
import os
from utils.styles import apply_styles
from utils.calculations import calculate_bmr, calculate_tdee, calculate_macros

apply_styles()

PROFILE_PATH = "data/user_profile.json"

def load_profile():
    with open(PROFILE_PATH, "r") as f:
        data = json.load(f)
    return data

def save_profile(data):
    with open(PROFILE_PATH, "w") as f:
        json.dump(data, f)

# تحميل البيانات عند فتح الصفحة
profile = load_profile()

if profile:
    for key, value in profile.items():
        st.session_state[key] = value

st.markdown("<h1 style='color: #BDC4D4;'>Profile 👤</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #52677D;'>Your personal details</p>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Name", value=st.session_state.get("name", ""))
    gender = st.selectbox("Gender", ["Female", "Male"],
                index=0 if st.session_state.get("gender", "Female") == "Female" else 1)
    age = st.number_input("Age", min_value=10, max_value=100,
                value=int(st.session_state.get("age", 25)))
    weight = st.number_input("Weight (kg)", min_value=30, max_value=300,
                value=int(st.session_state.get("weight", 60)))

with col2:
    height = st.number_input("Height (cm)", min_value=100, max_value=250,
                value=int(st.session_state.get("height", 165)))
    activity_options = ["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extra Active"]
    activity_level = st.selectbox("Activity Level", activity_options,
                index=activity_options.index(st.session_state.get("activity_level", "Sedentary")))
    goal_options = ["Lose Weight", "Maintain", "Gain Muscle"]
    goal = st.selectbox("Goal", goal_options,
                index=goal_options.index(st.session_state.get("goal", "Maintain")))

st.markdown("---")

if st.button("Save Profile 💾"):
    bmr = calculate_bmr(gender, age, weight, height)
    tdee = calculate_tdee(bmr, activity_level)
    protein, carbs, fats = calculate_macros(tdee)

    profile_data = {
        "name": name,
        "gender": gender,
        "age": age,
        "weight": weight,
        "height": height,
        "activity_level": activity_level,
        "goal": goal,
        "bmr": bmr,
        "tdee": tdee,
        "protein": protein,
        "carbs": carbs,
        "fats": fats
    }

    save_profile(profile_data)
    st.session_state.update(profile_data)

    st.success(f"Profile saved permanently! Welcome, {name} 🎉")

    st.markdown("---")
    st.markdown("<h3 style='color: #BDC4D4;'>Your Daily Targets 🎯</h3>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("TDEE", f"{tdee:.0f} kcal")
    with col2:
        st.metric("Protein", f"{protein:.0f}g")
    with col3:
        st.metric("Carbs", f"{carbs:.0f}g")
    with col4:
        st.metric("Fats", f"{fats:.0f}g")
        

        