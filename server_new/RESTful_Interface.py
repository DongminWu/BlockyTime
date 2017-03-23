import os
import sys
import time
import datetime
import copy
import json
from flask import request
from flask_restful import Resource, Api

from Initialization import Initialization

from Utilities import debug_msg

from Data_Controllers.day_controller import day_controller
from Data_Controllers.users_controller import users_controller
from Data_Controllers.statistic_controller import statistic_controller
from Data_Controllers.category_controller import category_controller
from Data_Controllers.blocks_controller import blocks_controller

#########


class mainpage_date(Resource):
    def get(self, uid, date):
        ret = {}

        blocks_con = blocks_controller(uid)
        ret['blocks'] = blocks_con.get_blocks_list_of_a_day(date)

        category_con = category_controller(user_id=uid)
        ret['category'] = category_con.get_category_list()

        statistic_con = statistic_controller(uid)
        ret_statistics = {}
        ret_statistics['Day'] = statistic_con.get_statistic_list_day(date)
        ret['statistic'] = ret_statistics

        day_con = day_controller(user_id=uid, date_string=date)
        ret['date'] = day_con.get_date_list()

        users_con = users_controller()
        ret['users'] = users_con.get_user_list(uid)

        return ret

    def post(self):
        return 'hello'


class Resource_Date(Resource):
    def get(self, date):
        formatted_datetime = datetime.datetime.strptime(
            date, "%Y-%m-%d").date()
        info = ModelMainPage().get_block_info_from_date(formatted_datetime)
        if info is None:
            result = ModelMainPage().create_an_empty_day(formatted_datetime)
            if result is None:
                return "Error creating empty day", 400
        info = ModelMainPage().get_block_info_from_date(formatted_datetime)
        ret = json.dumps(info)
        return ret


class Resource_Category(Resource):
    def get(self):
        info = ModelMainPage().get_all_Category()
        ret = json.dumps(info)
        return ret


class Resource_Blocks(Resource):
    def get(self, data):
        info = ModelMainPage().get_Blocks_from_date_id(data)
        ret = json.dumps(info)
        return ret

    def post(self, data):
        decoded = json.loads(request.form['data'])
        if decoded == None:
            return "None data", 400
        if type(decoded) != type([]):
            return "Data type error", 400
        for each in decoded:
            ret = ModelMainPage().update_a_block(each)
            if ret != 0:
                return "Date error!", 400
        return "upload success", 200


class RESTful_Interface:
    class __RESTful_Interface:
        app = None
        api = None

        def __init__(self):
            pass

        def initialize_api(self):
            self.app = Initialization().get_global_app()
            self.api = Api(self.app)
            self.api.add_resource(
                mainpage_date, "/MainPage/<int:uid>/date/<string:date>")

    # for singleton
    instance = None

    def __init__(self):
        if not RESTful_Interface.instance:
            RESTful_Interface.instance = RESTful_Interface.__RESTful_Interface()

    def __getattr__(self, name):
        return getattr(self.instance, name)
