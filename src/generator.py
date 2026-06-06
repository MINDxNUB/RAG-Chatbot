import google.generativeai as genai

genai.configure(api_key="AIzaSyBk6vZ6bMv_kGC826YtN5ByfeU8pYP0068")

SYSTEM_PROMPT = """
You are a legal assistant specializing only in the Information Technology Act 2000.
Answer strictly based on provided text chunks.
If information is not present, say: "The information you're asking for is not available. Please ensure your question aligns with the provisions of the IT Act."
Always cite page numbers of chunks used.
Never hallucinate or add information not present in the context.
Only display relevant sections retrieved if the data is available. 
"""

def generate_answer(query, chunks):
    context = "\n\n---\n\n".join(
        f"[Page {c['page']}]\n{c['text']}" for c in chunks
    )

    full_prompt = f"{SYSTEM_PROMPT}\n\nContext:\n{context}\n\nQuery: {query}\nAnswer with citations."

    response = genai.GenerativeModel("gemini-2.5-flash").generate_content(full_prompt)
    return response.text
