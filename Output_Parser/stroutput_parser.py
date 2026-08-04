from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_classic.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-120b" ,
    task = "text-generation",
    temperature = 0,
    max_new_tokens = 1000
)
model = ChatHuggingFace(llm = llm)
# model = ChatOpenAI(model = "gpt-5.5", temperature = 0, max_completion_tokens = 1000)
parser = StrOutputParser()
template1 = PromptTemplate(
    template = '''Generate a detailed report on the {topic}''',
    input_variables = ['topic']
)

template2 = PromptTemplate(
    template = '''Generate the detailed summary about the {report}''',
    input_variables = ['report']
)
# prompt1 = template1.invoke({"topic" : "Who is bhagat singh?"})
# response1 = model.invoke(prompt1)
# prompt2 = template2.invoke({"report" :response1})
# response2 = model.invoke(prompt2)
chain = template1 | model | parser | template2 | model | parser
response = chain.invoke({"topic" : "What is machine learning ? "}) 
print(response)