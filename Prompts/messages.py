from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
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

chat_history = [
    SystemMessage(content = "You are a helpful assistant in tech field")
]

while True:
    user_input = input("You : ")
    chat_history.append(HumanMessage(content = user_input))

    if user_input == 'exit':
        break
    else:
        response = model.invoke(chat_history).content
        chat_history.append(AIMessage(response))
        print(f"AI : {response}")
    
print(chat_history)


# personal data + training (pre-trained models) -> fine tuning :
# RAG : knowledge base add model brain
# book : pdf -> training basket leave policy + model

# make one maths agent