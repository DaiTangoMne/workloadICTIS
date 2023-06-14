import json

from flask import Flask, render_template, url_for, request
from flask_cors import CORS, cross_origin
import modify

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/", methods=["GET"])
@cross_origin()
def index():
    return render_template("index.html")


@app.route("/educators", methods=["GET"])
@cross_origin()
def get_educators():
    json_ = json.dumps(modify.get_tb_educators(), sort_keys=False, indent=4, separators=(',', ': '),
                       ensure_ascii=False, )
    return json_


@app.route("/educators/<int:id>", methods=["GET"])
@cross_origin()
def get_educator(id: int):
    json_ = json.dumps(modify.get_tb_educator(id), sort_keys=False, indent=4, separators=(',', ': '),
                       ensure_ascii=False)
    return json_


@app.route("/entry", methods=['GET'])
@cross_origin()
def get_entrys():
    json_ = json.dumps(modify.get_tb_entrys(), sort_keys=False, indent=4, separators=(',', ': '),
                       ensure_ascii=False)
    return json_


@app.route("/entry/<int:id>", methods=['GET'])
@cross_origin()
def get_entry(id: int):
    json_ = json.dumps(modify.get_tb_entry(id), sort_keys=False, indent=4, separators=(',', ': '),
                       ensure_ascii=False)
    return json_


@app.route("/entry/filter", methods=['GET'])
@cross_origin()
def get_entry_filter():
    workload = []
    workload.extend(request.args.get('workload').split(','))
    print(request.args.get('workload'))
    json_ = json.dumps(modify.get_tb_entry_with_filters(workload), sort_keys=False, indent=4, separators=(',', ': '),
                       ensure_ascii=False)
    return json_


if __name__ == '__main__':
    app.run(debug=True)
