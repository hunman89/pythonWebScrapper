from flask import Flask, render_template,request,redirect,send_file
from util import find_job_by_provider, rap_data
from file import save_to_file

app = Flask("Job Scrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    provider = request.args.get("provider")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        if provider in db[keyword]:
            jobs = db[keyword][provider]
        else:
            jobs = find_job_by_provider(provider, keyword)
            db[keyword] = rap_data(provider, jobs, db[keyword])
    else:
        jobs = find_job_by_provider(provider, keyword)
        db[keyword] = rap_data(provider, jobs, {})
    return render_template("search.html", keyword = keyword.capitalize(), jobs=jobs, provider=provider.capitalize())

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)
    
app.run("0.0.0.0")