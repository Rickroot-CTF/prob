from flask import Flask, request
import urllib
import re

app = Flask(__name__)

try: FLAG = open("flag.txt", "r").read()
except: FLAG = "[**FLAG**]"

url_pattern = re.compile(r"^https?://(?!127\.0\.0\.1\b|0\.0\.0\.0\b|localhost\b|.*\.localhost\b|.*\.168\b)[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,}.*$")

@app.route("/", methods=["GET"])
def index(): return "Hello"

@app.route("/req", methods=["GET"])
def req():
  if request.method == "GET":
    url = request.args.get('url')
    if url:
      if url_pattern.match(url): return "Invalid URL"
      try:
        response = urllib.request.urlopen(url)
        data = response.read()      # a `bytes` object
        return data.decode('utf-8')
      except:return "Error. Error"
  else: return "<h1>what you gonna do man?</h1>"

@app.route("/admin", methods=["GET"])
def admin():
  client_ip = request.headers.get('X-Real-IP') or request.remote_addr
  if request.method == "GET":
    if request.remote_addr == "localhost" or client_ip != "127.0.0.1": return "Wow...."
    return FLAG

app.run(host="0.0.0.0", port=10050)
