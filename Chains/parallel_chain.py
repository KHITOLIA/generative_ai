from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
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

prompt1 = PromptTemplate(
    template = '''generate short and simple notes from the following {text}''',
    input_variables = ['text']
)

prompt2 = PromptTemplate(
    template = '''genetate 5 short question and answer from the following text \n {text}''',
    input_variables = ['text']
)

parallel_chain = RunnableParallel(
    {
        'notes' : prompt1 | model | parser,
        'quiz' : prompt2 | model | parser 
    }
)
result = parallel_chain.invoke({"text" : '''Machine learning is a subfield of artificial intelligence that lets computers learn from data and improve over time without being explicitly programmed for every task. Instead of writing hardcoded rules, developers train models on data samples to recognize patterns and make predictions.Main Types of Machine LearningSupervised Learning: Trains on labeled data to predict outcomes or classify information (e.g., spam filters, linear regression).Unsupervised Learning: Finds hidden structures or groups in unlabeled data (e.g., customer clustering).Reinforcement Learning: Learns optimal actions through trial, error, and a reward system.Deep Learning: Uses multi-layered artificial neural networks to handle complex data like images and speech.Watch this video for a clear overview of how machine learning models work and compare to deep learning:2mMachine Learning Explained Simply (In 12 Minutes)1.2L views · 7 months agoYouTube · The Gradient DescentCommon Real-World UsesRecommendation systems on streaming and shopping sites.Spam detection in email inboxes.Autonomous driving and computer vision.Language translation and virtual assistants'''})
print(result.quiz)

print()
print(parallel_chain.get_graph().print_ascii())