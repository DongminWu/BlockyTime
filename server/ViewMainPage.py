
from flask import render_template
from Utilities import debug_msg
import sys



class ViewMainPage:

    __page_path = "download.html"
    
    def __init__(self):
        debug_msg(">>> %s.%s" %( __name__,sys._getframe().f_code.co_name))

    def generatePage(self):
        return render_template(self.__page_path)

