import sys
import datetime
from flask_sqlalchemy import SQLAlchemy
from Initialization import Initialization
from Utilities import debug_msg


from DB_Model.database_model import Users, Date, Blocks, Primary_Category, Secondary_Category
from DB_Model.database_helper import database_helper
from Initialization import Initialization


class database_tester(object):
    '''
    testing class
    '''

    def __init__(self):

        self.database = Initialization().get_global_db()
        self.helper = database_helper(self.database)
        debug_msg(">>> %s.%s" % (__name__, sys._getframe().f_code.co_name))

        self.uid = Users.query.count()
        self.nick_name = 'fake_user' + str(self.uid)
        self.password = '123@123' + str(self.uid)

        self.primary_id = Primary_Category.query.count()
        self.primary_name = 'fake_category' + str(self.primary_id)
        self.primary_color = '#f23456'
        self.primary_logo = './logo.png'

        self.secondary_id = Secondary_Category.query.count()
        self.secondary_name = 'fake_secondary' + str(self.secondary_id)
        self.secondary_color = "#b33321"
        self.secondary_logo = './secondary_logo.png'

        self.date_id = Date.query.count()
        self.date_date = datetime.date.today()
        self.date_last_changed_time = datetime.datetime.now()

        self.blocks_id = Blocks.query.count()

    def generate_fake_data(self):
        '''
        generate data
        '''
        new_user = Users(uid=self.uid, nick_name=self.nick_name,
                         password=self.password)
        self.helper.update_data(new_user)

        new_primary = Primary_Category(
            id=self.primary_id, uid=self.uid, name=self.primary_name,
            color=self.primary_color, logo=self.primary_logo)

        self.helper.update_data(new_primary)

        new_secondary = Secondary_Category(
            id=self.secondary_id, uid=self.uid, primary_id=self.primary_id,
            name=self.secondary_name, color=self.secondary_color, logo=self.secondary_logo)
        self.helper.update_data(new_secondary)

        new_date = Date(
            id=self.date_id, uid=self.uid, date=self.date_date,
            last_changed_time=self.date_last_changed_time)
        self.helper.update_data(new_date)

        index = 0
        new_block = {}
        for index in range(self.blocks_id, self.blocks_id + 48):
            pos = index - self.blocks_id
            display_time = "%02d:%02d" % (pos / 2, (pos % 2) * 30)
            new_block[pos] = Blocks(id=index, date_id=self.date_id,
                                    display_time=display_time,
                                    position=pos, uid=self.uid,
                                    secondary_category_id=self.secondary_id,
                                    primary_category_id=self.primary_id)
            self.helper.update_data(new_block[pos])

    def generate_fake_primary_category(self):
        '''
        return primary id
        '''
        primary_id = Primary_Category.query.count()
        primary_name = 'fake_category' + str(primary_id)
        primary_color = '#f23456'
        primary_logo = './logo' + str(primary_id) + '.png'
        new_primary = Primary_Category(
            id=primary_id, uid=self.uid, name=primary_name,
            color=primary_color, logo=primary_logo)
        self.helper.update_data(new_primary)
        return primary_id

    def generate_fake_secondary_category(self, primary_id):
        '''
        :)
        '''
        secondary_id = Secondary_Category.query.count()
        secondary_name = 'fake_secondary' + str(secondary_id)
        secondary_color = "#b33321"
        secondary_logo = './logo' + str(secondary_id) + '.png'
        new_secondary = Secondary_Category(
            id=secondary_id, uid=self.uid, primary_id=primary_id,
            name=secondary_name, color=secondary_color, logo=secondary_logo)
        self.helper.update_data(new_secondary)
        return secondary_id
