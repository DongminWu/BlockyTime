import os
import sys
from flask_sqlalchemy import SQLAlchemy
from Initialization import Initialization
from Utilities import debug_msg


class database_helper(object):
    '''
    For some overall database
    '''

    def __init__(self, db):
        debug_msg(">>> %s.%s" % (__name__, sys._getframe().f_code.co_name))

        self.db = db
        self.db.create_all()

    def rebuild_database(self):
        '''
        db drop then db create
        '''
        self.db.drop_all()
        self.db.create_all()


    def update_data(self, model):
        '''
        db.session.add(db.Model)
        db.session.commit()
        '''
        self.db.session.add(model)
        self.db.session.commit()
