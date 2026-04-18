import streamlit as st
import json
from utils.styles import apply_styles

apply_styles()

st.markdown("<h1 style='color: #BDC4D4;'>Workouts 💪</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #52677D;'>Exercise library & daily tracking</p>", unsafe_allow_html=True)
st.markdown("---")

with open("data/workouts.json", "r") as f:
    workouts = json.load(f)

# فلترة حسب مستوى الصعوبة
difficulty = st.selectbox("Filter by Difficulty", ["All", "Beginner", "Intermediate", "Advanced"])

if difficulty != "All":
    filtered = [w for w in workouts if w["difficulty"] == difficulty]
else:
    filtered = workouts

st.markdown("---")

# عرض التمارين
for workout in filtered:
    with st.expander(f"{workout['name']} — {workout['muscle']}"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"<p style='color: #BDC4D4;'><b>Difficulty:</b> {workout['difficulty']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: #BDC4D4;'><b>Equipment:</b> {workout['equipment']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: #52677D;'>{workout['description']}</p>", unsafe_allow_html=True)

        st.markdown("---")
st.markdown("<h3 style='color: #BDC4D4;'>Daily Workout Log 📝</h3>", unsafe_allow_html=True)

workout_names = [w["name"] for w in workouts]

col1, col2, col3 = st.columns(3)

with col1:
    selected_workout = st.selectbox("Exercise", workout_names)
with col2:
    sets = st.number_input("Sets", min_value=1, max_value=20, value=3)
with col3:
    reps = st.number_input("Reps", min_value=1, max_value=100, value=10)

if st.button("Log Workout ➕"):
    if "workout_log" not in st.session_state:
        st.session_state.workout_log = []
    
    st.session_state.workout_log.append({
        "name": selected_workout,
        "sets": sets,
        "reps": reps
    })
    st.success(f"{selected_workout} logged! ✅")

if "workout_log" in st.session_state and len(st.session_state.workout_log) > 0:
    st.markdown("---")
    st.markdown("<h3 style='color: #BDC4D4;'>Today's Exercises 🏋️</h3>", unsafe_allow_html=True)
    
    for log in st.session_state.workout_log:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"<p style='color: #BDC4D4;'>{log['name']}</p>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<p style='color: #52677D;'>{log['sets']} sets</p>", unsafe_allow_html=True)
        with col3:
            st.markdown(f"<p style='color: #52677D;'>{log['reps']} reps</p>", unsafe_allow_html=True)
            
