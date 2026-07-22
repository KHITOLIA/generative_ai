from langchain_classic.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-120b" ,
    task = "text-generation",
    temperature = 0,
    max_new_tokens = 1000
)
model = ChatHuggingFace(llm = llm)

template = PromptTemplate(
    template = '''Tell me some joke about {topic}''',
    input_variables = ['topic']
)
prompt = template.invoke({"topic" : "Maths"})
result = model.invoke(prompt).content
print(result)