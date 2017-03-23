import datetime
from Initialization import Initialization
from Data_Controllers.users_controller import users_controller
from DB_Model import database_helper
from DB_Model.database_tester import database_tester
from DB_Model.database_model import Users


class users_controller_tester(object):
    '''
    tester for day_controller
    '''

    def __init__(self):
        print("\n\n\n\n\n\n\n\n\n\n\n\n!!!users_controller_tester!!!")
        self.database = Initialization().get_global_db()
        self.db_helper = database_helper.database_helper(self.database)
        self.db_helper.rebuild_database()
        self.db_tester = database_tester()
        self.db_tester.generate_fake_user(
            nick_name='tester1', password='abcdef')
        self.db_tester.generate_fake_user(
            nick_name='tester2', password='abcdef')
        self.db_helper.dump_all_data()

    def testing_get_user_list(self):
        '''
        remove password
        '''
        user_con_true = users_controller()
        ret = user_con_true.get_user_list(0)
        print ret
        assert not 'password' in ret.keys()
        print "testing_get_user_list SUCCESS"

    def testing_sign_in(self):
        '''
        :)
        '''
        user_con_true = users_controller()
        ret_true = user_con_true.sign_in('tester1', 'abcdef')
        assert ret_true

        user_con_false = users_controller()
        ret_false = user_con_false.sign_in('tester2', 'abcdefg')
        assert not ret_false

        user_con_false = users_controller()
        ret_false = user_con_false.sign_in('tester3', 'abcdef')
        assert not ret_false
        print "testing_sign_in SUCCESS"

    def testing_sign_up(self):
        '''
        :)
        '''
        user_con_true = users_controller()
        ret_true = user_con_true.sign_up('tester3', 'abcdef')
        assert ret_true

        ret = Users.query.filter_by(nick_name='tester3').count()
        assert ret == 1

        user_con_false = users_controller()
        ret_false = user_con_false.sign_up('tester1', 'abcdefg')
        assert not ret_false
        # self.db_helper.dump_all_data()

        print "testing_sign_up SUCCESS"

    def testing_reset_password(self):
        '''
        :)
        '''
        user_con_true = users_controller()
        ret_true = user_con_true.reset_password(
            'tester2', 'abcdef', 'abcdefg')
        assert ret_true

        ret_true = user_con_true.sign_in('tester2', 'abcdefg')
        assert ret_true

        ret_false = user_con_true.sign_in('tester2', 'abcdef')
        assert not ret_false

        user_con_false = users_controller()
        ret_false = user_con_false.reset_password('tester4', 'abcdefg', 'sadf')
        assert not ret_false
        # self.db_helper.dump_all_data()

        print "testing_sign_up SUCCESS"
