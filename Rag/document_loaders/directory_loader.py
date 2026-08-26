from langchain_classic.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = r"C:\Users\Admin\Desktop\projects\Gen-AI_10_30_WD\data",
    glob = "*.pdf",
    loader_cls = PyPDFLoader
)

docs = loader.load()
print(docs)