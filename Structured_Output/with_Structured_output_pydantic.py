from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import Field, BaseModel

model = ChatOpenAI(model = "gpt-5.5", temperature = 0.5, max_completion_tokens = 1000)

# Review : from amazon : summary, sentiment

# class Review(TypedDict):
#     summary : str
#     sentiment : str


class Review(BaseModel):
    key_theme : str =  Field(description = "write down all the key themes you'll find in the review")
    summary : Annotated[str, "Give me brief summary of the given review"]
    sentiment : Annotated[Literal["pos", "neg"], "give me the sentiment from the review either negative positive or neutral"]
    pros : Annotated[Optional[list[str]], "Write down all the pros you find in the review"]
    cons : Annotated[Optional[list[str]], "Write down all the pros you find in the review"]
    rating : Annotated[str, "give me the rating given by the customer in the given review"]


review = '''
I was confused. I wanted to try the OnePlus 15 but settled for OnePlus Nord 5 for many reasons.
Here's a flat comparison
Pros & Cons
OnePlus Nord 5 5G 📱
Excellent performance. Outstanding selfie camera - one of the best till date by any phone, big display, great gaming modes and support.
OnePlus 15 Pro 📱
Amazing Overall Performance: Great display, battery is outstanding, more compact.
BATTERY
OnePlus Nord 5 5G 📱
6800 mAh (typical) battery is good enough unless you want to go for that slightly extra life.
'''

structured_output_model = model.with_structured_output(Review)

response = structured_output_model.invoke(review)
print(response)


