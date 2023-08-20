import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = "KEY"

st.title("Excel File Reader Java Code Generator")

uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file is not None:
    
    prompt = f"Generate Java code to read the uploaded Excel file using the Apache POI library.\n"
    prompt += f"File path: {uploaded_file.name}\n"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates Java code."},
            {"role": "user", "content": prompt},
        ]
    )

    generated_code = response.choices[0].message["content"].strip()

    st.subheader("Generated Java Code:")
    st.code(generated_code, language="java")

