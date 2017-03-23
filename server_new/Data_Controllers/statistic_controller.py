import datetime
import sys
from flask_sqlalchemy import SQLAlchemy
from Utilities import debug_msg


from Initialization import Initialization
from DB_Model.database_model import Users
from DB_Model.database_helper import database_helper
from Data_Controllers.day_controller import day_controller
from Data_Controllers.blocks_controller import blocks_controller

half_hour = 0.5
hours_of_a_day = 24  # 24hrs one day
presentage_of_half_hour = float(half_hour / hours_of_a_day) * 100


class statistic_controller(object):
    '''
    initializing with uid

    get statistic information of day, month, year
    '''

    def __init__(self, uid):
        '''
        :)
        '''
        debug_msg(">>> %s.%s" % (__name__, sys._getframe().f_code.co_name))
        self.database = Initialization().get_global_db()
        self.db_helper = database_helper(self.database)
        self.uid = uid

    def __create_secondary_data_slot(self, query_list, secondary_category_id):
        insert = {'secondary_category_id': secondary_category_id, 'hours': 0,
                  'presentage': 0}
        if query_list == []:
            query_list.append(insert)
        else:
            for each in query_list:
                if each['secondary_category_id'] == secondary_category_id:
                    return
            query_list.append(insert)
        return

    def __create_data_slot(self, query_list, primary_category_id, secondary_category_id):
        insert = {'primary_category_id': primary_category_id, 'hours': 0,
                  'presentage': 0, 'secondary_category': []}
        if query_list == []:
            query_list.append(insert)
        else:
            for each in query_list:
                if each['primary_category_id'] == primary_category_id:
                    self.__create_secondary_data_slot(
                        each['secondary_category'], secondary_category_id)
                    return
            query_list.append(insert)
        for each in query_list:
            if each['primary_category_id'] == primary_category_id:
                self.__create_secondary_data_slot(
                    each['secondary_category'], secondary_category_id)
        return

    def __increase_secondary_hours(self, query_list, secondary_category_id):
        for each_primary in query_list:
            for each in each_primary['secondary_category']:
                if each['secondary_category_id'] == secondary_category_id:
                    each['hours'] = str(float(each['hours']) + half_hour)

    def __increase_primary_hours(self, query_list, primary_category_id):
        for each in query_list:
            if each['primary_category_id'] == primary_category_id:
                each['hours'] = str(float(each['hours']) + half_hour)

    def __calculate_presentage(self, query_list):
        for each_pri in query_list:
            each_pri['presentage'] = str(
                int(float(each_pri['hours']) / hours_of_a_day * 100))
            for each_sec in each_pri['secondary_category']:
                each_sec['presentage'] = str(
                    int(float(each_sec['hours']) / hours_of_a_day * 100))

    def get_statistic_list_day(self, day_string):
        '''
        get list
        '''
        blocks_con = blocks_controller(self.uid)
        blocks_objs = blocks_con.get_blocks_objects_of_a_day(day_string)

        ret = []
        for each_block in blocks_objs:
            self.__create_data_slot(ret, each_block.primary_category_id,
                                    each_block.secondary_category_id)

        for each_block in blocks_objs:
            self.__increase_primary_hours(ret, each_block.primary_category_id)
            self.__increase_secondary_hours(
                ret, each_block.secondary_category_id)

        self.__calculate_presentage(ret)

        return ret
