import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import math

# Opening the Chrome browser
ser_odj = Service("E:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_odj)
# Opening a URL
driver.get("https://www.foundit.in/")
driver.implicitly_wait(10)
driver.find_element(By.NAME, "fts").send_keys(input("keyword"))
driver.find_element(By.NAME, "lmy").send_keys(input("location"))
# driver.find_element(By.CLASS_NAME, "multiselect modal-ref-class").click()
# driver.find_element(By.CLASS_NAME, "multiselect_content-wrapper ac_results custom-v-scroll modal-ref-class").click()
driver.find_element(By.CLASS_NAME, "btn").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/ul/li[2]/button").click()
# time.sleep(5)
exp = int(input("exp"))
if exp>=0 and exp<=1:
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/ul/li[2]/div/div[1]/div[1]/div/div/label").click()
if exp>=1 and exp<=2:
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/ul/li[2]/div/div[1]/div[2]/div/div/label").click()
if exp >= 2 and exp <= 5:
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/ul/li[2]/div/div[1]/div[3]/div/div/label").click()
if exp >= 5 and exp <= 7:
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/ul/li[2]/div/div[1]/div[4]/div/div/label").click()
if exp >= 7 and exp <= 10:
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/ul/li[2]/div/div[1]/div[5]/div/div/label").click()
if exp>=10 and exp<=15:
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/ul/li[2]/div/div[1]/div[6]/div/div/label").click()
if exp>=15:
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/ul/li[2]/div/div[1]/div[7]/div/div/label").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/ul/li[2]/div/div[2]/button[2]").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/ul/li[3]/button").click()
salary = int(input("salary in lpa"))
if salary>=0 and salary<=1:
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/ul/li[3]/div/div[1]/div[1]/div/div/label/span[2]").click()
if salary>=1 and salary<=2:
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/ul/li[3]/div/div[1]/div[2]/div/div/label/span[2]").click()
if salary>=2 and salary<=5:
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/ul/li[3]/div/div[1]/div[3]/div/div/label/span[2]").click()
if salary>=5 and salary<=10:
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/ul/li[3]/div/div[1]/div[4]/div/div/label/span[2]").click()
if salary>=10 and salary<=20:
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/ul/li[3]/div/div[1]/div[5]/div/div/label/span[2]").click()
if salary>=20 and salary<=30:
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/ul/li[3]/div/div[1]/div[6]/div/div/label/span[2]").click()
if salary>=30 and salary<=50:
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/ul/li[3]/div/div[1]/div[7]/div/div/label/span[2]").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/ul/li[3]/div/div[2]/button[2]").click()
driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/ul/li[10]/button").click()
yn= input("Do you want company wise filter")
if yn=="yes":
    for x in range(10):
        company = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/ul/li[10]/div/div[2]/div["+str(x+1)+"]/div/div/label")
        print(str(x+1)+". "+company.text.strip())
    x=list(map(int,input("Enter respective number of company")))
    for i in x:
        driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/ul/li[10]/div/div[2]/div["+str(i)+"]/div/div/label").click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/ul/li[10]/div/div[3]/button[2]").click()

# /html/body/div[3]/div[1]/div[3]/ul/li[10]/div/div[2]/div[1]/div/div/label
# /html/body/div[3]/div[1]/div[3]/ul/li[10]/div/div[2]/div[2]/div/div/label
# /html/body/div[3]/div[1]/div[3]/ul/li[10]/div/div[2]/div[1]/div/div/label
# /html/body/div[3]/div[1]/div[3]/ul/li[10]/div/div[2]/div[2]/div/div/label

driver.get(driver.current_url)
soup = BeautifulSoup(driver.page_source, "html.parser")
jobs = soup.find_all("div", class_="jobTitle")
companies = soup.find_all("div", class_="companyName")
# salary = soup.find_all("div", class_="details")
for x in range(min(len(companies),len(jobs))):

    print(str(x+1)+". "+jobs[x].text.strip()+"  ||  "+companies[x].text.strip())
    driver.find_element(By.XPATH, "/html / body / div[3] / div[1] / div[4] / div[1] / div / div["+str(x+2)+"] / div / div / div[1] / div / div[1]").click()
    # driver.get(driver.current_url)
    # driver.implicitly_wait(20)
    # soup = BeautifulSoup(driver.page_source, "html.parser")
    skills = soup.find_all("div", class_="skillDesc")
    print("Required Skills Are:")
    for i in range(10):
        try:
            skill = driver.find_element(By.XPATH, "/ html / body / div[3] / div[1] / div[4] / div[2] / div / div[3] / div[3] / div / div[5] / div[2] / div["+str(i+1)+"]")
            print(skill.text.strip()+" | ",end="")
        except:
            break
    print()
    # for skill in skills:
    #     print(skill.text.strip()+" | ",end="")
    # print()
    # / html / body / div[3] / div[1] / div[4] / div[2] / div / div[3] / div[3] / div / div[5] / div[2] / div[1]
    # / html / body / div[3] / div[1] / div[4] / div[2] / div / div[3] / div[3] / div / div[5] / div[2] / div[1]
    # / html / body / div[3] / div[1] / div[4] / div[2] / div / div[3] / div[3] / div / div[5] / div[2] / div[2]
    print("Salary is : ",end="")
    sal = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[4]/div[2]/div/div[3]/div[1]/div[1]/div/div[3]/div[2]")
    print("₹"+sal.text)
    # print(salary[x].text.strip()+" | ",end="")
    # print()