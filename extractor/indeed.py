from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def extract_indeed_jobs(keyword):
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')    
    browser = webdriver.Chrome(options=options)
    pages = pagenation(browser, keyword)
    results = []
    for page in range(pages):
        get_jobs(browser, keyword, page, results)
    return results
    
def pagenation(browser, keyword):
    browser.get(f'https://kr.indeed.com/jobs?q={keyword}')    
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    pagination = soup.find('ul', class_='pagination-list')
    if pagination == None:
        return 1
    pages = pagination.find_all('li', reculsive=False)
    count = len(pages)
    if count >= 5:
        return 5
    return count

def get_jobs(browser, keyword, page, results):    
    browser.get(f'https://kr.indeed.com/jobs?q={keyword}&start={page*10}')    
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    job_list = soup.find('ul', class_='jobsearch-ResultsList')
    jobs = job_list.find_all('li', recursive=False)    
    
    for job in jobs:
        zone = job.find('div', class_='mosaic-zone')
        if zone == None:
            anchor = job.select_one('h2 a')
            link = anchor['href']
            title = anchor['aria-label']
            company = job.find('span', class_='companyName')
            location = job.find('div', class_='companyLocation')
            job_data = {
                        'link' : f'https://kr.indeed.com{link}',
                        'company' : company.string.replace(",", " "),
                        'location' : location.string.replace(",", " "),
                        'title' : title.replace(",", " ")
                    }
            results.append(job_data)
