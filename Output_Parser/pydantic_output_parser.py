from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_classic.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser, PydanticOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from pydantic import BaseModel, Field
from typing import List, Literal, Optional
from dotenv import load_dotenv
load_dotenv()
# model = ChatOpenAI(model = 'gpt-5.5', temperature = 0, max_completion_tokens = 500)

llm = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-120b" ,
    task = "text-generation",
    temperature = 0,
    max_new_tokens = 1000
)
model = ChatHuggingFace(llm = llm)

class Review(BaseModel):
    name : str = Field(description = "Name of the person from the movie")
    age : str = Field(description = "Actual age of the person from the movie")
    strength : str = Field(description = "How much strength that character have in the movie")
    location : str = Field(description = "Where is the location ")

parser = PydanticOutputParser(pydantic_object = Review)

template1 = PromptTemplate(
    template = '''Provide mt the detailed information about any character from the movie {movie} \n {format_instruction}''',
    input_variables = ['movie'],
    partial_variables = {"format_instruction" : parser.get_format_instructions()}
)

chain = template1 | model | parser
result = chain.invoke({"movie" : "Captain America Civil War"})
print(result.name, result.location)