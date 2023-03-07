from python_db_logger.db_logger import DBLogger
from python_db_logger.connection_helper import ConnectionHelper
import logging

"""
Why a separate file? Since Python imports provide the same 
reference of a module wherever imported, it is easier to create
DBLogger in a separate file and import it everywhere. This way,
we don't have to worry about creating and passing the dbLogger 
instances from one file to another.
"""

db_logger: DBLogger = DBLogger(
    logging.getLogger(('')),
    ConnectionHelper(dot_env_file='.env')
)
