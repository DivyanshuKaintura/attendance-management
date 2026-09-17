
# SQLAlchemy uses a declarative system to let us define database tables using Python classes.

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """Base class for all models."""
    pass