import streamlit as st
from utils.styles import apply_styles

st.set_page_config(
    page_title="TrueFit",
    page_icon="assets/truefit_logo.png",
    layout="wide"
)

apply_styles()

st.image("assets/background.png", width=150)

st.markdown("""
    <style>
    .stApp {
        background-color: #0F1A2B;
    } [data-testid="stSidebar"] { background-color : #1C2E4A;} [data-testid="stSidebar"]*{color : #BDC4D4;} 
    </style>
""", unsafe_allow_html=True)
st.markdown("""
    <style>
    .stApp {
        background-color: #0F1A2B;
    }
    [data-testid="stSidebar"] {
        background-color: #1C2E4A;
    }
    [data-testid="stSidebar"] * {
        color: #BDC4D4;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <h1 style='color: #BDC4D4;'>Welcome to TrueFit 💪</h1>
    <p style='color: #52677D; font-size: 18px;'>Your fitness journey starts here.</p>
""", unsafe_allow_html=True)
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div style='background-color: #1C2E4A; padding: 20px; border-radius: 10px; text-align: center;'>
            <h3 style='color: #BDC4D4;'>🔥 Calorie Tracker</h3>
            <p style='color: #52677D;'>Track your daily calories</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style='background-color: #1C2E4A; padding: 20px; border-radius: 10px; text-align: center;'>
            <h3 style='color: #BDC4D4;'>🍽️ My Meals</h3>
            <p style='color: #52677D;'>Log your daily meals</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div style='background-color: #1C2E4A; padding: 20px; border-radius: 10px; text-align: center;'>
            <h3 style='color: #BDC4D4;'>💪 Workouts</h3>
            <p style='color: #52677D;'>Track your workouts</p>
        </div>
    """, unsafe_allow_html=True)
    

    




