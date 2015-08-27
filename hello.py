##from flask import Flask
##app = Flask(__name__)
##
##@app.route("/")
##def hello():
##    return "Hello from Sierra's server!"
##
##def ftoc(ftemp):
##   return (ftemp-32.0)*(5.0/9.0)
##
##@app.route('/ftoc/<ftempString>')
##def convertFtoC(ftempString):
##    ftemp = 0.0
##    try:
##        ftemp = float(ftempString)
##        ctemp = ftoc(ftemp)
##        return "In Fahrenheit: " + ftempString + " In Celsius: " + str(ctemp) 
##    except ValueError:
##        return "Sorry.  Could not convert " + ftempString + " to a number "
##
##def milesToKm(miles):
##    return (miles/0.62137)
##
##@app.route('/mtokm/<milesString>')
##def convertMilesToKm(milesString):
##    miles = 0.0
##    try:
##        miles = float(milesString)
##        Km = milesToKm(miles)
##        return "In miles: " + milesString + " In kilometers: " + str(Km)
##    except ValueError:
##        return "Sorry. Could not convert " + milesString + " to a number "
##    
##if __name__ == "__main__":
##    app.run(port=5000)

import os
from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def helloRoot():
    return "Try <a href='" + url_for('tempConvert') + "'>Temperature Conversion</a>"

def ftoc(ftemp):
    return (ftemp - 32 ) * (5.0/9.0)

@app.route('/tempConvert')
def tempConvert():
    return render_template('tempConvert.html')

@app.route('/doTempConvert')
def doTempConvert():

    try:
        ftempstring = request.args['ftemp']
        ftemp=float(ftempstring)
        ctemp=ftoc(ftemp)
        return render_template('tempconvertresults.html',
                               showFtemp=ftemp,
                               showCtemp=ctemp)
    except ValueError:
        return render_template('tempcouldnotconvert.html',
                               showFtemp = ftempstring)
    
if __name__=="__main__":
    app.run(debug=False)
    app.run(port=5000)
