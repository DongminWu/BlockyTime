import os,sys,time
from flask import Flask, render_template



from Initialization import Initialization
from MyConfig import MyConfig
from Utilities import debug_msg
from ViewMainPage import ViewMainPage








view = ViewMainPage()





Initialization().global_create_app(__name__);
app = Initialization().get_global_app();

db = Initialization().global_create_db(app);

from ModelMainPage import ModelMainPage
#datamodel initialization
ModelMainPage().initialize_database(db)


@app.route('/')
def index():
    return view.generatePage();



if __name__ == '__main__':
    config = MyConfig()
    debug_msg("BlockyTime Version: "+str(config.getConfig("version")))

    ModelMainPage().create_an_empty_day(time.strptime("2016-12-27 00:00:00",
                                                      "%Y-%m-%d %H:%M:%S"));
#    app.run()

