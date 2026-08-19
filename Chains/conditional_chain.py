from pydantic import BaseModel, Field
from typing import Literal, Optional
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch, RunnableLambda
from dotenv import load_dotenv
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id = "openai/gpt-oss-120b" ,
    task = "text-generation",
    temperature = 0,
    max_new_tokens = 1000
)
model = ChatHuggingFace(llm = llm)
class Feedback(BaseModel):
    sentiment : Literal["positive", "negative"] = Field(description = 'Give me the correct sentiment of the following feedback')

str_parser = StrOutputParser()
pydantic_parser = PydanticOutputParser(pydantic_object = Feedback)

prompt1 = PromptTemplate(
    template = '''Classify the sentiment of the following {feedback} into positive and negative
    return only json object sentiment \n
    {format_instruction}''',
    input_variables = ['feedback'],
    partial_variables = {'format_instruction' : pydantic_parser.get_format_instructions()}
)

classifier_chain = prompt1 | model | pydantic_parser
# result = classifier_chain.invoke({"feedback" : 'This samsung product is working so well since the day I bought it Samsung S24 ultra is legendary phone'})
# print(result.sentiment)

prompt2 = PromptTemplate(
    template = '''write an straight forward line to the response to this positive feedback {feedback}''',
    input_variables = ['feedback']
)

prompt3 = PromptTemplate(
    template = '''write an straight forward line to the response to this negative feedback {feedback}''',
    input_variables = ['feedback']
)

branch_chain = RunnableBranch(
    (lambda x : x.sentiment == 'positive', prompt2 | model | str_parser),
    (lambda x : x.sentiment == 'negative', prompt3 | model | str_parser),
    RunnableLambda(lambda x : "Could not find any sentiment for the Feedback")
)

chain = classifier_chain | branch_chain
# review = '''Amazing 5g mobile phone at a good price. Battery backup, camera quality, performance is very good except sound is little bit low. Best in starting price range and good for students or normal users.'''

review = 'samsung phone '
result = chain.invoke({"feedback" : review})
print(result)
print()
print()
branch_chain.get_graph().print_ascii()