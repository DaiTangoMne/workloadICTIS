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
    max_hours = Column(REAL)
    min_hours = Column(REAL)

    def __init__(self, unit: str, post: str, name: str, email: str, state: str, degree: str, rank: str, rate: float,
                 max_hours: float, min_hours: float):
        self.unit = unit
        self.post = post
        self.name = name
        self.email = email
        self.state = state
        self.degree = degree
        self.rank = rank
        self.rate = rate
        self.max_hours = max_hours
        self.min_hours = min_hours

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        # info: dict = {
        #     'ID': self.ID,
        #     'unit': self.unit,
        #     'post': self.post,
        #     'name': self.name,
        #     'email': self.email,
        #     'state': self.state,
        #     'degree': self.degree,
        #     'rank': self.rank,
        #     'rate': self.rate,
        #     'max_hours': self.max_hours,
        #     'min_hours': self.min_hours
        # }
        info: str = f'ID: {self.ID}, Name: {self.name}'
        return info
