
from flask_sqlalchemy import SQLAlchemy
from Initialization import Initialization
from Utilities import debug_msg


db = Initialization().get_global_db()


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
