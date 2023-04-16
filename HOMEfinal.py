import streamlit as st
from streamlit_lottie import st_lottie
import requests
from monster2 import monster

from resume_reader import compare_similarity
from jobdes import jobdes


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
year_of_experience=-1
# Dropdown for years of experience
years_of_experience = st.selectbox("Years of Experience", options=list(range(1, 11)))
k=0

from title_find_indeed import finder_indeed
from comp_scrap_indeed import company_indeed
from filter_indeed import filter_indeed

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
p=0;







# Collect input from user
remote_job = st.text_input('Do you want a remote job?(Yes/No)')

salary = st.text_input('What is your expected salary (in LPA)?')



# Show user input after "Next" button is clicked

st.write('Filter Your Jobs:')
st.write(f'Remote Job: {remote_job}')
st.write(f'Salary: {salary} LPA')



input_complete=False



while input_complete is False:
    # Check if input is empty
    if (job_keyword!= "" and job_location!="" and salary!=""):
        # Input is completed, set session state to True
        input_complete = True


    # Sleep for a short duration to avoid excessive looping
    time.sleep(0.5)

# Use input in Selenium and BeautifulSoup code
if input_complete:

    current=finder_indeed(job_keyword,job_location)
    current = filter_indeed(current, salary)
    # a=monster(job_keyword,job_location,3,salary,remote_job)

# Create a webdriver instance (e.g., using Chrome)
driver = webdriver.Chrome()

# Navigate to the Indeed job search page

driver.get(current)



from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By



# Navigate to the Indeed job search page
url = driver.current_url
driver.get(url)


# Get the HTML content of the dropdown menu
html = driver.page_source

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find the dropdown menu items (company list items)

job_title = soup.find_all('a', class_='jcs-JobTitle css-jspxzf eu4oa1w0')
company_name = soup.find_all('span', class_='companyName')
salary= soup.find_all('div', "metadata salary-snippet-container")
# Extract and print the text content of each company list item


def info():
    x=[job_title,company_name,salary]
    return x
# def monsterinfo():
#     return a


driver.close()

import streamlit as st
from PyPDF2 import PdfFileReader

k=""
# Create a Streamlit app
def app():
    st.title('Resume Upload')

    # File input widget for resume
    resume_file = st.file_uploader('Upload your resume (PDF)', type=['pdf'])

    # If resume file is uploaded
    if resume_file is not None:
        # Read PDF file
        pdf_reader = PdfFileReader(resume_file)
        num_pages = pdf_reader.numPages

        # Display number of pages in the PDF
        st.write(f'Number of pages in resume: {num_pages}')

        # Display PDF content
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text = page.extractText()
            k=text





# Run the Streamlit app
if __name__ == '__main__':
    app()

from streamlit_extras.switch_page_button import switch_page



# Next button to navigate to next page
if st.button("Next"):
    # Perform actions after clicking Next button
    # Add your code logic here

    st.write("Go To Results Page To See The Jobs")
    switch_page("Results")

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

#