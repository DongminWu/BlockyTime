import datetime
import sys
from flask_sqlalchemy import SQLAlchemy
from Utilities import debug_msg


from Initialization import Initialization
from DB_Model.database_model import Users
from DB_Model.database_helper import database_helper


class users_controller(object):
    '''
    initializing with uid
    1. return user list
    2. login, logout
    2. reset password
    3. creating a user

    to learn: how to ensure security of user session
    '''

    def __init__(self):
        '''
        :)
        '''
        debug_msg(">>> %s.%s" % (__name__, sys._getframe().f_code.co_name))
        self.database = Initialization().get_global_db()
        self.db_helper = database_helper(self.database)

    def check_login_status(self, uid):
        '''
        we can use flask_login plugin
        before implement that plugin, just leave it True
        '''
        return True

    def get_user_object(self, uid):
        '''
        it is better to be a privae method
        get the information of a user
        '''
        info = Users.query.filter_by(uid=uid).all()
        if info == []:
            return None
        else:
            return info[0]

    def get_user_list(self, uid):
        '''
        return get_user_object(uid).serialize, unless the return value is error(-1)
        remove the password item
        '''
        ret = self.get_user_object(uid)
        if ret is None:
            return -1
        else:
            ret_list = ret.serialize
            del ret_list['password']
            return ret_list

    def __get_uid_from_nick_name(self, nick_name):
        '''
        nick_name should be unique
        '''
        info = Users.query.filter_by(nick_name=nick_name).all()
        if info == []:
            return None
        else:
            return info[0].uid

    def sign_in(self, nick_name, password):
        '''
        return true or false
        '''
        uid = self.__get_uid_from_nick_name(nick_name)
        if uid is None:
            return False
        ret = self.get_user_object(uid)
        if ret is None:
            return False
        elif ret.serialize['password'] != password:
            return False
        else:
            return True

    def logout(self, uid):
        '''
        return true or false
        '''
        return True

    def reset_password(self, nick_name, old_password, new_password):
        '''
        return True or Flase
        '''
        uid = self.__get_uid_from_nick_name(nick_name)
        if uid is None:
            return False
        ret = self.get_user_object(uid)
        if ret is None:
            return False
        elif ret.serialize['password'] != old_password:
            return False
        else:
            ret.password = new_password
            self.db_helper.update_data(ret)
            return True

    def __create_a_user(self, nick_name, password):
        '''
        it is better to be a private method
        will be used by sign_up(uid)
        '''
        new_uid = Users.query.count()
        new_User = Users(uid=new_uid, nick_name=nick_name, password=password)
        self.db_helper.update_data(new_User)
        return True

    def sign_up(self, nick_name, password):
        '''
        return true or false
        '''
        ret = Users.query.filter_by(nick_name=nick_name).count()
        if ret > 0:
            return False
        else:
            return self.__create_a_user(nick_name, password)
