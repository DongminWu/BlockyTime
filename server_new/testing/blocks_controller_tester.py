import datetime
from Initialization import Initialization
from Data_Controllers.blocks_controller import blocks_controller
from DB_Model import database_helper
from DB_Model.database_tester import database_tester
from DB_Model.database_model import Blocks
from DB_Model.database_model import Users


class blocks_controller_tester(object):
    '''
    tester for day_controller
    '''

    def __init__(self):
        print("\n\n\n\n\n\n\n\n\n\n\n\n!!!users_controller_tester!!!")
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

    def testing_get_blocks_list_of_a_day(self):
        '''
        :)
        '''
        blocks_con_tester = blocks_controller('0')
        assert len(blocks_con_tester.get_blocks_list_of_a_day(
            '2017-03-10')) == 48
        print "testing_get_blocks_list_of_a_day SUCCESS  <<<<<<<<<<<<<<<<<<<<<<"

    def testing_update_a_block(self):
        '''
        :)
        '''
        blocks_con_tester = blocks_controller('0')
        blocks_con_tester.update_a_block('1', '1')
        ret_obj = Blocks.query.filter_by(id=1).first()
        assert ret_obj.secondary_category_id == 1
        assert ret_obj.primary_category_id == 1

        blocks_con_tester.update_a_block(2, 2)
        ret_obj = Blocks.query.filter_by(id=2).first()
        assert ret_obj.secondary_category_id == 2
        assert ret_obj.primary_category_id == 1

        #there is no secondary_category_id = 6, not update,no crashing
        blocks_con_tester.update_a_block(3, 6)
        ret_obj = Blocks.query.filter_by(id=3).first()
        assert ret_obj.secondary_category_id == 0
        assert ret_obj.primary_category_id == 0
        print "testing_update_a_block SUCCESS  <<<<<<<<<<<<<<<<<<<<<<"
