from app.db.database import engine, Base
from app.db.models import Review

Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")