import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Create a webdriver instance (e.g., using Chrome)
driver = webdriver.Chrome()

# Navigate to the Indeed job search page
url = "https://www.foundit.in/srp/results?query=software+engineer&searchId=4af3bc80-d45c-47b0-a4a8-d63e7bbb8d75"
driver.get(url)

# Wait for the page to load


element = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[11]/div[2]/a/span')
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()

# dropdown menu
WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[11]/div[3]/div[2]/div[2]/div/div[1]/div[3]/label/p/span[1]')))

# Parse the HTML content using BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

titles=[]
# Find all job titles using the given XPath and wait for them to be visible
for x in range(1,9):
    tit = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[11]/div[3]/div[2]/div[2]/div/div[1]/div['+str(x)+']/label/p/span[1]')))
    titles.extend(tit)

# Print all job titles
for title in titles:
    print(title.text)

# Close the webdriver
driver.quit()
