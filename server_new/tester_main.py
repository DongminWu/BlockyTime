import os
import sys
import datetime
from flask import Flask, render_template
from flask_cors import CORS, cross_origin
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


from Initialization import Initialization
from MyConfig import MyConfig
from Utilities import debug_msg

Initialization().global_create_app(__name__, 'database/db_tester.sqlite')
init_app = Initialization().get_global_app()
#debug_msg("enable CORS")
#CORS(init_app, send_wildcard=True)

init_db = Initialization().global_create_db(init_app)


from DB_Model import database_helper
db_helper = database_helper.database_helper(init_db)
db_helper.rebuild_database()


from DB_Model.database_tester import database_tester

db_tester = database_tester()

db_tester.generate_fake_data()

db_tester = database_tester()

db_tester.generate_fake_data()


db_helper.dump_all_data()


migrate = Migrate(init_app, init_db)


manager = Manager(init_app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    config = MyConfig()
    debug_msg("**********************************************")
    debug_msg("           tester main ver: " +
              str(config.getConfig("version")))
    debug_msg("**********************************************")


    '''

    from testing.day_controller_tester import day_controller_tester

    day_controller_testing = day_controller_tester()
    day_controller_testing.testing_get_date_object_from_string()
    day_controller_testing.testing_get_date_object_from_id()
    day_controller_testing.testing_get_date_id_from_string()
    day_controller_testing.testing_get_last_changed_time_from_string()
    day_controller_testing.testing_get_date_list()
    day_controller_testing.testing_update_date_data()
    '''

    from testing.category_controller_tester import category_controller_tester
    category_controller_testing = category_controller_tester()
    category_controller_testing.testing_get_primary_object_list()
    category_controller_testing.testing_get_primary_object_from_id()
    category_controller_testing.testing_get_secondary_object_from_id()
    category_controller_testing.testing_get_category_list()

    # init_app.run(host='0.0.0.0', debug=True)
    manager.run()
