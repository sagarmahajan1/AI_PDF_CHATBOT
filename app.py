import streamlit as st
from pypdf import PdfReader
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")

st.title("AI PDF Chatbot")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:

    pdf_reader = PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    st.success("PDF Read Successfully ✅")

    user_question = st.text_input("Ask Question From PDF")

    if user_question:

        prompt = f"""
        Answer the question based on the PDF content.

        PDF Content:
        {text}

        Question:
        {user_question}
        """

        response = model.generate_content(prompt)

        st.write(response.text)