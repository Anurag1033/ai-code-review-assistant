from fastapi import FastAPI
from pydantic import BaseModel

from app.services.reviewer import review_code

app = FastAPI(
    title="AI Code Review Assistant"
)


class CodeRequest(BaseModel):
    code: str


@app.get("/")
def home():

    return {
        "message": "AI Code Review Assistant Running"
    }


@app.post("/review")
def review(request: CodeRequest):

    result = review_code(
        request.code
    )

    return {
        "review": result
    }