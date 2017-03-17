import sys
from flask_sqlalchemy import SQLAlchemy
from Utilities import debug_msg


from Initialization import Initialization
from DB_Model.database_model import Primary_Category
from DB_Model.database_model import Secondary_Category
from DB_Model.database_helper import database_helper


class category_controller(object):
    '''
    the main purpose of this class
    1. Get current categories list
    2. Get a Primary_Category object from primary id
    3. Get the id of Primary_Category from a Secondary_Category object
    3. Get a primary_Categroy object from Secondary_Category object
    '''

    def __init__(self, user_id=None):
        debug_msg(">>> %s.%s" % (__name__, sys._getframe().f_code.co_name))
        self.uid = user_id

    def get_primary_object_list(self):
        '''
        :)
        '''
        info = Primary_Category.query.filter_by(uid=self.uid).all()
        if info == []:
            return -1
        else:
            return info

    def get_primary_object_from_id(self, id):
        '''
        get primary objctect from primary id
        should be careful with wrong uid
        '''
        info = Primary_Category.query.filter_by(uid=self.uid, id=id).all()
        if info == []:
            return -1
        else:
            return info[0]

    def get_secondary_object_from_id(self, id):
        '''
        nothing
        '''
        info = Secondary_Category.query.filter_by(uid=self.uid, id=id).all()
        if info == []:
            return -1
        else:
            return info[0]

    def get_primary_object_from_secondary_object(self, secondary_obj):
        '''
        nothing
        '''
        if not isinstance(secondary_obj, Secondary_Category):
            return -1
        info = Primary_Category.query.filter_by(
            uid=self.uid, id=secondary_obj.primary_id).all()
        if info == []:
            return -1
        else:
            return info[0]

    def get_primary_id_from_secondary_object(self, secondary_obj):
        '''
        get_primary_object_from_secondary_object() + get_primary_object_from_id()
        '''
        if not isinstance(secondary_obj, Secondary_Category):
            return -1
        else:
            return secondary_obj.primary_id

    def get_secondary_object_list_from_primary_object(self, primary_obj):
        '''
        :)
        '''
        if not isinstance(primary_obj, Primary_Category):
            return -1
        info = Secondary_Category.query.filter_by(
            uid=self.uid, primary_id=primary_obj.id).all()
        if info == []:
            return -1
        else:
            return info

    def get_secondary_id_list_from_primary_object(self, primary_obj):
        '''
        :)
        '''
        ret = self.get_secondary_object_list_from_primary_object(primary_obj)
        if ret == -1:
            return ret
        else:
            ret_id_list = []
            for each in ret:
                ret_id_list.append(each.id)
            return ret_id_list

    def get_category_list(self):
        '''
        get completed category list, {primary: xxxx, secondary:{},...
        '''
        ret = []
        info = Primary_Category.query.filter_by(uid=self.uid).all()
        for each_pri in info:
            second_list = []
            each_pri_list = each_pri.serialize
            sec_info = Secondary_Category.query.filter_by(
                uid=self.uid, primary_id=each_pri.id).all()
            for each_sec in sec_info:
                second_list.append(each_sec.serialize)
            each_pri_list['secondary_category'] = second_list
            ret.append(each_pri_list)
        return ret
