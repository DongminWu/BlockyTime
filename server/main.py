import os,sys,datetime
from flask import Flask, render_template
from flask_cors import CORS, cross_origin
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand



from Initialization import Initialization
from MyConfig import MyConfig
from Utilities import debug_msg

Initialization().global_create_app(__name__);
init_app = Initialization().get_global_app();
debug_msg("enable CORS")
#CORS(init_app, send_wildcard = True)

init_db = Initialization().global_create_db(init_app);



'''
datamodel initialization
'''
from ModelMainPage import ModelMainPage,Users,Primary_Category,Second_Category,Date,Blocks
ModelMainPage().initialize_database(init_db)

from ViewMainPage import ViewMainPage
view = ViewMainPage()

from ControllerMainPage import ControllerMainPage
ControllerMainPage().initialize_api()



migrate = Migrate(init_app, init_db)

manager = Manager(init_app)
manager.add_command('db', MigrateCommand)
'''
add some env to shell command
'''
def my_make_context ():
    return dict(Initialization = Initialization,
                      ModelMainPage = ModelMainPage,
                      ViewMainPage = ViewMainPage,
                      ControllerMainPage = ControllerMainPage,
                      Users = Users,
                      Primary_Category = Primary_Category,
                      Second_Category = Second_Category,
                      Date = Date,
                      Blocks = Blocks)

manager.add_command('shell', Shell(make_context=my_make_context))




def test_import():
    from Initialization import Initialization
    from ModelMainPage import ModelMainPage


@init_app.route('/',methods=['GET','POST','OPTIONS'])
def index():
    return view.generatePage();



if __name__ == '__main__':
    config = MyConfig()
    debug_msg("**********************************************")
    debug_msg("             BlockyTime Version: "+str(config.getConfig("version")))
    debug_msg("**********************************************")

    print(ModelMainPage().get_Date(datetime.date(2016,12,28)))
    ModelMainPage().get_Blocks_from_date_id(0)
    ModelMainPage().get_Second_Category_from_id(0)
    ModelMainPage().get_Primary_Category_from_id(0)
    ModelMainPage().get_all_Category()
    print(ModelMainPage().get_block_info_from_date(datetime.date(2016,12,30)))


    #init_app.run(host='0.0.0.0',debug=True)
    manager.run()

