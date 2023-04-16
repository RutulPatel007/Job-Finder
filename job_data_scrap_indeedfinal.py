from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

# Create a webdriver instance (e.g., using Chrome)
driver = webdriver.Chrome()

# Navigate to the Indeed job search page
url = "https://in.indeed.com/jobs?q=software+engineer+%E2%82%B96%2C50%2C000&l=banglore&sc=0kf%3Aattr%28DSQF7%29attr%28HFDVW%29%3B&vjk=b212f6bcd78e425a"
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
