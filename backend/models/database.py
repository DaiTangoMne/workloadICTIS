from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:root@localhost:5432/workload", echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()

# engine.connect()
