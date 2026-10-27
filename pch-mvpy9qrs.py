from flask import Flask
import requests
app = Flask(__name__)
app.run(host="0.0.0.0")
requests.get("https://example.com", verify=False)
