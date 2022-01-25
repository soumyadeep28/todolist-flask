from http.client import HTTPResponse
from flask_sqlalchemy import SQLAlchemy
from flask import Flask ,render_template, request ,redirect , url_for

#------------------Define app---------------------
app = Flask(__name__)

#------set environment variable------------

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False 


#------------------ Creating DB -------------------
db =SQLAlchemy(app)


#------------------Creating the Table for that opertaion --------------
class Todo(db.Model):
    id =db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(100) )
    complete = db.Column(db.Boolean)


#------------------Url rendering and function and class calling -----------------
@app.route('/')
def index():
    todolist = Todo.query.all()
    print(todolist)
    return render_template("Base.html" , params= todolist )


@app.route('/add' , methods =['POST' , 'GET'])
def add():
    #add new item
    title = request.form.get('mytext')
    new_todo = Todo(title = title , complete = False )
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<int:todoid>' , methods= ['POST' , 'GET'])
def complete(todoid):
    todo = Todo.query.filter_by(id = todoid).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>' , methods= ['POST' , 'GET'])
def delete(id):
    todo = Todo.query.filter_by(id = id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))












#-----------------run-------------
if __name__ == "__main__":
    db.create_all()
    '''
    new_todo = Todo(title = 'todo1' ,complete = False)
    db.session.add(new_todo)
    db.session.commit() 
    
    '''


    app.run(debug =True)

'''
You can also set params
FLASK_ENV=development
FLASK_APP=main.py
and do flask run commanmd to run the flask app
'''