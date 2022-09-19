'''
----------------------------------------------------------------------------
"THE BEER-WARE LICENSE" (Revision 42):
github.com/dnzlr; wrote this file. As long as you retain this notice you
can do whatever you want with this stuff. If we meet some day, and you think
this stuff is worth it, you can buy me a beer in return. The Wover
----------------------------------------------------------------------------
'''
from flask import Flask, render_template, request
import datetime
import yps_led as yl

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M:%S")
    timeYear = now.strftime("%Y")

    templateData = {'time': timeString, 'timeYear': timeYear}

    #return 'Hello world'
    return render_template('index.html', **templateData)

@app.route("/<action>")
def action(action):
    if action == "on":
        yl.ypsCol(yl.ledObject, yl.WHITE)
    if action == "off":
        yl.wheelOff()
        #yl.ypsCol(yl.ledObject, yl.OFF)
    if action == "red":
        yl.ypsCol(yl.ledObject, yl.RED)
    if action == "green":
        yl.ypsCol(yl.ledObject, yl.GREEN)
    if action == "blue":
        yl.ypsCol(yl.ledObject, yl.BLUE)
    if action == "pink":
        yl.ypsCol(yl.ledObject, yl.PINK)
    if action == "rainbow":
        yl.rainbowCycle(yl.ledObject)

    return render_template('index.html')

'''
@app.route('/cakes')
def cakes():
    #return 'Yummy cakes!'
    return render_template('cakes.html')
@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

@app.route('/on')
def ledOn():
    print("TURNING LED ON")
    yl.ypsCol(yl.WHITE)
    #return 'Yummy cakes!'
    return render_template('on.html')

@app.route('/off')
def ledOff():
    print("TURNING LED OFF")
    yl.ypsCol(yl.OFF)
    #return render_template('off.html')
'''

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
