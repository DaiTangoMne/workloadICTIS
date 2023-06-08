from sqlalchemy import Column, Integer, String, REAL
from models.database import Base


class Educators(Base):
    __tablename__ = 'educators'

    ID = Column(Integer, primary_key=True)
    unit = Column(String)
    post = Column(String)
    name = Column(String)
    email = Column(String, unique=True)
    state = Column(String)
    degree = Column(String)
    rank = Column(String)
    rate = Column(REAL)

    def __init__(self, unit: str, post: str, name: str, email: str, state: str, degree: str, rank: str, rate: float):
        self.unit = unit
        self.post = post
        self.name = name
        self.email = email
        self.state = state
        self.degree = degree
        self.rank = rank
        self.rate = rate

    def __repr__(self):
        info: str = f'ID: {self.ID}\n' \
                    f'Преподаватель: {self.name}\n' \
                    f'email: {self.email}'
        return info