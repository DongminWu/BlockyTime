
import sys,datetime
from flask import render_template
from Utilities import debug_msg



class Page_Generator:

    __page_path = "download.html"
    
    def __init__(self):
        debug_msg(">>> %s.%s" %( __name__,sys._getframe().f_code.co_name))

    def generatePage(self):
        return render_template(self.__page_path)

