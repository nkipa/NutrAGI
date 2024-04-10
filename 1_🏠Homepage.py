import streamlit as st
import pandas as pd
from io import StringIO





# Streamlit page config
st.set_page_config(page_title="NutrAGI - Nutritional Assistant", page_icon="🧊", layout="wide", initial_sidebar_state="expanded")
st.markdown("<h1 style='text-align: center; color: Black;'>NutrAGI </br> Nutritional Assistant</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: Black; '>Meal Suggestion and Tracking App</h3>", unsafe_allow_html=True)

st.sidebar.success("Choose What you want to do now:")
with st.sidebar.container():
   
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
    
    action = st.radio(
        "d", 
        ["Track your nutrients.", "Get a suggestion for your next meal.", "Analyse your nutrition information."],
        index=None,
        label_visibility="collapsed"
            )
        
    if action == "Track your nutrients.":
        st.switch_page('pages/2_🖲️Track.py')
    elif action == "Get a suggestion for your next meal.":
        st.switch_page("pages/3_💡Suggest.py")
    elif action == "Analyse your nutrition information.":
        st.switch_page("pages/4_⚒️Analyse.py")



