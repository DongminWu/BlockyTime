import os
import sys
from flask_sqlalchemy import SQLAlchemy
from Initialization import Initialization
from Utilities import debug_msg

from DB_Model.database_model import Users, Date, Blocks, Primary_Category, Secondary_Category

class database_helper(object):
    '''
    For some overall database
    '''

    def __init__(self, db):
        debug_msg(">>> %s.%s" % (__name__, sys._getframe().f_code.co_name))

        self.db = db
        db.create_all()

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

    def dump_all_data(self):
        '''
        dump all data in database
        '''

        '''
        dump Users data
        '''
        debug_msg('=========Users  start========')
        users_info = Users.query.all()
        for each in users_info:
            debug_msg(each.serialize)
        debug_msg('=========Users  end  ========')

        debug_msg('=========Primary_Category  start========')
        Primary_Categoryinfo = Primary_Category.query.all()
        for each in Primary_Categoryinfo:
            debug_msg(each.serialize)
        debug_msg('=========Primary_Category  end  ========')

        debug_msg('=========Secondary_Category  start========')
        Secondary_Categoryinfo = Secondary_Category.query.all()
        for each in Secondary_Categoryinfo:
            debug_msg(each.serialize)
        debug_msg('=========Secondary_Category  end  ========')

        debug_msg('=========Date  start========')
        Date_info = Date.query.all()
        for each in Date_info:
            debug_msg(each.serialize)
        debug_msg('=========Date  end  ========')

        debug_msg('=========Blocks  start========')
        Blocks_info = Blocks.query.all()
        for each in Blocks_info:
            debug_msg(each.serialize)
        debug_msg('=========Blocks  end  ========')
