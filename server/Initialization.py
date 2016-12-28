import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from MyConfig import MyConfig
from Utilities import debug_msg




class Initialization:
    class __Initialization:
        app = None
        db = None
        
        def global_create_app(self,name):
            basedir = os.path.abspath(os.path.dirname(__file__))
            if (name == None):
                debug_msg("Warning: no app name!")
                name = '__main__'
            
            app = Flask(name)
            app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'database/data.sqlite')
            app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
            self.app = app
            return app
        
        def global_create_db(self,app):
            db = SQLAlchemy(app)
            self.db = db
            return db

        def __init__(self):
            pass
            
            

        def get_global_app(self):
            return self.app

        def get_global_db(self):
            return self.db


    #for singleton
    instance = None
    def __init__(self):
        if not Initialization.instance:
            Initialization.instance = Initialization.__Initialization()
            
    def __getattr__(self,name):
        return getattr(self.instance, name)
    
    
    



