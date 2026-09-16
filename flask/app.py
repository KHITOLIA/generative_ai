from flask import Flask, request, render_template
from LLM.chat_model import llm_model
app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        candidate_name =  request.form['candidate_name']
        candidate_skills = request.form['candidate_skills']
        candidate_experience = float(request.form['candidate_experience'])
        candidate_projects = request.form['candidate_projects']
        target_role = request.form['target_role']
        company_name = request.form['company_name']
        job_description = request.form['job_description']
        company_email = request.form['company_email']
        result = llm_model(candidate_name, candidate_skills, candidate_experience, candidate_projects, target_role, company_name, job_description
                           ,company_email)
        return render_template("home.html", result = result)
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)