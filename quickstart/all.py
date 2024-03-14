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

@app.route("/t/<user_id>")
def t(user_id):
  return f"<h1>Your User ID is {0} {1} {2}</h1>".format(user_id[0], user_id[1], user_id[2])
  


@app.route("/test1/<v1><v2><v3>")
def test1(v1, v2, v3):
  return render_template(
    "test1.html", v1=v1, v2=v2, v3=v3
  )

if __name__ == "__main__":
  app.run(debug=True)



