import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from src.retriever import retrieve
from src.generator import generate_answer

# Page configuration (for better layout)
st.set_page_config(
    page_title="IT LawBot: Navigating the Information Technology Act 2000",
    page_icon=":balance_scale:",
    layout="wide"
)

# Main title and description
st.title("IT LawBot: Navigating the Information Technology Act 2000")
st.write(
    "Welcome to **IT LawBot**! Ask your question related to the **Information Technology Act, 2000** "
    "and get relevant legal sections and a detailed answer generated based on the Act's provisions."
)

# Input box for the user's question
query = st.text_input("Enter your question related to the IT Act 2000:")

# Submit button functionality
if st.button("Submit", help="Click to retrieve relevant sections and generate an answer"):
    if query:
        with st.spinner("Retrieving legal sections..."):
            try:
                # Retrieve relevant legal chunks
                chunks = retrieve(query, k=5)

                if not chunks:
                    st.warning("No relevant sections found. Please try rephrasing your query.")
                else:
                    with st.spinner("Generating answer..."):
                        # Generate the answer from the retrieved chunks
                        answer = generate_answer(query, chunks)

                    # Displaying the generated answer in a nicely formatted box
                    st.subheader("Answer:")
                    st.markdown(f"""
                    <div style="background-color: #333333; padding: 20px; border-radius: 5px; border: 1px solid #444444; color: white;">
                        {answer}
                    </div>
                    """, unsafe_allow_html=True)

                    # Displaying the relevant chunks in an organized format
                    st.subheader("Relevant Sections Retrieved:")

                    # Use columns to display chunks in a more organized way
                    cols = st.columns(2)
                    for i, c in enumerate(chunks):
                        col = cols[i % 2]  # Alternate between columns
                        col.markdown(f"**Page {c['page']}**", unsafe_allow_html=True)
                        col.write(f"<div style='color: #D3D3D3;'>{c['text'][:400]}...</div>", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"An error occurred while processing your request: {e}")
    else:
        st.warning("Please enter a question to get an answer.")
