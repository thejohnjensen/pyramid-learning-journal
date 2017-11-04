from sqlalchemy import (
    Column,
    Unicode,
    Index,
    Integer,
    Text,
    DateTime
)

from .meta import Base
from datetime import datetime


class Journal(Base):
    __tablename__ = 'journal_entries'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    date = Column(DateTime)
    body = Column(Text)

    def __init___(self, *args, **kwargs):
        """."""
        super(Journal, self).__init___(*args, **kwargs)
        self.date = datetime.now()

    def to_dict(self):
        """."""
        return {
            'id': self.id,
            'title': self.title,
            'date': self.date.strftime('%m/%d/%Y'),
            'body': self.body
        }


# Index('my_index', MyModel.name, unique=True, mysql_length=255)
