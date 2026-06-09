from app.chains.reviewer_chain import chain
from app.db.database import SessionLocal
from app.db.models import Review


def review_code(code: str, language: str):

    try:
        review = chain.invoke(
            {"code": code}
        ).content

    except Exception as e:
        review = f"Gemini Error: {str(e)}"

    db = SessionLocal()

    review_record = Review(
        code=code,
        language=language,
        review=review
    )

    db.add(review_record)
    db.commit()
    db.refresh(review_record)

    response = {
        "id": review_record.id,
        "review": review
    }

    db.close()

    return response


def get_all_reviews():

    db = SessionLocal()

    reviews = db.query(Review).all()

    db.close()

    return reviews


def get_review_by_id(review_id: int):

    db = SessionLocal()

    review = db.query(Review).filter(
        Review.id == review_id
    ).first()

    db.close()

    return review


def get_stats():

    db = SessionLocal()

    total_reviews = db.query(Review).count()

    python_reviews = db.query(Review).filter(
        Review.language == "Python"
    ).count()

    java_reviews = db.query(Review).filter(
        Review.language == "Java"
    ).count()

    javascript_reviews = db.query(Review).filter(
        Review.language == "JavaScript"
    ).count()

    cpp_reviews = db.query(Review).filter(
        Review.language == "C++"
    ).count()

    db.close()

    return {
        "total_reviews": total_reviews,
        "python_reviews": python_reviews,
        "java_reviews": java_reviews,
        "javascript_reviews": javascript_reviews,
        "cpp_reviews": cpp_reviews
    }


def delete_review(review_id: int):

    db = SessionLocal()

    review = db.query(Review).filter(
        Review.id == review_id
    ).first()

    if not review:
        db.close()
        return False

    db.delete(review)
    db.commit()
    db.close()

    return True


def get_reviews_by_language(language: str):

    db = SessionLocal()

    reviews = db.query(Review).filter(
        Review.language.ilike(language)
    ).all()

    db.close()

    return reviews


def get_paginated_reviews(page: int, limit: int):

    db = SessionLocal()

    offset = (page - 1) * limit

    reviews = (
        db.query(Review)
        .offset(offset)
        .limit(limit)
        .all()
    )

    db.close()

    return reviews