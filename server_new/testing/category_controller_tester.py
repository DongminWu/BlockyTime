import datetime
from Initialization import Initialization
from Data_Controllers.category_controller import category_controller
from DB_Model import database_helper
from DB_Model.database_tester import database_tester
from DB_Model.database_model import Secondary_Category
from DB_Model.database_model import Primary_Category


class category_controller_tester(object):
    def __init__(self):
        print("\n\n\n\n\n\n\n\n\n\n\n\n!!!category_controller_tester!!!")
        self.database = Initialization().get_global_db()
        self.db_helper = database_helper.database_helper(self.database)
        self.db_helper.rebuild_database()
        self.db_tester = database_tester()
        self.db_tester.generate_fake_data()
        new_pri = self.db_tester.generate_fake_primary_category()
        new_sec = self.db_tester.generate_fake_secondary_category(new_pri)
        new_sec = self.db_tester.generate_fake_secondary_category(new_pri)
        new_sec = self.db_tester.generate_fake_secondary_category(new_pri)
        self.db_helper.dump_all_data()

    def testing_get_primary_object_list(self):
        '''
        :)
        '''
        cate_con_true = category_controller(user_id='0')
        cate_con_ture_pri_list = cate_con_true.get_primary_object_list()
        assert len(cate_con_ture_pri_list) == 2
        assert isinstance(cate_con_ture_pri_list[0], Primary_Category)
        print cate_con_ture_pri_list

        cate_con_false = category_controller(user_id='10')
        cate_con_false_pri_list = cate_con_false.get_primary_object_list()
        assert cate_con_false_pri_list == -1
        print "testing_get_primary_object_list SUCCESS  <<<<<<<<<<<<<<<<<<<<<<"

    def testing_get_primary_object_from_id(self):
        '''
        :)
        '''
        cate_con_true = category_controller(user_id='0')
        ret = cate_con_true.get_primary_object_from_id('0')
        assert isinstance(ret, Primary_Category)
        print ret.serialize

        cate_con_false = category_controller(user_id='10')
        ret = cate_con_false.get_primary_object_from_id('0')
        assert ret == -1

        cate_con_false = category_controller(user_id='0')
        ret = cate_con_false.get_primary_object_from_id('10')
        assert ret == -1
        print "testing_get_primary_object_from_id SUCCESS  <<<<<<<<<<<<<<<<<<<<<<"

    def testing_get_secondary_object_from_id(self):
        cate_con_true = category_controller(user_id='0')
        ret = cate_con_true.get_secondary_object_from_id('0')
        assert isinstance(ret, Secondary_Category)
        print ret.serialize

        cate_con_false = category_controller(user_id='10')
        ret = cate_con_false.get_secondary_object_from_id('0')
        assert ret == -1

        cate_con_false = category_controller(user_id='0')
        ret = cate_con_false.get_secondary_object_from_id('10')
        assert ret == -1
        print "testing_get_secondary_object_from_id SUCCESS  <<<<<<<<<<<<<<<<<<<<<<"

    def testing_get_category_list(self):
        '''
        :)
        '''
        cate_con_true = category_controller(user_id='0')
        ret0 = cate_con_true.get_category_list()
        print ret0
