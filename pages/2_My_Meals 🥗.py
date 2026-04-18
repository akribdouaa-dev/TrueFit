import streamlit as st
import json
from utils.styles import apply_styles

apply_styles()

st.markdown("<h1 style='color: #BDC4D4;'>My Meals 🍽️</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #52677D;'>Track your daily meals</p>", unsafe_allow_html=True)
st.markdown("---")

with open("data/products.json", "r") as f:
    products = json.load(f)

product_names = [p["name"] for p in products]

col1, col2 = st.columns(2)

with col1:
    selected_product = st.selectbox("Select Product", product_names)

with col2:
    quantity = st.number_input("Quantity (g)", min_value=1, max_value=1000, value=100)

if st.button("Add to Meals ➕"):
    product = next(p for p in products if p["name"] == selected_product)
    
    calories = (product["calories"] * quantity) / 100
    protein = (product["protein"] * quantity) / 100
    carbs = (product["carbs"] * quantity) / 100
    fats = (product["fats"] * quantity) / 100
    
    if "meals" not in st.session_state:
        st.session_state.meals = []
    
    st.session_state.meals.append({
        "name": selected_product,
        "quantity": quantity,
        "calories": calories,
        "protein": protein,
        "carbs": carbs,
        "fats": fats
    })

    st.success(f"{selected_product} added! ✅")

    st.markdown("---")

if "meals" in st.session_state and len(st.session_state.meals) > 0:
    st.markdown("<h3 style='color: #BDC4D4;'>Today's Meals 🍽️</h3>", unsafe_allow_html=True)
    
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fats = 0

    for meal in st.session_state.meals:
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.markdown(f"<p style='color: #BDC4D4;'>{meal['name']}</p>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<p style='color: #52677D;'>{meal['quantity']}g</p>", unsafe_allow_html=True)
        with col3:
            st.markdown(f"<p style='color: #52677D;'>{meal['calories']:.0f} kcal</p>", unsafe_allow_html=True)
        with col4:
            st.markdown(f"<p style='color: #52677D;'>P: {meal['protein']:.0f}g</p>", unsafe_allow_html=True)
        with col5:
            st.markdown(f"<p style='color: #52677D;'>C: {meal['carbs']:.0f}g F: {meal['fats']:.0f}g</p>", unsafe_allow_html=True)

        total_calories += meal['calories']
        total_protein += meal['protein']
        total_carbs += meal['carbs']
        total_fats += meal['fats']

    st.markdown("---")
    st.markdown("<h3 style='color: #BDC4D4;'>Daily Total 📊</h3>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Calories", f"{total_calories:.0f} kcal")
    with col2:
        st.metric("Protein", f"{total_protein:.0f}g")
    with col3:
        st.metric("Carbs", f"{total_carbs:.0f}g")
    with col4:
        st.metric("Fats", f"{total_fats:.0f}g")
else:
    st.markdown("<p style='color: #52677D;'>No meals added yet. Start by adding a meal above! 🍽️</p>", unsafe_allow_html=True)
    