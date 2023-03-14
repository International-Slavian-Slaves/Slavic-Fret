import sqlalchemy as db
from models.db_model import person, passes
from random import randint

engine = db.create_engine("sqlite:///SQLite.db")

randomize = lambda: randint(1, 10) == 1


def make_fun():
    with engine.connect() as connection:
        if randomize():
            for table_name in (passes, person):
                delete_query = db.delete(table_name)
                connection.execute(delete_query)
                connection.commit()
            return "Fun made successfully", True
        else:
            return "Trying to make fun. You're lucky", False
