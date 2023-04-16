import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# def naukri(keyword, location, experience):
# Opening the Chrome browser
ser_odj = Service("E:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_odj)
# Opening a URL
driver.get("https://www.naukri.com/")
driver.implicitly_wait(10)
# driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div/button").click()
driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/span").click()
driver.find_element(By.CSS_SELECTOR, "#root > div.qsbWrapper > div > div > div.keywordSugg > div > div > div > div:nth-child(1) > div > input").send_keys(input("keyword"))
driver.find_element(By.CSS_SELECTOR, "#root > div.qsbWrapper > div > div > div.qsbExperience > div > span").click()
experience = int(input("experience"))
driver.find_element(By.CSS_SELECTOR, "#sa-dd-scrollexpereinceDD > div:nth-child(1) > ul > li:nth-child("+str(experience+1)+")").click()
driver.find_element(By.CSS_SELECTOR, "#root > div.qsbWrapper > div > div > div.locationSugg > div > div > div > div:nth-child(1) > div > input").send_keys(input("location"))
driver.find_element(By.CSS_SELECTOR, "#root > div.qsbWrapper > div > div > div.qsbSubmit").click()

# current_url = driver.current_url
driver.get(driver.current_url)
final_list = []
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.implicitly_wait(20)
# jobtitles = soup.find_all("div", class_="info fleft")
# companynames = soup.find_all("div", class_="companyInfo subheading")
jobtitles =[]
companynames = []
salaries = []
# skills_list = []
for x in range(15):

    jobtitle = driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div/div/section[2]/div[2]/article["+str(x+1)+"]/div[1]/div[1]/a").text.strip()
    # /html/body/div[1]/div[4]/div/div/section[2]/div[2]/article[2]/div[1]/div[1]/a
    # /html/body/div[1]/div[4]/div/div/section[2]/div[2]/article[2]/div[1]/div[1]/div/a[1]
    # jobtitles.extend(jobtitle)
    compan = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/section[2]/div[2]/article["+str(x+1)+"]/div[1]/div[1]/div/a[1]").text.strip()
    # companynames.extend(compan)
    sala = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/section[2]/div[2]/article["+str(x+1)+"]/div[1]/ul/li[2]/span[1]").text.strip()
    # salaries.extend(sala)
    # / html / body / div[1] / div[4] / div / div / section[2] / div[2] / article[2] / div[1] / ul / li[2] / span[1]
    # / html / body / div[1] / div[4] / div / div / section[2] / div[2] / article[1] / ul / li[1]
    # / html / body / div[1] / div[4] / div / div / section[2] / div[2] / article[1] / ul / li[2]
    # / html / body / div[1] / div[4] / div / div / section[2] / div[2] / article[2] / ul / li[1]
    print(jobtitle + "  ||  " + compan)
    #
    print("Skills required are : ", end="")
    # skills = []
    for i in range(5):
        skill = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/section[2]/div[2]/article["+str(x+1)+"]/ul/li["+str(i+1)+"]")
        print(skill.text.strip()+" | ",end="")
        # skills.extend(skill.text.strip())
    # skills_list.extend(skills)
    print()
    print("Salary is : " + sala)
# final_list.extend(jobtitles)
# final_list.extend(companynames)
# final_list.extend(salaries)

driver.quit()
# return final_list
# print(naukri("Machine Learning", "Bangalore", 2))
# END OF PROGRAM
# for x in range(min(len(jobtitles),len(companynames))):
#     print(jobtitles[x]['title']+" || "+companynames[x].text.strip())
# yn = input("Type yes if you want company wise filter")

# if yn=="yes":
#     # url = "https://www.naukri.com/sofware-engineer-jobs?k=sofware%20engineer"
#     driver.get(driver.current_url)
#
#     # Wait for the page to load
#     time.sleep(5)
#     driver.find_element(By.ID, "qctopGroupId").click()
#
#     # element = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[11]/div[2]/a/span')
#     # driver.execute_script("arguments[0].scrollIntoView();", element)
#     # element.click()
#
#     # dropdown menu
#     WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH,
#                                                                            '/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[11]/div[3]/div[2]/div[2]/div/div[1]/div[3]/label/p/span[1]')))
#
#     # Parse the HTML content using BeautifulSoup
#     html = driver.page_source
#     soup = BeautifulSoup(html, "html.parser")
#
#     titles = []
#     # Find all job titles using the given XPath and wait for them to be visible
#     for x in range(1, 9):
#         tit = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH,
#                                                                                      '/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[11]/div[3]/div[2]/div[2]/div/div[1]/div[' + str(
#                                                                                          x) + ']/label/p/span[1]')))
#         titles.extend(tit)
#
#     # Print all job titles
#     for title in titles:
#         print(title.text)
    # element = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[11]/div[2]/a/span')
    # driver.execute_script("arguments[0].scrollIntoView();", element)
    # # element.click()
    # driver.implicitly_wait(10)
    # driver.find_element(By.ID, "qctopGroupId").click()
    #
    # # dropdown menu
    # # WebDriverWait(driver, 2).until(EC.visibility_of_all_elements_located((By.XPATH, '/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[11]/div[3]/div[2]/div[2]/div/div[1]/div[3]/label/p/span[1]')))
    #
    # # Parse the HTML content using BeautifulSoup
    # html = driver.page_source
    # soup = BeautifulSoup(html, "html.parser")
    # companies = []
    # for company in soup.find_all("span", {"class": "ellipsis fleft filterLabel"}):
    #     companies.append(company['title'])
    #
    # print(companies)
    # titles=[]
    # # Find all job titles using the given XPath and wait for them to be visible
    # for x in range(1,9):
    #     driver.implicitly_wait(10)
    #     # tit = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[11]/div[3]/div[2]/div[2]/div/div[1]/div['+str(x)+']/label/p/span[1]')
    #     tit = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[11]/div[3]/div[2]/div[2]/div/div[1]/div['+str(x)+']/label/p/span[1]')))
    #
    #     titles.extend(tit)
    #
    # # Print all job titles
    # count=1
    # for title in titles:
    #     print(str(count)+". " + title.text)
    #     count+=1
    # com = int(input("Enter the number of respective company"))
    # driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[11]/div[3]/div[2]/div[2]/div/div[1]/div["+str(com)+"]/label/p/span[1]").click()
    # time.sleep(10)
    # driver.find_element(By.CLASS_NAME, "filter-apply-btn").click()

# Close the webdriver

# driver.find_element(By.ID, "qctopGroupId").click()
# companies = soup.find_all("div" , class_="")
# for x in range(10):
#     # company=driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[11]/div[3]/div[2]/div[2]/div/div[1]/div["+str(x+1)+"]/label/p/span[1]").text.strip()
#     # print(company)
#     driver.get(driver.current_url)
#     company = driver.find_element(By.CSS_SELECTOR, "tooltip > div.expanded-filters-container > div.swiper-container.swiperType.swiper-container-initialized.swiper-container-horizontal > div > div.swiper-slide.swiper-slide-active > div:nth-child("+str(x+1)+") > label > p > span.ellipsis.fleft.filterLabel")
#     print(company.text.strip())
    # tooltip > div.expanded-filters-container > div.swiper-container.swiperType.swiper-container-initialized.swiper-container-horizontal > div > div.swiper-slide.swiper-slide-active > div:nth-child(3) > label > p > span.ellipsis.fleft.filterLabel
# /html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[11]/div[3]/div[2]/div[2]/div/div[1]/div[1]/label/p/span[1]
# /html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[11]/div[3]/div[2]/div[2]/div/div[1]/div[2]/label/p/span[1]
# top_companies = soup.find_all("span", class_="fw500")
# for l in top_companies:
#     if l.text=="Top companies":
#         tc = soup.find_all("span", class_="ellipsis fleft filterLabel", )
#         for eke in tc:
#             print(eke['title'])

# job_listings = soup.find_all(class_='jobTuple')
# for job in job_listings:
#     company_elem = job.find(class_='companyName')
#     if company_elem is not None:
#         company = company_elem.text.strip()
#         print(company)


# https://www.naukri.com/machine-learing-jobs-in-remote?k=machine%20learing&l=remote&experience=2
# import requests
# from bs4 import BeautifulSoup
#
# url = "https://www.naukri.com/machine-learning-jobs-in-remote?k=machine%20learning&l=remote&nignbevent_src=jobsearchDeskGNB&experience=2"
# page = requests.get(url)
#
# soup = BeautifulSoup(page.content, "html.parser")
#
# jobs = soup.find_all("div", class_="jobTupleHeader")
#
# for job in jobs:
#     job_title = job.find("a", class_="title ellipsis").text.strip()
#     print(job_title)
# element = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[11]/div[2]/a/span')
# driver.execute_script("arguments[0].scrollIntoView();", element)
# element.click()
#
# # dropdown menu
# WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[11]/div[3]/div[2]/div[2]/div/div[1]/div[3]/label/p/span[1]')))
#
# # Parse the HTML content using BeautifulSoup
# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")
#
# titles=[]
# # Find all job titles using the given XPath and wait for them to be visible
# for x in range(1,9):
#     tit = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '/html/body/div[1]/div[4]/div/div/section[1]/div[2]/div[11]/div[3]/div[2]/div[2]/div/div[1]/div['+str(x)+']/label/p/span[1]')))
#     titles.extend(tit)
#
# # Print all job titles
# for title in titles:
#     print(title.text)


