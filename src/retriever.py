import faiss, json
import numpy as np
from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer("all-MiniLM-L6-v2")

def load_all():
    index = faiss.read_index("D:/Zecser/B110-Muhammed-Salman-Phase-4/Data/faiss_index.bin")
    metadata = [json.loads(line) for line in open("D:/Zecser/B110-Muhammed-Salman-Phase-4/Data/metadata.jsonl")]
    return index, metadata

index, metadata = load_all()

def retrieve(query, k=5):
    q_emb = embedder.encode([query], convert_to_numpy=True)
    faiss.normalize_L2(q_emb)
    D, I = index.search(q_emb, k)
    
    results = []
    for score, idx in zip(D[0], I[0]):
        if idx == -1: continue
        results.append(metadata[idx])
    return results
