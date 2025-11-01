from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables (optional if already set)
from dotenv import load_dotenv
load_dotenv()

# Create a prompt template
prompt = ChatPromptTemplate.from_template(
    "You are a creative AI assistant. Write a fun startup idea based on: {idea}"
)

# Create the LLM (Groq model)
llm = ChatGroq(model="llama-3.1-8b-instant")

# Combine prompt + model
chain = prompt | llm

# Example input
one_liner = "an app that helps people find cofounders with complementary skills"

# Run the chain
response = chain.invoke({"idea": one_liner})

print("\n💡 Startup Idea:")
print(response.content)
