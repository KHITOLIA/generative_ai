from langchain_classic.document_loaders import TextLoader

loader = TextLoader(file_path = r"C:\Users\Admin\Desktop\projects\Gen-AI_10_30_WD\abc.txt")
docs = loader.load()
print(docs[0].page_content)