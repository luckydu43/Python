from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():

    l=[
        {"name":"Dup", "firstname":"Luc"},
        {"name":"Doe", "firstname":"John"},
    ]
    html=""
    for item in l:
        html+=f"<tr><td>{item['firstname']}</td><td>{item['name']}</td></tr>"
    return f"<table>{html}</table>"

