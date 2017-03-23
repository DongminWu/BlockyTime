import sys
from flask_sqlalchemy import SQLAlchemy
from Utilities import debug_msg


from Initialization import Initialization
from DB_Model.database_model import Blocks
from DB_Model.database_helper import database_helper
from Data_Controllers.day_controller import day_controller


class blocks_controller(object):
    '''
    initializing with uid
    1. return a whole blocks list of a day
    2. update a block, change secondary category
    3. create default block
    '''

    def __init__(self, user_id):
        debug_msg(">>> %s.%s" % (__name__, sys._getframe().f_code.co_name))
        self.uid = user_id
        self.database = Initialization().get_global_db()
        self.db_helper = database_helper(self.database)

    def get_block_obj_from_id(self, id):
        '''
        return a block object
        '''
        info = Blocks.query.filter_by(uid=self.uid, id=id).all()
        if info == []:
            return None
        else:
            return info[0]

    def get_blocks_objects_of_a_day(self, day_string):
        '''
        return a list of objects
        if met error, return []
        '''
        day_obj = day_controller(
            user_id=self.uid, id=None, date_string=day_string)
        day_id = day_obj.get_date_id()
        if day_id is None:
            return []
        info = Blocks.query.filter_by(uid=self.uid, date_id=day_id).all()
        return info

    def get_blocks_list_of_a_day(self, day_string):
        '''
        return a serialized list of blocks
        if met error, return []
        '''
        block_objs = self.get_blocks_objects_of_a_day(day_string)
        ret = []
        for each in block_objs:
            ret.append(each.serialize)
        return ret

    def update_a_block(self, block_id, secondary_category_id):
        '''
        will not update last change time
        '''
        from Data_Controllers.category_controller import category_controller
        category_con = category_controller(self.uid)
        primary_category_id = category_con.get_primary_id_from_secondary_object(
            category_con.get_secondary_object_from_id(secondary_category_id))
        if primary_category_id == -1:
            return -1
        block_obj = self.get_block_obj_from_id(block_id)
        block_obj.primary_category_id = primary_category_id
        block_obj.secondary_category_id = secondary_category_id
        self.db_helper.update_data(block_obj)

