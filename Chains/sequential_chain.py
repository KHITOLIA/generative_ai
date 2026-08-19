from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-120b" ,
    task = "text-generation",
    temperature = 0,
    max_new_tokens = 1000
)
model = ChatHuggingFace(llm = llm)
parser = StrOutputParser()

template1 = PromptTemplate(
    template = '''generate a detailed report on the {topic}''',
    input_variables = ['topic']
)

template2 = PromptTemplate(
    template = '''generate me 5 points about the summary from the following {text}''',
    input_variables = ['text']
)

chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({"topic" : "Attention is all you need research paper"})
print(result)

print()
print()
chain.get_graph().print_ascii()
