from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   num1 = db.Column(db.String(100))
   num2 = db.Column(db.String(50))
   total = db.Column(db.String(200)) 
   

   def __init__(self, num1, num2, total):
      self.num1 = num1
      self.num2 = num2
      self.total = total

@app.route('/')
def show_all():
   return render_template('show_all.html', students = students.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['num1'] or not request.form['num2'] :
         flash('Please enter all the fields', 'error')
      else:
         res=int(request.form['num1'])+int(request.form['num2'])
         print(int(request.form['num1'])+int(request.form['num2']))
         # res=int(request.form['num1'])+int(request.form['num2'])
         # print(request.form['num1'], request.form['num2'], request.form['total'])
         # student = students(num1=request.form['num1'], num2=request.form['num2'], total=res)
         student = students(num1=request.form['num1'], num2=request.form['num2'] ,total=res)
         
         db.session.add(student)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')


def hello ():
   print("hello abdullah")

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True,host='0.0.0.0')