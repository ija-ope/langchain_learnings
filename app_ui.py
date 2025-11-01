from dotenv import load_dotenv
load_dotenv()


import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# --- Set up the model ---
llm = ChatGroq(model="llama-3.1-8b-instant")

# --- Define your prompt ---
prompt = ChatPromptTemplate.from_template(
    "You are Paul Graham. Write a short reflective essay based on this idea: {idea}. "
    "Keep it thoughtful, conversational, and insightful."
)

# --- UI Layout ---
st.title("🧠 Paul Graham Essay Generator")
st.write("Type an idea and watch 'Paul Graham' write about it in seconds.")

idea = st.text_area("💡 Enter your idea here:", "")

if st.button("Generate Essay"):
    if idea.strip() == "":
        st.warning("Please enter an idea first!")
    else:
        with st.spinner("Thinking like Paul Graham..."):
            chain = prompt | llm
            response = chain.invoke({"idea": idea})
            st.subheader("📝 Paul Graham-style Essay:")
            st.write(response.content)
