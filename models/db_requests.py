import sqlalchemy as db
from models.db_model import person, passes
from local_logging import logger
from werkzeug.datastructures import ImmutableMultiDict

engine = db.create_engine("sqlite:///SQLite.db")


def make_dict(request_data):
    with engine.connect() as connection:
        logger.debug("making dict")
        edited_data = ImmutableMultiDict.to_dict(request_data)
        logger.debug(edited_data)
        data_dict = dict()
        data_dict['RF_ID'] = edited_data['rf_id']
        data_dict['Per_Fname'] = edited_data['f_name']
        data_dict['Per_Mname'] = edited_data['m_name']
        data_dict['Per_Lname'] = edited_data['l_name']
        logger.debug(data_dict)
        return data_dict


def insert_person_data(request_data):
    with engine.connect() as connection:
        logger.debug("entered")
        data_dict = make_dict(request_data)
        logger.debug(data_dict)
        insertion_query = person.insert().values([data_dict])
        connection.execute(insertion_query)
        connection.commit()


# insert_data_person({'RF_ID':'112343434', 'Per_Fname':'Иван', 'Per_Sname': 'Иванович', 'Per_Tname': 'Иванов'})

def select_recent_passes():
    with engine.connect() as connection:
        logger.debug("entered")
        selection_query = db.select(person.join(passes, person.columns.RF_ID == passes.columns.RF_ID)) \
            .order_by(db.desc(passes.columns.Pass_Date)) \
            .limit(3)
        result = connection.execute(selection_query)
        return result.fetchall()


print(select_recent_passes())
