from openai_api import chat_bot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
def jobdes():
    ser_odj = Service("E:\chromedriver_win32\chromedriver.exe")
    driver = webdriver.Chrome(service=ser_odj)
    # Opening a URL
    driver.get("https://in.indeed.com/jobs?l=Bengaluru%2C+Karnataka&from=mobRdr&utm_source=%2Fm%2F&utm_medium=redir&utm_campaign=dt&vjk=5c90a9efeabd112a")
    driver.implicitly_wait(10)
    k = []
    for x in range(0,10):
        driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div/div/div[5]/div[1]/div[5]/div/ul/li["+str(x+1)+"]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2/a").click()
        driver.implicitly_wait(100)
        jobdes  = driver.find_element(By.CLASS_NAME, "jobsearch-jobDescriptionText").text.strip()
       
        k.extend(chat_bot(jobdes))
    return k;

