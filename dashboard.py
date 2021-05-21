from flask import Flask, render_template

app = Flask(__name__)


@app.route("/dashboard")
def home():
  return "Redirecting..."

if __name__ = __main__:
  app.run()
