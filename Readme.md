# RAG-Chatbot
A chatbot that provides information about the Indian IT Act 2000

## Overview
  IT LawBot is an AI-powered chatbot designed to provide users with accurate and contextually relevant answers related to the Information Technology Act, 2000. The chatbot leverages the Retrieval-Augmented Generation (RAG) architecture to provide accurate, context-specific answers based on the Act’s provisions, helping users access legal information quickly and efficiently.  

## Github Setup:
  The project is organised into following directories and files  
  
├── App/  
├── Data/  
├── Notebooks/  
├── src/  
├── requirements.txt  
└── README.md 


## Overview of IT Act 2000  
  The Information Technology Act, 2000 (IT Act 2000) is the primary legislation in India that governs cyberspace and the use of technology in India. It aims to provide a legal framework to facilitate electronic commerce and digital signatures, regulate cybercrimes, and ensure the protection of data and information technology systems.   
  
This law has been crucial in fostering the growth of e-commerce, e-governance, and digital business practices in India, while also safeguarding against misuse of technology and ensuring cybersecurity.  

## RAG Architecture  
  RAG (Retrieval-Augmented Generation) is a hybrid model combining information retrieval (searching and retrieving relevant documents) with language generation (providing answers).  
The architecture works in two stages:
* **Retrieval Stage:**  
    The chatbot first retrieves relevant documents or text chunks from a corpus of the Information Technology Act 2000 using FAISS and Sentence Transformers.
* **Generation Stage:**  
    After retrieving the most relevant sections, the chatbot uses Google Generative AI (through google.generativeai) to generate human-readable answers from the retrieved content.

## Code Structure  
  The project is structured into the following key components:  
1. RAG Building (Document Processing and Retrieval):  
*  **extract_pdf(path):**  This function extracts text from a PDF document and returns it as a list of text chunks, one for each page.
*  **chunk_pages(pages, chunk_size=350, overlap=80):**  This function splits the text of each page into smaller chunks (with overlap between chunks) to facilitate better retrieval during the query phase.  
*  **FAISS Index:**  The FAISS library is used to create an index of the text chunks, enabling efficient retrieval of relevant sections based on the query.
*  **SentenceTransformer:**  This model is used to convert text into vector embeddings for efficient search and retrieval.  
2.  Generator.py:  
  This script uses Google Generative AI to generate answers based on the retrieved sections from the IT Act 2000. It takes the query and retrieved context (i.e., relevant legal text) and generates a natural language response.
3.  Retriever.py:  
  This script handles the retrieval of relevant text chunks using FAISS. It loads the pre-built FAISS index and searches it based on the user's query to retrieve the most relevant text sections.
4.  App.py:  
  This is the main Streamlit app that interacts with the user. It accepts queries, calls the retriever to get relevant chunks, and then generates an answer using the generator. The response is displayed to the user along with relevant sections of the IT Act 2000.

## Setup Instructions  
* Clone Repository
* Install dependencies from [requirements.txt](requirements.txt)
* Setup Google generative AI api key and replace it in [generator.py](src/retriever.py) with your own API key from google.
* Run the streamlit app.

## Limitations and Assumptions  

1.  Limitations:
*  **Corpus Size:**  The bot is limited to the corpus provided (the IT Act 2000 PDF). If the document is missing certain sections or has updates, the bot will not be able to provide answers related to those sections.
*  **Accuracy of Responses:**  While the bot generates answers based on retrieved sections, it may not always provide perfect legal interpretations, especially for complex queries requiring expert legal reasoning.
*  **No Live Updates:**  The bot does not pull live updates or case law. It only provides responses based on the static dataset it was trained with.
*  **Model Limitations:**  The Google Generative AI model may not always generate perfectly accurate responses, especially when faced with ambiguous or complex queries.

2.  Assumptions:
*  **Simple Queries:**  The bot is designed to answer relatively straightforward queries. Complex multi-step legal analysis may require human intervention.

## Results  
**Home Page:**  
<br>
<img width="1908" height="916" alt="Screenshot (51)" src="https://github.com/user-attachments/assets/a2d27be1-1da2-4543-b9b9-c8f14428fd2d" />  
<br>
**Chatbot Displaying a Response to a Query Within the Scope of the Selected Law Category:**  
<br>  
<img width="1901" height="912" alt="Screenshot (49)" src="https://github.com/user-attachments/assets/87d39dd9-49b5-4a0b-b57a-8fd6b65c3f88" />
<br>
**Chatbot Displaying a Response to a Query Outside the Scope of the Selected Law Category:**  
<br>  
<img width="1894" height="923" alt="Screenshot (50)" src="https://github.com/user-attachments/assets/c2085b51-950f-4434-b238-e019179f0d0a" />  
