from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route("/user/<user_id>")
def user_id(user_id):
  return render_template("user_id.html", user_id=user_id)

@app.route("/test1/<v1><v2><v3>")
def test1(v1, v2, v3):
  return render_template(
    "test1.html", v1=v1, v2=v2, v3=v3
  )