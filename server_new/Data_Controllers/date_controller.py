from flask_sqlalchemy import SQLAlchemy
import datetime
import sys
from Utilities import debug_msg


from DB_Model.database_model import Date

class date_controller(object):
    '''
    All operation related to Date table will be written here
    '''
    def __init__(self):
        debug_msg(">>> %s.%s" % (__name__, sys._getframe().f_code.co_name))
    