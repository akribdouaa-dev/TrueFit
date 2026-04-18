import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        .stApp {
            background-color: #FFFFFF;
        }
        [data-testid="stSidebar"] {
            background-color: #1C2E4A;
        }
        [data-testid="stSidebar"] * {
            color: #BDC4D4;
        }
        [data-testid="stMetricValue"] {
            color: #1C2E4A;
        }
        [data-testid="stMetricLabel"] {
            color: #52677D;
        }
        .stSelectbox > div > div {
            background-color: #D1CFC9;
            color: #1C2E4A;
        }
        .stNumberInput input {
            background-color: #D1CFC9 !important;
            color: #1C2E4A !important;
        }
        input {
            background-color: #D1CFC9 !important;
            color: #1C2E4A !important;
        }
        .stExpander {
            background-color: #D1CFC9 !important;
            border: 1px solid #52677D !important;
        }
        .stExpander summary {
            color: #1C2E4A !important;
        }
        .stExpander p {
            color: #52677D !important;
        }
        </style>
    """, unsafe_allow_html=True)
    

    

