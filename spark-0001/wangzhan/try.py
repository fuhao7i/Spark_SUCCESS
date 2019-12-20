'''
from flask import Flask
from flask import render_template

app = Flask(__name__,template_folder='./',static_folder="",static_url_path="")

@app.route("/")
def main():
  return render_template("tw.html")

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=5000)
'''
from flask import Flask, redirect
from flask import render_template
from flask import request, url_for

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():

    return render_template('index.html', htmlList=[])  \


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
