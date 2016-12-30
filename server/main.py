import os,sys,datetime
from flask import Flask, render_template



from Initialization import Initialization
from MyConfig import MyConfig
from Utilities import debug_msg
from ViewMainPage import ViewMainPage








view = ViewMainPage()





Initialization().global_create_app(__name__);
init_app = Initialization().get_global_app();

init_db = Initialization().global_create_db(init_app);

from ModelMainPage import ModelMainPage
#datamodel initialization
ModelMainPage().initialize_database(init_db)

from ControllerMainPage import ControllerMainPage
ControllerMainPage().initialize_api()

def test_import():
    from Initialization import Initialization
    from ModelMainPage import ModelMainPage


@init_app.route('/')
def index():
    return view.generatePage();



if __name__ == '__main__':
    config = MyConfig()
    debug_msg("**********************************************")
    debug_msg("             BlockyTime Version: "+str(config.getConfig("version")))
    debug_msg("**********************************************")

    ModelMainPage().get_Date(datetime.date(2016,12,28));
    ModelMainPage().get_Blocks_from_date_id(0)
    ModelMainPage().get_Second_Category_from_id(0)
    ModelMainPage().get_Primary_Category_from_id(0)
    ModelMainPage().get_all_Category()
    ModelMainPage().get_block_info_from_date(datetime.date(2016,12,28));


    init_app.run(debug=True)

