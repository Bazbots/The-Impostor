from flask import Flask
from threading import Thread

app = Flask("The Impostor")

@app.route("/")
def home():
  return "When the Impostor is sus"
def run():
  app.run(host="0.0.0.0",port=8080)

def keep_alive():
  server = Thread(target=run)
  server.start()
