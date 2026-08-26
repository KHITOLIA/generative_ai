# from langchain_classic.document_loaders import PyPDFLoader

# loader = PyPDFLoader(file_path = r"C:\Users\Admin\Desktop\projects\Gen-AI_10_30_WD\Machine learning System Design.pdf")

# docs = loader.load()
# print(len(docs))


from langchain_classic.document_loaders import PyMuPDFLoader
loader = PyMuPDFLoader(file_path = r"C:\Users\Admin\Desktop\projects\Gen-AI_10_30_WD\Machine learning System Design.pdf")

docs = loader.load()
print(len(docs))