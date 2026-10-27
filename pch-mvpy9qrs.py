from flask import Flask, request
app = Flask(__name__)
@app.route("/greet")
def greet():
    return request.args.get("name", "")
app.run(host="0.0.0.0")
