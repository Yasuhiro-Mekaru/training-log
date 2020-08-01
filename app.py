import json
import logging

from flask import Flask, jsonify, request

import db


app = Flask(__name__)
app.debug = True

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



@app.route("/", methods=['GET'])
def hello():
    datebase = db.My_log_database()
    res = datebase.insert_data()
    # return 'Hello World.'
    return 'The response is {}!!'.format(res)



@app.route('/reply', methods=['POST'])
def reply():
    data = json.loads(request.data)
    answer = "Yes, it is %s!\n" % data["keyword"]
    result = {
      "Answer":{"Text": answer}
    }
    return jsonify(result)


# Test
@app.route('/test1', methods=['POST'])
def test1():
    data = request.get_data()
    data = json.loads(data)
    data_type = type(data)
    logger.info({
        'action': 'test1',
        'data_type': data_type
        })
    return data

@app.route('/test2', methods=['POST'])
def test2():
    data = request.data
    data = json.loads(data)
    data_type = type(data)
    return data_type

@app.route('/test3', methods=['POST'])
def test3():
    data = request.get_json()
    value = data['key']
    return jsonify(value)

@app.route('/test4', methods=['POST'])
def test4():
    data = request.json
    value = data['key']
    return jsonify(value)

@app.route('/test5', methods=['POST'])
def test5():
    data = request.value
    return jsonify(data)




#milage dataがPOSTされた際の処理
@app.route('/post_data', methods=['POST'])
def  post_data():
    pass



# if __name__ == "__main__":
    # app.debug = True
    # app.run()
    # app.run(host='0.0.0.0',port=5000,debug=True)