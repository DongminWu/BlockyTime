from flask_sqlalchemy import SQLAlchemy
from Initialization import Initialization
from Utilities import debug_msg


debug_msg("Database Models")

db = Initialization().get_global_db()


class Blocks(db.Model):
    '''
    Table Blocks
    '''
    __tablename__ = 'Blocks'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    display_time = db.Column(db.String(16))
    date_id = db.Column(db.Integer, db.ForeignKey('Date.id'))
    position = db.Column(db.Integer)
    secondary_category_id = db.Column(
        db.Integer, db.ForeignKey('Secondary_Category.id'))
    primary_category_id = db.Column(
        db.Integer, db.ForeignKey('Primary_Category.id'))

    @property
    def serialize(self):
        '''
        serializing to dict
        '''
        return {
            'id':   self.id,
            'uid':   self.uid,
            'display_time':   self.display_time,
            'date_id':   self.date_id,
            'position':   self.position,
            'secondary_category_id':   self.secondary_category_id,
            'primary_category_id':   self.primary_category_id
        }

    def __repr__(self):
        return '<Blocks %r>' % self.id

class Primary_Category(db.Model):
    __tablename__ = 'Primary_Category'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    name = db.Column(db.String(64))
    color = db.Column(db.String(16))
    logo = db.Column(db.String(1024))
    secondary_category = db.relationship(
        'Secondary_Category', backref='primary_category')

    @property
    def serialize(self):
        return {
            'id':   self.id,
            'uid':   self.uid,
            'name':   self.name,
            'color':   self.color
        }

    def __repr__(self):
        return '<Primary_Category %r>' % self.id



class Secondary_Category(db.Model):
    __tablename__ = 'Secondary_Category'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    primary_id = db.Column(db.Integer, db.ForeignKey('Primary_Category.id'))
    name = db.Column(db.String(64))
    color = db.Column(db.String(16))
    logo = db.Column(db.String(1024))
    blocks = db.relationship('Blocks', backref='Secondary_category')

    @property
    def serialize(self):
        return {
            'id':   self.id,
            'uid':   self.uid,
            'primary_id':   self.primary_id,
            'name':   self.name,
            'color':   self.color
        }


    def __repr__(self):
        return '<Secondary_Category %r>' % self.id


class Date(db.Model):
    __tablename__ = 'Date'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    date = db.Column(db.Date)
    last_changed_time = db.Column(db.DateTime)
    blocks = db.relationship('Blocks', backref='date')

    # http://stackoverflow.com/questions/7102754/jsonify-a-sqlalchemy-result-set-in-flask
    @property
    def serialize(self):
        return {
            'id':   self.id,
            'uid':   self.uid,
            'date':   self.date,
            'last_changed_time':   self.last_changed_time
        }


    def __repr__(self):
        return '<Date %r>' % self.id


class Users(db.Model):
    '''
    Users table in Datebase
    '''
    __tablename__ = 'Users'
    uid = db.Column(db.Integer, primary_key=True)
    nick_name = db.Column(db.String(64))
    password = db.Column(db.String(64))

    #uid_foreignkey = db.relationship('Second_Category',backref='primary_category')

    @property
    def serialize(self):
        '''
        return list
        '''
        return {
            'uid':   self.uid,
            'nick_name':   self.nick_name,
            'password':   self.password
        }



    def __repr__(self):
        return '<Users %r>' % self.id
