import os, sys, time,datetime


from flask_sqlalchemy import SQLAlchemy
from Initialization import Initialization
from Utilities import debug_msg


db = Initialization().get_global_db();

class Primary_Category(db.Model):
    __tablename__ = 'Primary_Category'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Unicode(64))
    color = db.Column(db.Integer)
    logo = db.Column(db.String(1024))
    second_category = db.relationship('Second_Category',backref='primary_category')

    def __repr__(self):
        return '<Primary_Category %r>' % self.id


class Second_Category(db.Model):
    __tablename__ = 'Second_Category'
    id = db.Column(db.Integer, primary_key = True)
    primary_id = db.Column(db.Integer, db.ForeignKey('Primary_Category.id'))
    name = db.Column(db.Unicode(64))
    color = db.Column(db.Integer)
    logo = db.Column(db.String(1024))
    blocks = db.relationship('Blocks',backref = 'second_category')

    def __repr__(self):
        return '<Second_Category %r>' % self.id

class Date(db.Model):
    __tablename__ = 'Date'
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date)
    last_changed_time = db.Column(db.DateTime)
    blocks = db.relationship('Blocks',backref = 'date')

    def __repr__(self):
        return '<Date %r>' % self.id


class Blocks(db.Model):
    __tablename__ = 'Blocks'
    id = db.Column(db.Integer, primary_key = True)
    date_id = db.Column(db.Integer,db.ForeignKey('Date.id'))
    display_time = db.Column(db.String(16))
    position = db.Column(db.Integer)
    second_category_id = db.Column(db.Integer,db.ForeignKey('Second_Category.id'))

    def __repr__(self):
        return '<Blocks %r>' % self.id




class ModelMainPage:
    class __ModelMainPage:
        db = None
        def __init__(self):
            pass
        def initialize_database(self, db):
            debug_msg(">>> %s.%s" %( __name__,sys._getframe().f_code.co_name))
            self.db = db
            db.create_all();
            debug_msg("Primary_Category: %d" % Primary_Category.query.count())
            debug_msg("Second_Category: %d" % Second_Category.query.count())
            debug_msg("Date: %d" % Date.query.count())
            debug_msg("Blocks: %d" % Blocks.query.count())
            new_pri_cata = Primary_Category(id = 0, name = u"test", color =
                                            0,logo = "yo")
            new_sec_cata = Second_Category(id = 0, name = u"test", color = 0,
                                           logo = "hello", primary_id = 0)
            
            #following codes are only used for testing
            '''
            self.db.session.add(new_pri_cata)
            self.db.session.add(new_sec_cata)
            self.db.session.commit()
            '''

        def create_an_empty_day(self,input_time):
            debug_msg(">>> %s.%s" %( __name__,sys._getframe().f_code.co_name))
            if not db == None:
                formatted_date = datetime.date(input_time.tm_year,input_time.tm_mon,input_time.tm_mday)
                if 0== Date.query.filter_by(date=formatted_date).count():
                    debug_msg("This is a brand new day!!")

                    last_changed_time = time.localtime()
                    last_changed_time_formatted = datetime.datetime\
                        (last_changed_time.tm_year,\
                        last_changed_time.tm_mon,\
                        last_changed_time.tm_mday,\
                        last_changed_time.tm_hour,\
                        last_changed_time.tm_min,\
                        last_changed_time.tm_sec) 
                    
                    new_date_id = Date.query.count() 
                    new_date = Date(id = new_date_id,\
                                    date = formatted_date,\
                                   last_changed_time =  last_changed_time_formatted\
                                   )
                    self.db.session.add(new_date)
                    debug_msg("new Date id: %d,date: %s,last_changed_time :%s" %
                              (new_date.id,new_date.date,new_date.last_changed_time))
                    self.db.session.commit()
                    debug_msg("committed")

                    new_block={}
                    new_blocks_start_id = Blocks.query.count()
                    for index in range(new_blocks_start_id, new_blocks_start_id+48):
                        pos = index - new_blocks_start_id
                        print pos
                        display_time = "%02d:%02d" % (pos/2, (pos%2)*30)
                        new_block[pos] = Blocks(id = index,date_id =new_date_id,\
                                           display_time = display_time,\
                                          position = pos,\
                                           second_category_id = 0 \
                                          )
                        self.db.session.add(new_block[pos])
                        debug_msg("new Blocks[%d] id: %d,date_id: %s,display_time: %s,pos: %d, second_category_id: %d"%
                              (pos,new_block[pos].id,\
                                new_block[pos].date_id,\
                                new_block[pos].display_time,\
                                new_block[pos].position,\
                                new_block[pos].second_category_id))


                    self.db.session.commit()
                    debug_msg("committed")
                else:
                    debug_msg("this day already existed")

        def create_today(self):
            self.create_an_empty_day(time.localtime())

                    



                


    #for singleton
    instance = None
    def __init__(self):
        debug_msg(">>> %s.%s" %( __name__,sys._getframe().f_code.co_name))
        if not ModelMainPage.instance:
            ModelMainPage.instance = ModelMainPage.__ModelMainPage()
            
    def __getattr__(self,name):
        return getattr(self.instance, name)




