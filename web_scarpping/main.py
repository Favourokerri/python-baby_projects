from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
    date = job.find('span', class_ = 'sim-posted').text
    if 'few' in date:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
        skill = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
        print(f"company name: {company_name.strip()}")
        print(f"skills: {skill.strip()}")
        print(f"posted: {date.strip()}")
        print("")