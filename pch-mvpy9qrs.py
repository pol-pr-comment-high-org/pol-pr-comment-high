from flask import Flask, request
from markupsafe import Markup
app = Flask(__name__)
@app.route("/greet")
def greet():
    return Markup(request.args.get("name", ""))
app.run(host="0.0.0.0")
