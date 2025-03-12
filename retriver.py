from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

knowledge_base = [
    "Configure RAN with frequency 3.5 GHz and bandwidth 100 MHz",
    "Set gNB to 2.6 GHz with MIMO 4x4"
]

embeddings = model.encode(knowledge_base)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

def retrieve_best_match(query):
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), 1)
    return knowledge_base[I[0][0]]
