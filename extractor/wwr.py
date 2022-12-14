from requests import get
from bs4 import BeautifulSoup


def extract_wwr_jobs(keyword):
    base_url = 'https://weworkremotely.com/remote-jobs/search?utf8=✓&term='
    response = get(f'{base_url}{keyword}')

    if response.status_code != 200:
        print('request error')
    else:
        results = []
        soup = BeautifulSoup(response.text, 'html.parser')
        jobs = soup.find_all('section', class_='jobs')
        for job_sections in jobs:
            job_posts = job_sections.find_all('li')
            job_posts.pop(-1)
            for job_post in job_posts:
                anchors = job_post.find_all('a')
                anchor = anchors[1]
                link = anchor['href']
                region = ""
                company, kind, region = anchor.find_all('span',
                                                        class_='company')
                title = anchor.find('span', class_='title')
                job_data = {
                    'link':
                    f'https://weworkremotely.com{link}',
                    'company':
                    company.string.replace(",", " "),
                    'location':
                    region.string.replace(",", " ")
                    if region.string is not None else "",
                    'position':
                    title.string.replace(",", " ")
                }
                results.append(job_data)
        return results
