from fastapi import (
    FastAPI,
    UploadFile,
    File,
    Query,
    HTTPException
)


from app.schema.review import ReviewRequest

from app.services.reviewer import (
    review_code,
    get_review_by_id,
    get_stats,
    delete_review,
    get_reviews_by_language,
    get_paginated_reviews
)

from app.services.language_detector import detect_language

from app.db.database import engine
from app.db.models import Base
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Code Review Assistant"
)


@app.get("/")
def home():

    return {
        "message": "AI Code Review Assistant Running"
    }


@app.post("/review")
def review(request: ReviewRequest):

    language = "Python"

    result = review_code(
        request.code,
        language
    )

    return {
        "filename": "inline_input",
        "language": language,
        "review": result
    }


@app.get("/reviews")
def paginated_reviews(
    page: int = Query(1, ge=1),
    limit: int = Query(5, ge=1)
):

    data = get_paginated_reviews(
        page,
        limit
    )

    result = []

    for review in data:

        result.append({
            "id": review.id,
            "code": review.code,
            "language": review.language,
            "review": review.review,
            "created_at": review.created_at
        })

    return {
        "page": page,
        "limit": limit,
        "data": result
    }


@app.get("/reviews/{language}")
def reviews_by_language(language: str):

    data = get_reviews_by_language(language)

    result = []

    for review in data:

        result.append({
            "id": review.id,
            "code": review.code,
            "language": review.language,
            "review": review.review,
            "created_at": review.created_at
        })

    return result


@app.get("/review/{review_id}")
def single_review(review_id: int):

    review = get_review_by_id(review_id)

    if not review:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    return {
        "id": review.id,
        "code": review.code,
        "language": review.language,
        "review": review.review,
        "created_at": review.created_at
    }


@app.delete("/review/{review_id}")
def remove_review(review_id: int):

    deleted = delete_review(review_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    return {
        "message": "Review deleted successfully"
    }


@app.get("/stats")
def stats():

    return get_stats()