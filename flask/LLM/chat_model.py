from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from prompt_template.template import prompt_template


load_dotenv()
def llm_model(candidate_name, candidate_skills, candidate_experience, candidate_projects, target_role, company_name, job_description, company_email):
    model = ChatOpenAI(model = 'gpt-5', temperature=0)
    prompt = prompt_template()
    chain = prompt | model 
    response = chain.invoke({"candidate_name" : candidate_name,
                                       "candidate_skills" : candidate_skills,
                                       "candidate_experience" : candidate_experience,
                                       "candidate_projects" : candidate_projects, 
                                       "target_role" : target_role,
                                       "company_name" : company_name,
                                       "job_description" : job_description,
                                       "company_email" : company_email})
    return response.content