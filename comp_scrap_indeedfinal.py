from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


def company_indeed(url):


    # Create a webdriver instance (e.g., using Chrome)
    driver = webdriver.Chrome()

    # Navigate to the Indeed job search page
    url = "https://in.indeed.com/jobs?q=software+engineer+%E2%82%B96%2C50%2C000&l=banglore&sc=0kf%3Aattr%28DSQF7%29attr%28HFDVW%29%3B&vjk=b212f6bcd78e425a"
    driver.get(url)

    # Find the Company dropdown button element
    button = driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div/div/div[2]/div/div/div/div[2]/div/div[6]/button/div[1]")

    # Click the Company dropdown button to open the dropdown menu
    button.click()

    # Get the HTML content of the dropdown menu
    html = driver.page_source

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Find the dropdown menu items (company list items)

    company_list_items =soup.find('ul', class_='yosegi-FilterPill-dropdownList is-dropdownOpen')
    # Extract and print the text content of each company list item
    y=[]
    for item in company_list_items:
        y.append(item.text.strip())

    print(y)

    # Close the webdriver
    driver.close()
    return y
