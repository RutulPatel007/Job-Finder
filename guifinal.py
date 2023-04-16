import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Set page title and icon
st.set_page_config(page_title="Job Finder", page_icon=":money_mouth_face:", layout="wide")

# Page 1: Input Form
st.markdown('<h1 style="text-align: center; color:#ffffff;">JOB FINDER</h1>', unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center; color: #ffffff;">One stop solution to find your next job</h2>', unsafe_allow_html=True)

def load(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie_coding=load("https://assets9.lottiefiles.com/packages/lf20_3rwasyjy.json")

st.container()
st_lottie(lottie_coding, height=300, key="job")

# Set input boxes to smaller size and center align
st.markdown('<style>input[type="text"]{height: 35px; width: 200px; font-size: 16px; text-align: left;}</style>', unsafe_allow_html=True)
st.markdown('<style>div[role="combobox"] > div > input{text-align: center; margin: 0 auto;}</style>', unsafe_allow_html=True)

# Input box for job keyword
job_keyword = st.text_input("Job Keyword")

# Input box for job location
job_location = st.text_input("Job Location")

# Dropdown for years of experience
years_of_experience = st.selectbox("Years of Experience", options=list(range(1, 11)))

# Next button to navigate to next page
if st.button("Next"):
    # Perform actions after clicking Next button
    # Add your code logic here
    st.write("Next button clicked!")
    # Add code to navigate to next page or perform other actions
    st.experimental_show("page2") # Show Page 2
    # Scroll to the results section
    st.experimental_scroll_to("page2")

# Logos of companies
st.markdown('<h3 style="text-align: center; color: #ffffff;">Data taken from:</h3>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.image("naukrilogo.png", width=250)
    st.markdown('<p style="text-align: center; color: #ffffff;">www.naukri.com</p>', unsafe_allow_html=True)
with col2:
    st.image("indeed.png", width=250)
    st.markdown('<p style="text-align: center; color: #ffffff;">www.indeed.com</p>', unsafe_allow_html=True)
with col3:
    st.image("foundit.png", width=250)
    st.markdown('<p style="text-align: center; color: #ffffff;">www.foundit.com</p>', unsafe_allow_html=True)

# Page 2: Result Page
st.experimental_show("page2")
st.markdown('<h1 style="text-align: center; color:#ffffff;">RESULTS</h1>', unsafe_allow_html=True)
