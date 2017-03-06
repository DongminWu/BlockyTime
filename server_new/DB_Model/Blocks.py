from flask_sqlalchemy import SQLAlchemy
from Initialization import Initialization
from Utilities import debug_msg


debug_msg("_____blocks______")

db = Initialization().get_global_db()


class Blocks(db.Model):
    '''
    Table Blocks
    '''
    __tablename__ = 'Blocks'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    display_time = db.Column(db.String(16))
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
            'position':   self.position,
            'secondary_category_id':   self.secondary_category_id,
            'primary_category_id':   self.primary_category_id
        }

    def __repr__(self):
        return '<Blocks %r>' % self.id
