import datetime
from Initialization import Initialization
from Data_Controllers.statistic_controller import statistic_controller
from Data_Controllers.blocks_controller import blocks_controller
from DB_Model import database_helper
from DB_Model.database_tester import database_tester

from DB_Model.database_model import Users


class statistic_controller_tester(object):
    '''
    tester for day_controller
    '''

    def __init__(self):
        print("\n\n\n\n\n\n\n\n\n\n\n\n!!!statics_controller_tester!!!")
        self.database = Initialization().get_global_db()
        self.db_helper = database_helper.database_helper(self.database)
        self.db_helper.rebuild_database()
        self.db_tester = database_tester()
        self.db_tester.generate_fake_data()
        new_pri = self.db_tester.generate_fake_primary_category()
        new_sec = self.db_tester.generate_fake_secondary_category(new_pri)
        new_sec = self.db_tester.generate_fake_secondary_category(new_pri)
        new_sec = self.db_tester.generate_fake_secondary_category(new_pri)
        new_pri = self.db_tester.generate_fake_primary_category()
        new_sec = self.db_tester.generate_fake_secondary_category(new_pri)
        new_sec = self.db_tester.generate_fake_secondary_category(new_pri)
        new_sec = self.db_tester.generate_fake_secondary_category(new_pri)
        blocks_con = blocks_controller('0')
        blocks_con.update_a_block(1, 2)
        blocks_con.update_a_block(2, 1)
        blocks_con.update_a_block(3, 4)
        blocks_con.update_a_block(4, 4)
        blocks_con.update_a_block(5, 6)
        blocks_con.update_a_block(6, 5)
        self.db_helper.dump_all_data()

    def testing_get_statistic_list_day(self):
        '''
        :)
        '''
        statistic_con_true = statistic_controller('0')
        ret = statistic_con_true.get_statistic_list_day('2017-03-10')
        total_pri_hours = 0
        total_sec_hours = 0
        total_pri_presentage = 0
        total_sec_presentage = 0
        for each_pri in ret:
            total_pri_hours += float(each_pri['hours'])
            total_pri_presentage += float(each_pri['presentage'])
            for each_sec in each_pri['secondary_category']:
                total_sec_hours += float(each_sec['hours'])
                total_sec_presentage += float(each_sec['presentage'])
        print ret
        print total_pri_presentage
        print total_sec_presentage
        assert total_pri_hours == 24
        assert total_sec_hours == 24
        # TODO: not 100 issue!!!
        assert 98 <= total_sec_presentage <= 100
        assert 98 <= total_pri_presentage <= 100
