from extractor.indeed import extract_indeed_jobs
from extractor.wwr import extract_wwr_jobs

keyword = input("What do you search?")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobs = indeed + wwr

print(len(jobs))