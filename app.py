from flask import Flask, render_template, g, request, session, redirect, url_for
from database import get_db
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()



@app.route('/',methods=['GET','POST'])
def index():
    '''db= get_db()
    if request.method=='POST':
        
        name = request.form['field1']
        email = request.form['field2']
        message = request.form['field3']
        db.execute('insert into msg (name, email, message) values (?, ?, ?)', [name, email,message])
        db.commit()
    msg=db.execute('select name,message from msg')
    users=msg.fetchall()'''
    db= get_db()
    if request.method=='POST':
        
        name = request.form['field1']
        email = request.form['field2']
        message = request.form['field3']
        
        db.execute('insert into msg (name, email, message) values (?, ?, ?)', [name, email,message])
        db.commit()
        

    msg=db.execute('select name,email,message from msg where name!=""')
    
    users=msg.fetchall()   
    users=users[::-1]
    return render_template('index.html',users=users)

if __name__ == '__main__':
    app.run(use_reloader = True, debug = True)
        


