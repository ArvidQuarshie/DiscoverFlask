
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

@app.route('/login',methods=['GET','POST'])
def login():
    error=None
    return render_template('login.html',error=error)
    if request.method=='POST':
        if request.form['username']!='admin' or request.form['password'!='admin':
                                                              error="invalid credentials.Please try again"
                                                             else:
                                                             return redirect(url_for('home'))
                                                             
         return render_template('login.html',error=error)  
                                                             
#initializes the localhost and allows for debugging
if __name__=='__main__':
    app.run(debug=True)
