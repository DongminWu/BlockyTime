
import sys,datetime
from flask import render_template
from Utilities import debug_msg
from ModelMainPage import ModelMainPage



class ViewMainPage:

    __page_path = "download.html"
    
    def __init__(self):
        debug_msg(">>> %s.%s" %( __name__,sys._getframe().f_code.co_name))

    def generatePage(self):
        formatted_datetime = datetime.date.today()
        info =  ModelMainPage().get_block_info_from_date(formatted_datetime)
        if info is None:
            result=ModelMainPage().create_an_empty_day(formatted_datetime)
            if result is None:
                return "Error creating empty day",400
        string_date = str(formatted_datetime)
        category_list = ModelMainPage().get_all_Category()
        return render_template(self.__page_path, date=string_date,category_list = category_list)

