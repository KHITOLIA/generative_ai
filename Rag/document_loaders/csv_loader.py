# import pandas as pd

# df = pd.read_csv("")

# print(df.head())

from langchain_classic.document_loaders import CSVLoader

loader = CSVLoader(file_path= r"C:\Users\Admin\Desktop\projects\Gen-AI_10_30_WD\insurance.csv")

docs = loader.load()
print(docs[0].page_content)