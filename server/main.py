from flask import Flask, render_template
from MyConfig import MyConfig
from Utilities import debug_msg
from ViewMainPage import ViewMainPage


view = ViewMainPage()

app = Flask(__name__)
@app.route('/')
def index():
    return view.generatePage();

if __name__ == '__main__':
    config = MyConfig()
    debug_msg("BlockyTime Version: "+str(config.getConfig("version")))
    app.run()

