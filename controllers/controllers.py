from models.db_queries import insert_person_data, select_recent_passes, select_locations, select_month_time
from models.db_queries import select_admin
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


def get_hours(id):
    return select_month_time(id)


def check_admin(id):
    return select_admin(id)
