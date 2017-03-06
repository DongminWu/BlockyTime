

from flask_sqlalchemy import SQLAlchemy
from Initialization import Initialization
from Utilities import debug_msg


db = Initialization().get_global_db()


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
