import streamlit as st
import plotly.graph_objects as go
from utils.styles import apply_styles
from utils.calculations import calculate_bmr, calculate_tdee, calculate_macros

apply_styles()

st.markdown("<h1 style='color: #1C2E4A;'>Calorie Tracker 🔥</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #52677D;'>Calculate your daily calories and macros</p>", unsafe_allow_html=True)
st.markdown("---")

# هل المستخدم حفظ بياناته في Profile؟
if "tdee" in st.session_state:
    st.success(f"Welcome back, {st.session_state.get('name', '')}! Here are your results 🎯")

    bmr = st.session_state.bmr
    tdee = st.session_state.tdee
    protein = st.session_state.protein
    carbs = st.session_state.carbs
    fats = st.session_state.fats

else:
    st.info("💡 Save your profile first for automatic results — or enter your details below manually.")

    col1, col2 = st.columns(2)
    with col1:
        gender = st.selectbox("Gender", ["Female", "Male"])
        age = st.number_input("Age", min_value=10, max_value=100, value=25)
        weight = st.number_input("Weight (kg)", min_value=30, max_value=300, value=60)
    with col2:
        height = st.number_input("Height (cm)", min_value=100, max_value=250, value=165)
        activity_level = st.selectbox("Activity Level", [
            "Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extra Active"
        ])

    if st.button("Calculate 💪"):
        bmr = calculate_bmr(gender, age, weight, height)
        tdee = calculate_tdee(bmr, activity_level)
        protein, carbs, fats = calculate_macros(tdee)
    else:
        st.stop()

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("BMR", f"{bmr:.0f} kcal")
with col2:
    st.metric("TDEE", f"{tdee:.0f} kcal")
with col3:
    st.metric("Protein", f"{protein:.0f}g")
with col4:
    st.metric("Carbs / Fats", f"{carbs:.0f}g / {fats:.0f}g")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    fig_pie = go.Figure(data=[go.Pie(
        labels=["Protein", "Carbs", "Fats"],
        values=[protein, carbs, fats],
        hole=0.5,
        marker=dict(colors=["#52677D", "#BDC4D4", "#1C2E4A"])
    )])
    fig_pie.update_layout(
        paper_bgcolor="#0F1A2B",
        plot_bgcolor="#0F1A2B",
        font=dict(color="#1C2E4A"),
        title=dict(text="Macros Distribution", font=dict(color="#1C2E4A")),
        legend=dict(font=dict(color="#1C2E4A"))
    )
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    fig_bar = go.Figure(data=[go.Bar(
        x=["Protein", "Carbs", "Fats"],
        y=[protein * 4, carbs * 4, fats * 9],
        marker_color=["#52677D", "#BDC4D4", "#1C2E4A"]
    )])
    fig_bar.update_layout(
        paper_bgcolor="#0F1A2B",
        plot_bgcolor="#0F1A2B",
        font=dict(color="#BDC4D4"),
        title=dict(text="Calories per Macro", font=dict(color="#BDC4D4")),
        xaxis=dict(color="#BDC4D4"),
        yaxis=dict(color="#BDC4D4")
    )
    st.plotly_chart(fig_bar, use_container_width=True)
    

    

        


