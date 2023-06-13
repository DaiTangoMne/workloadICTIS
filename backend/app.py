import json

from flask import Flask, render_template, url_for, request
import modify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "<p>GET/educators</p>"


@app.route("/educators", methods=["GET"])
def get_educators():
    json_ = json.dumps(modify.get_tb_educators(), sort_keys=False, indent=4, separators=(',', ': '),
                       ensure_ascii=False, )
    return json_


@app.route("/educators/<int:id>", methods=["GET"])
def get_educator(id: int):
    json_ = json.dumps(modify.get_tb_educator(id), sort_keys=False, indent=4, separators=(',', ': '),
                       ensure_ascii=False, )
    return json_


if __name__ == '__main__':
    app.run(debug=True)
