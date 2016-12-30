import os, sys, time,datetime,copy,json
from flask import request
from flask_restful import Resource, Api

from Initialization import Initialization
from ModelMainPage import ModelMainPage

from Utilities import debug_msg







#########



class Resource_Date(Resource):
    def get(self, date):
        formatted_datetime = datetime.datetime.strptime(date,"%Y-%m-%d").date()
        info =  ModelMainPage().get_block_info_from_date(formatted_datetime)
        if info is None:
            result=ModelMainPage().create_an_empty_day(formatted_datetime)
            if result is None:
                return "Error creating empty day",400
        info =  ModelMainPage().get_block_info_from_date(formatted_datetime)
        ret = json.dumps(info)
        return ret
        


class Resource_Category(Resource):
    def get(self):
        info = ModelMainPage().get_all_Category()
        ret = json.dumps(info)
        return ret

class Resource_Blocks(Resource):
    def get(self,data):
        info = ModelMainPage().get_Blocks_from_date_id(data)
        ret = json.dumps(info)
        return ret
    def post(self , data):
        decoded = json.loads(request.form['data'])
        if decoded == None:
            return "None data",400
        if type(decoded) != type([]) :
            return "Data type error",400
        for each in decoded :
            ret = ModelMainPage().update_a_block(each)
            if ret != 0:
                return "Date error!",400
        return "upload success",200

        

class ControllerMainPage:
    class __ControllerMainPage:
        app = None
        api = None
        def __init__(self):
            pass
        def initialize_api(self):
            self.app = Initialization().get_global_app();
            self.api = Api(self.app)
            self.api.add_resource(Resource_Date,"/Date/<string:date>")
            self.api.add_resource(Resource_Category,"/Category/")
            self.api.add_resource(Resource_Blocks,"/Blocks/<int:data>")




    #for singleton
    instance = None
    def __init__(self):
        if not ControllerMainPage.instance:
            ControllerMainPage.instance = ControllerMainPage.__ControllerMainPage()
            
    def __getattr__(self,name):
        return getattr(self.instance, name)
