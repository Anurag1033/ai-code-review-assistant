from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from app.prompts.review_prompt import REVIEW_PROMPT

load_dotenv()

prompt = PromptTemplate(
    template=REVIEW_PROMPT,
    input_variables=["code"]
)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)

chain = prompt | llm