import streamlit as st
import google.generativeai as genai

# Set up Google Generative AI (Gemini) API
genai.configure(api_key="")

def review_code(code):
    """Uses Gemini AI to review Python code and suggest fixes."""
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"""
    You are an AI Code Reviewer. Review the following Python code and:
    1. Identify potential bugs, errors, and inefficiencies.
    2. Suggest improvements.
    3. Provide a corrected version of the code.
    
    Code:
    {code}
    """
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.title("🧑‍💻 An AI Code Reviewer")
st.write("Enter your Python code below for AI-powered code review.")

code_input = st.text_area("Enter your Python code here...", height=200)

if st.button("Generate"):
    if code_input.strip():
        with st.spinner("Reviewing code..."):
            response = review_code(code_input)
        st.subheader("Code Review")
        st.write(response)
    else:
        st.warning("Please enter some code before generating a review.")
