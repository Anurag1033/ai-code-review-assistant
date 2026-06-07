from app.chains.reviewer_chain import chain

from app.db.database import SessionLocal
from app.db.models import Review


def review_code(code: str):

    result = chain.invoke({
        "code": code
    })

    review_text = result.content

    db = SessionLocal()

    review_row = Review(
        code=code,
        review=review_text
    )

    db.add(review_row)
    db.commit()

    db.close()

    return review_text