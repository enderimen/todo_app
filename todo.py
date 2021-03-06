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

@app.route("/complete/<string:id>")   # Url' den gelen veriye göre listeleme yapıyoruz 
def completeTodo(id): #görevi tamamla
 
    todo = Todo.query.filter_by(id=id).first()
 
    if (todo.complete == False):
       todo.complete = True
    else:
        todo.complete = False

    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")   # Url' den gelen verinin id sine göre silme işlemi yapıyoruz 
def deleteTodo(id): # Silme işlemini gerçekleştir
    
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/detail/<string:id>")   # Url' den gelen verinin id sine göre detay sayfasına yönlendireceğiz 
def detailTodo(id): # Detay sayfası
    todo = Todo.query.filter_by(id=id).first()
    return render_template("detail.html",todo = todo)

class Todo(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    complete = db.Column(db.Boolean)

if __name__ == "__main__":
    app.run(debug = True)
