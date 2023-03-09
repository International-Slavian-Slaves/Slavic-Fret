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
        data_dict['RF_ID'] = edited_data['f_name']
        data_dict['Per_Fname'] = edited_data['s_name']
        data_dict['Per_Sname'] = edited_data['t_name']
        data_dict['Per_Tname'] = edited_data['rf_id']
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
