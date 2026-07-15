from langchain_huggingface import HuggingFaceEmbeddings

model_name = "Qwen/Qwen3-Embedding-0.6B"

embedding_model = HuggingFaceEmbeddings(model = model_name)

query = "This is a dog ?"

vectors = embedding_model.embed_query(query)
print(len(vectors))
print()
print(type(vectors))