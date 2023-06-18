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
    flag = False
    unit = request.args.get('unit')
    post = request.args.get('post')
    rate = request.args.get('rate')
    if unit is not None:
        unit = [i.strip() for i in unit.split(',')]
        flag = True
    if post is not None:
        post = [i.strip() for i in post.split(',')]
        flag = True
    if rate is not None:
        rate = [i.strip() for i in rate.split(',')]
        flag = True
    if flag:
        json_ = json.dumps(modify.get_tb_educators_with_filters(unit, post, rate), sort_keys=False, indent=4,
                           separators=(',', ': '), ensure_ascii=False, )
    else:
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
    flag = False
    workload = request.args.get('workload')
    if workload is not None:
        workload = [i.strip() for i in workload.split(',')]
        flag = True
    if flag:
        json_ = json.dumps(modify.get_tb_entry_with_filters(workload), sort_keys=False, indent=4,
                           separators=(',', ': '), ensure_ascii=False, )
    else:
        json_ = json.dumps(modify.get_tb_entrys(), sort_keys=False, indent=4, separators=(',', ': '),
                           ensure_ascii=False, )
    return json_


@app.route("/entry/<int:id>", methods=['GET'])
@cross_origin()
def get_entry(id: int):
    json_ = json.dumps(modify.get_tb_entry(id), sort_keys=False, indent=4, separators=(',', ': '),
                       ensure_ascii=False)
    return json_


if __name__ == '__main__':
    app.run(debug=True)
