from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.document_loaders import TextLoader
loader = TextLoader(file_path = r"C:\Users\Admin\Desktop\projects\Gen-AI_10_30_WD\abc.txt")

docs = loader.load()
# print(docs)

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 150,
    chunk_overlap = 30
)

chunks = splitter.split_documents(documents = docs)
print(len(chunks))