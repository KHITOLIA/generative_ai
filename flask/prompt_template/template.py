from langchain_classic.prompts import PromptTemplate

def prompt_template():

    email_prompt = PromptTemplate(
        template = '''
    You are an expert professional career assistant and recruiter communication specialist.

    Your task is to draft a highly professional, concise, personalized cold outreach email for a job application.

    The email should:
    - Sound human and authentic
    - Be concise (150-250 words maximum)
    - Avoid generic AI-sounding language
    - Highlight relevant skills matching the JD
    - Mention 1-2 strong relevant projects or experiences
    - Show genuine interest in the role/company
    - Include a strong but polite CTA
    - Maintain professional tone
    - Avoid excessive flattery
    - Avoid buzzword stuffing
    - Be optimized for recruiter readability
    - do not write any subject for this email just give me the body (content) .

    Candidate Information:
    ----------------------
    Candidate Name: {candidate_name}

    Skills:
    {candidate_skills}

    Experience:
    {candidate_experience} years

    Projects:
    {candidate_projects}


    Target Role:
    -------------
    {target_role}
    
    Company:
    ---------
    {company_name}

    Job Description:
    ----------------
    {job_description}

    Now generate:
    1. A strong email subject line
    2. A personalized cold outreach email

    Formatting Rules:
    -----------------
    - Keep paragraphs short
    - No markdown
    - No bullet points
    - Professional email format
    - Mention resume attachment naturally
    - End with a professional signature


    Output Format:
    Dear Hiring Team,
    .....

   provide only the email body.
   Do not generate subject line.
   Do not generate Regards section.
   Do not provide these things as well
    Tushar Khitoliya 
    Phone: +91 7827458285 
    Email: tushar.khitoliya26@gmail.com   ''',
        input_variables = [
            "candidate_name",
            "candidate_skills",
            "candidate_experience",
            "candidate_projects",
            "target_role",
            "company_name",
            "job_description",

        ]
    )
    return email_prompt