import os, sys


from flask_sqlalchemy import SQLAlchemy
from Initialization import Initialization
from Utilities import debug_msg


db = Initialization().get_global_db();

class Primary_Category(db.Model):
    __tablename__ = 'Primary_Category'
    Category_Id = db.Column(db.Integer, primary_key = True)
    Category_Name = db.Column(db.Unicode(64))
    Color = db.Column(db.Integer)
    Logo = db.Column(db.String(256))

    def __repr__(self):
        return '<Primary_Category %r>' % self.name



class ModelMainPage:
    class __ModelMainPage:
        def __init__(self):
            pass
        def initialize_database(self, db):
            self.db = db
            db.create_all();

    #for singleton
    instance = None
    def __init__(self):
        debug_msg(">>> %s.%s" %( __name__,sys._getframe().f_code.co_name))
        if not ModelMainPage.instance:
            ModelMainPage.instance = ModelMainPage.__ModelMainPage()
            
    def __getattr__(self,name):
        return getattr(self.instance, name)




