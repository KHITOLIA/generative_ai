from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
model_name = "sentence-transformers/all-MiniLM-L6-v2"

embedding_model = HuggingFaceEmbeddings(model = model_name)

q1 = '''Virat Kohli is an Indian international cricketer and the former all-format captain of the Indian national cricket team. He is a right-handed batter and occasional right-arm medium-pace bowler. Considered one of the greatest batsmen in limited overs cricket, he has been acclaimed for his batting skills and records'''
q2 = '''India has given to the world many a great cricketer but none as ambitious as Virat Kohli. To meet his ambition, Kohli employed the technical assiduousness of Sachin Tendulkar and fitness that was in the league of top athletes in the world, not just cricketers. As a result, Kohli became the most consistent all-format accumulator of his time, making jaw-dropping chases look easy, and finding, in his own words, the safest possible way to score runs. Plenty of them.
This ambition transferred seamlessly to his captaincy: he demanded more than ever before of his bowlers, especially the quick ones, often sacrificed a batter for bowling depth, and led India to a long stay at No. 1 in the Test rankings and a first-ever Test series win in Australia. India won 40 out of the 68 Tests in which Kohli led, making him the fourth-most successful captain in the world, behind Graeme Smith, Ricky Ponting and Steve Waugh.'''

v1 = embedding_model.embed_query(q1)
v2 = embedding_model.embed_query(q2)
v1 = np.array(v1).reshape(1, -1)
v2 = np.array(v2).reshape(1, -1)
print(cosine_similarity(v1, v2))