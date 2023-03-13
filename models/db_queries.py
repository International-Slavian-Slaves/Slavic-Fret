import sqlalchemy as db
import sqlite3 as sqlite
from models.db_model import person, passes
from local_logging import logger
from werkzeug.datastructures import ImmutableMultiDict
from count_month_time import create_stack, count_month_time

engine = db.create_engine("sqlite:///SQLite.db")


def make_dict(request_data):
    with engine.connect() as connection:
        edited_data = ImmutableMultiDict.to_dict(request_data)
        data_dict = dict()
        data_dict['RF_ID'] = edited_data['rf_id']
        data_dict['Per_Fname'] = edited_data['f_name']
        data_dict['Per_Mname'] = edited_data['m_name']
        data_dict['Per_Lname'] = edited_data['l_name']
        return data_dict


def insert_person_data(request_data):
    with engine.connect() as connection:
        data_dict = make_dict(request_data)
        insertion_query = person.insert().values([data_dict])
        connection.execute(insertion_query)
        connection.commit()


def select_recent_passes(limit):
    with engine.connect() as connection:
        selection_query = db.select(person.join(passes, person.columns.RF_ID == passes.columns.RF_ID)) \
            .order_by(db.desc(passes.columns.Pass_Date))
        result = connection.execute(selection_query)
        return result.fetchmany(limit)


def select_locations():
    with sqlite.connect('SQLite.db') as connection:
        cursor = connection.cursor()
        query = "SELECT * FROM GeneralViewDudes;"
        result = cursor.execute(query)
        return result.fetchall()


def select_month_time(id):
    with sqlite.connect('SQLite.db') as connection:
        cursor = connection.cursor()
        query = "SELECT * FROM MonthPasses WHERE RF_ID = ?;"
        result = cursor.execute(query, (id,))
        data_array = result.fetchall()
        if data_array:
            stack = create_stack(data_array)
            return count_month_time(stack)
        else:
            return "Данные не найдены"


print(select_month_time("1233244"))
