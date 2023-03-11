from models.db_queries import insert_person_data, select_recent_passes, select_locations
from models.kill_yourself import make_fun
from local_logging import logger


def register_user(request_data):
    insert_person_data(request_data)


def get_recent_passes(limit):
    return select_recent_passes(limit)


def get_fun():
    return make_fun()


def get_locations():
    return select_locations()
