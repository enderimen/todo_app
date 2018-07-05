from flask import Flask ,render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Acer E1 571G/Desktop/todo_app/todo.db'
db = SQLAlchemy(app)

@app.route("/") # Default yönlendirme
def index():
    todos = Todo.query.all() # Tüm kayıtları çekiyoruz
    return render_template("index.html",todos = todos)

@app.route("/add",methods = ["POST"])   # Yapılacak submit işleminin POST old. belirtiyoruz
def addTodo():
    title   = request.form.get("title")     
    content = request.form.get("content")
    
    newTodo = Todo(title = title,content = content, complete = False) 

    db.session.add(newTodo) # tabloya gönderiyoruz
    db.session.commit() # tabloya ekleme işlemini gerçekleştirdik
    return redirect(url_for("index")) # Tekrar anasayfaya dönüyoruz

class Todo(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    complete = db.Column(db.Boolean)

if __name__ == "__main__":
    app.run(debug = True)
