import enum
from models.db import db
from sqlalchemy.orm import Mapped, mapped_column

class RentalStatus(enum.Enum):
    available = 1
    rented = 2
    unavailable = 3 # lost or damaged

class Book(db.Model):
  __tablename__ = 'books'
  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column()
  author: Mapped[str] = mapped_column()
  publisher: Mapped[str] = mapped_column()
  year: Mapped[int] = mapped_column()
  status: Mapped[RentalStatus] = mapped_column() 
  
  def __repr__(self):
    return f"<Book(id={self.id}, title='{self.title}', author='{self.author}', publisher='{self.publisher}', year={self.year}, status='{self.status.name}')>"

  def to_dict(self):
    return {
      'id': self.id,
      'title': self.title,
      'author': self.author,
      'publisher': self.publisher,
      'year': self.year,
      'status': self.status.name
    }
