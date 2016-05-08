
#!usr/bin/python
from flask import Flask, render_template


#creates the instance of the flask object
app=Flask(__name__)

@app.route('/')
#def home():
   # return "Hello World!"

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

#initializes the localhost and allows for debugging
if __name__=='__main__':
    app.run(debug=True)
