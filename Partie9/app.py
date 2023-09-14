from flask import Flask, redirect, render_template
from TodoDAO import TodoDAO

app = Flask(__name__)

@app.route("/")
def index():

    dao = TodoDAO("todos_db.db")

    listeChargeeDAO = dao.findAll()
    
    return render_template('todo_list.html', todos=listeChargeeDAO)

@app.route("/delete/<id>")
def delete(id):
    dao = TodoDAO("todos_db.db")
    dao.delete(id)
    return redirect('/')

@app.route("/sale")
def sale():
    dao = TodoDAO("todos_db.db")

    listeManuelle=[
        {"name":"Dup", "firstname":"Luc"},
        {"name":"Doe", "firstname":"John"},
    ]
    listeChargeedeDAO = dao.findAll()
    
    html=""

    for item in listeManuelle:
        html+=f"<tr><td>{item['firstname']}</td><td>{item['name']}</td></tr>"

    for todo in listeChargeedeDAO:
        html+=f"<tr><td>{todo.title}</td><td>{todo.completed}</td></tr>"

    return f"<table>{html}</table>"