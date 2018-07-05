from flask import Flask ,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Acer E1 571G/Desktop/todo_app/todo.db'
db = SQLAlchemy(app)

@app.route("/")
def index():
   return render_template("index.html")

class Todo(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    complete = db.Column(db.Boolean)

if __name__ == "__main__":
    app.run(debug = True)
