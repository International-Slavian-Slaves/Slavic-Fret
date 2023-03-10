from models.db_requests import insert_person_data, select_recent_passes
from local_logging import logger


def register_user(request_data):
    insert_person_data(request_data)

def get_recent_passes():
    return select_recent_passes()
