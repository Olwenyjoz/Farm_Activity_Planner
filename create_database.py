"""
Create the SQLite database.
"""

from app.database.base import Base
from app.database.connection import engine

# Import models so SQLAlchemy knows about them
from app.database.models import FarmPlanModel


Base.metadata.create_all(bind=engine)

print("Database created successfully.")