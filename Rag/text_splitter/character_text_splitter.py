from langchain_text_splitters import CharacterTextSplitter
from langchain_classic.document_loaders import TextLoader
loader = TextLoader(file_path = r"C:\Users\Admin\Desktop\projects\Gen-AI_10_30_WD\abc.txt")

splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 50,
    chunk_overlap = 30
)

docs = loader.load()
chunks = splitter.split_documents(docs)

print(chunks)


# s = "Training basket"
# The series was among FAHASA’s Top 10\nReaders Choice Books in 2014.\
#  among FAHASA’s Top 10\nReaders Choice Books in 2014.
# print(s.split())