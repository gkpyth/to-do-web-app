from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, Date, DateTime, ForeignKey, Table, Column
from typing import Optional
from datetime import datetime

# Base class required by Flask-SQLAlchemy 3.x for model definitions
class Base(DeclarativeBase):
    pass


# Create the database instance with the base class
db = SQLAlchemy(model_class=Base)

class Task(db.Model):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    task: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[str] = mapped_column(String(100), nullable=False, default='To Do')            # 'To Do', 'Done'
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    def __repr__(self):
        return f"<Task {self.id} - {self.title}>"
