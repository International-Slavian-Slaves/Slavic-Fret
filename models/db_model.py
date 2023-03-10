import sqlalchemy as db
from sqlalchemy.orm import declarative_base

Base = declarative_base()

engine = db.create_engine("sqlite:///SQLite.db")
connection = engine.connect()
metadata = db.MetaData()

person = db.Table('person', metadata,
                  db.Column('RF_ID', db.TEXT, unique=True, primary_key=True),
                  db.Column('Per_Fname', db.TEXT),
                  db.Column('Per_Mname', db.TEXT),
                  db.Column('Per_Lname', db.TEXT)
                  )

passes = db.Table('passes', metadata,
                  db.Column('Pass_ID', db.INTEGER, nullable=False, unique=True, autoincrement=True, primary_key=True),
                  db.Column('RF_ID', db.TEXT, db.ForeignKey('person.RF_ID')),
                  db.Column('Pass_Date', db.TEXT),
                  db.Column('Pass_Dir', db.TEXT),
                  )

# metadata.create_all(engine)
# connection.close()