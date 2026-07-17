from src.database.database import Base
from src.database.database import engine


def init_database():

    Base.metadata.create_all(engine)
