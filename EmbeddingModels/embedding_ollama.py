from langchain_ollama import OllamaEmbeddings

embedding_model = OllamaEmbeddings(model = "bge-m3")
query = "What is machine learning"
vector = embedding_model.embed_query(query)
print(len(vector))