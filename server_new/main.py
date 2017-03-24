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

Initialization().global_create_app(__name__, None)
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


from Data_Controllers.blocks_controller import blocks_controller

new_pri = db_tester.generate_fake_primary_category()
new_sec = db_tester.generate_fake_secondary_category(new_pri)
new_sec = db_tester.generate_fake_secondary_category(new_pri)
new_sec = db_tester.generate_fake_secondary_category(new_pri)
new_pri = db_tester.generate_fake_primary_category()
new_sec = db_tester.generate_fake_secondary_category(new_pri)
new_sec = db_tester.generate_fake_secondary_category(new_pri)
new_sec = db_tester.generate_fake_secondary_category(new_pri)
blocks_con = blocks_controller('0')
blocks_con.update_a_block(1, 2)
blocks_con.update_a_block(2, 1)
blocks_con.update_a_block(3, 4)
blocks_con.update_a_block(4, 4)
blocks_con.update_a_block(5, 6)
blocks_con.update_a_block(6, 5)

db_helper.dump_all_data()


'''
datamodel initialization
'''
'''
from ModelMainPage import ModelMainPage, Users, Primary_Category, Second_Category, Date, Blocks
ModelMainPage().initialize_database(init_db)

from ViewMainPage import ViewMainPage
view=ViewMainPage()

'''
from RESTful_Interface import RESTful_Interface
RESTful_Interface().initialize_api()


migrate = Migrate(init_app, init_db)


manager = Manager(init_app)
manager.add_command('db', MigrateCommand)


'''
add some env to shell command
'''

'''
def my_make_context():
    return dict(Initialization=Initialization,
                ModelMainPage=ModelMainPage,
                ViewMainPage=ViewMainPage,
                ControllerMainPage=ControllerMainPage,
                Users=Users,
                Primary_Category=Primary_Category,
                Second_Category=Second_Category,
                Date=Date,
                Blocks=Blocks)


manager.add_command('shell', Shell(make_context=my_make_context))





@init_app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def index():
    return view.generatePage()

'''

if __name__ == '__main__':
    config = MyConfig()
    debug_msg("**********************************************")
    debug_msg("           BlockyTime Version: " +
              str(config.getConfig("version")))
    debug_msg("**********************************************")

    init_app.run(host=config.getConfig("host"),port=config.getConfig("port"), debug=True)
    manager.run()
