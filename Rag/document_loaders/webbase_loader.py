from langchain_classic.document_loaders import WebBaseLoader

loader = WebBaseLoader(web_path = "https://www.orimi.com/pdf-test.pdf")

docs = loader.load()
print(docs)