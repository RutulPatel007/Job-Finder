import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
from bs4 import BeautifulSoup


def filter_indeed(url,salary):
    serv_obj = Service("C:\drivers\chromedriver.exe")

    # Set the path to the ChromeDriver executable

    # Create a ChromeDriver instance
    driver = webdriver.Chrome(service=serv_obj)

    # Open a webpage
    driver.get(url)
    time.sleep(2)

    # Click on the drop-down button
    driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div/div/div[2]/div/div/div/div[2]/div/div[2]/button").click()

    # Wait for the "Remote" option to be clickable
    remote_option = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div[1]/div/div/div[2]/div/div/div/div[2]/div/div[2]/ul/li[1]/a")))

    # Click on the "Remote" option
    remote_option.click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/button").click()


    def get_integer_before_plus(string):

        # Find the index of '+' sign
        plus_index = string.find('+')

        # Extract the substring before the '+' sign
        integer_part = string[1:plus_index]

        # Convert the substring to an integer and return
        return float(integer_part.replace(",","").replace(" ",""))





    driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div/div/div[2]/div/div/div/div[2]/div/div[3]/button").click()

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    list_sal = soup.find('ul', class_='yosegi-FilterPill-dropdownList is-dropdownOpen')
    # Extract and print the text content of each company list item
    y=[]
    for item in list_sal:
        y.append(item.text.strip())
    m=[]
    # Close the webdriver
    for x in y:
        m.append(get_integer_before_plus(x))

    for z in range(0,len(m)):
        if int(salary)<m[z]:
            break
    driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div/div/div[2]/div/div/div/div[2]/div/div[3]/ul/li["+str(z+1)+"]/a").click()
    return driver.current_url
    driver.close()

    return driver.current_url


