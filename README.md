# Job-Finder
Job Finder is a Python-based automation tool that helps job seekers to find job postings from three major job portals: Indeed, Monster, and Naukri.com. This tool uses Selenium automation and web scraping techniques to extract job details like job title, company name, job location, and job description from the job portals. The extracted data is then presented through a Streamlit-based frontend GUI.

## Requirements
Python 3.x

Selenium WebDriver for Python

BeautifulSoup4

ChromeDriver

Streamlit

## Installation

### Clone the repository

git clone https://github.com/RutulPatel007/Job-Finder.git
  
### Install the required libraries

pip install -r requirements.txt

Download the ChromeDriver executable from here and place it in the job-finder directory.
  
### Usage
Open job_finder.py in any text editor of your choice.

Edit the search_terms list variable to add your preferred job titles and locations.

Copy code
search_terms = [    {'title': 'Software Developer', 'location': 'New York'},    {'title': 'Data Scientist', 'location': 'San Francisco'},    {'title': 'Product Manager', 'location': 'London'}]
  
Run job_finder.py to start the automation process.

Copy code

streamlit run job_finder.py

Wait for the tool to finish scraping job postings from the job portals.

After the tool finishes scraping, the Streamlit-based frontend GUI will open in your default web browser. Use the GUI to browse the job postings that were extracted by the tool.
