from extractor.indeed import extract_indeed_jobs
from extractor.wwr import extract_wwr_jobs
from extractor.rok import extract_rok_jobs

def find_job_by_provider(provider, keyword):
    jobs = []
    if provider == "weworkremotely":
        jobs = extract_wwr_jobs(keyword)
    if provider == "remoteok":
        jobs = extract_rok_jobs(keyword)
    if provider == "all":
        wwr = extract_wwr_jobs(keyword)
        rok = extract_rok_jobs(keyword)
        jobs = wwr + rok
    return jobs

def rap_data(provider, search_data, exist_data):
    data = exist_data
    data[provider] = search_data
    return data