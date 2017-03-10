import datetime
import sys
from flask_sqlalchemy import SQLAlchemy
from Utilities import debug_msg


from Initialization import Initialization
from DB_Model.database_model import Date
from DB_Model.database_helper import database_helper


class day_controller(object):
    '''
    All operation related to Date table will be written here
    Behaviors:
    1. get data of a day
    2. get date object for a day
    2. renew a day
        In this case, the last_changed_time should be updated

    '''

    def __init__(self, date_string=None, id=None,  user_id=None):
        debug_msg(">>> %s.%s" % (__name__, sys._getframe().f_code.co_name))
        self.date = None
        if date_string != None:
            self.date = self.query_date_from_string(date_string, user_id)
        if id != None:
            self.date = self.query_date_from_id(id, user_id)

        self.database = Initialization().get_global_db()
        self.db_helper = database_helper(self.database)

    def query_date_from_id(self, id, user_id):
        '''
        return a Date object after quering the Datebase
        '''
        info = Date.query.filter_by(id=id, uid=user_id).all()
        if info == []:
            return None
        else:
            return info[0]

    def query_date_from_string(self, date_string, user_id):
        '''
        return a Date object after quering the Datebase
        '''
        converted_date = datetime.datetime.strptime(
            date_string, "%Y-%m-%d").date()
        info = Date.query.filter_by(date=converted_date, uid=user_id).all()
        if info == []:
            return None
        else:
            return info[0]

    def get_date_object(self):
        '''
        getter of date object
        '''
        return self.date

    def get_date_id(self):
        '''
        design for internal using, return date_id for query Blocks
        '''
        if self.date is None:
            return self.date
        else:
            return self.date.id

    def get_last_changed_time(self):
        if self.date is None:
            return self.date
        else:
            return self.date.last_changed_time

    def get_date_list(self):
        ret = {}
        if self.date is None:
            return {}
        else:
            ret = self.date.serialize
            ret['date'] = ret['date'].strftime("%Y-%m-%d")
            ret['last_changed_time'] = ret['last_changed_time'].strftime(
                "%Y-%m-%d %H:%M:%S")
            return ret

    def update_day_data(self, data):
        '''
        update other data of this day
        '''
        #(2017.03.10)in this version, no data should update
        data = data
        if self.date is None:
            return self.date
        self.date.last_changed_time = datetime.datetime.now()
        self.db_helper.update_data(self.date)
        return self.date.last_changed_time
