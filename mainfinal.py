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

driver=webdriver.Chrome()
keyword=input("what is the job keyword")
location=input("where you want your job")
a=finder_indeed(keyword,location)
salary=int(input("expected salary"))
b=filter_indeed(a,salary)

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By





# Create a webdriver instance (e.g., using Chrome)
driver = webdriver.Chrome()

# Navigate to the Indeed job search page

driver.get(b)



from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

# Create a webdriver instance (e.g., using Chrome)


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


for title in job_title:
    print(title.text.strip())
for name in company_name:
    print(name.text.strip())
for salary in salary:
    print(salary.text.strip())

driver.close()
