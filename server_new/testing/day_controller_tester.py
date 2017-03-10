import datetime
from Initialization import Initialization
from Data_Controllers.day_controller import day_controller
from DB_Model import database_helper
from DB_Model.database_tester import database_tester
from DB_Model.database_model import Date


class day_controller_tester(object):
    '''
    tester for day_controller
    '''

    def __init__(self):
        print("\n\n\n\n\n\n\n\n\n\n\n\n!!!day_controller_tester!!!")
        self.database = Initialization().get_global_db()
        self.db_helper = database_helper.database_helper(self.database)
        self.db_helper.rebuild_database()
        self.db_tester = database_tester()
        self.db_tester.generate_fake_data()
        self.db_helper.dump_all_data()

    def testing_get_date_object_from_string(self):
        '''
        should retrun an date object from string
        '''
        day_con_true = day_controller(date_string='2017-03-10', user_id='0')
        assert isinstance(day_con_true.get_date_object(), Date)
        day_con_false = day_controller(date_string='2017-03-01', user_id='0')
        assert day_con_false.get_date_object() is None
        day_con_false = day_controller(date_string='2017-03-10', user_id='1')
        assert day_con_false.get_date_object() is None
        print "testing_get_date_object_from_string SUCCESS"

    def testing_get_date_object_from_id(self):
        '''
        should retrun an date object from date id
        '''
        day_con_true = day_controller(id=0, user_id='0')
        assert isinstance(day_con_true.get_date_object(), Date)
        day_con_false = day_controller(id=1, user_id='0')
        assert day_con_false.get_date_object() is None
        day_con_false = day_controller(id=0, user_id='1')
        assert day_con_false.get_date_object() is None
        print "testing_get_date_object_from_id SUCCESS"

    def testing_get_date_id_from_string(self):
        '''
        None : error
        >=0: success
        '''
        day_con_true = day_controller(date_string='2017-03-10', user_id='0')
        assert day_con_true.get_date_id() >= 0
        day_con_false = day_controller(date_string='2017-03-01', user_id='0')
        assert day_con_false.get_date_id() is None
        print "testing_get_date_id_from_string SUCCESS"

    def testing_get_last_changed_time_from_string(self):
        '''
        None : error
        datetime: success
        '''
        day_con_true = day_controller(date_string='2017-03-10', user_id='0')
        assert isinstance(
            day_con_true.get_last_changed_time(), datetime.datetime)
        day_con_false = day_controller(date_string='2017-03-01', user_id='0')
        assert day_con_false.get_last_changed_time() is None
        print "testing_get_last_changed_time_from_string SUCCESS"

    def testing_get_date_list(self):
        '''
        all value should be string
        '''
        day_con_true = day_controller(date_string='2017-03-10', user_id='0')
        return_list = day_con_true.get_date_list()
        assert return_list != {}
        assert return_list['date'] == '2017-03-10'
        assert return_list['uid'] == 0
        assert return_list['last_changed_time']
        assert isinstance(return_list['id'], int)
        print "testing_get_date_list SUCCESS"

    def testing_update_date_data(self):
        '''
        compare the data between return value and the value in database
        '''
        day_con_true = day_controller(date_string='2017-03-10', user_id='0')
        return_time = day_con_true.update_day_data(None)

        query_day_con = day_controller(date_string='2017-03-10', user_id='0')
        query_time = query_day_con.get_last_changed_time()
        assert return_time == query_time

        '''
        if we gave a wrong date, should return None
        '''
        day_con_false = day_controller(date_string='2017-03-01', user_id='0')
        assert day_con_false.update_day_data(None) is None

        print "testing_update_date_data SUCCESS"
