from models.db_requests import insert_person_data
from local_logging import logger

def register_user(request_data):
    logger.debug("working")
    insert_person_data(request_data)
