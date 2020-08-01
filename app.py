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
    posted_data = request.get_data()
    logger.info({
        'action': 'test1',
        'posted_data': posted_data
        })
    posted_data_type = type(posted_data)
    logger.info({
        'action': 'test1',
        'posted_data_type': posted_data_type
        })
    loaded_data = json.loads(posted_data)
    logger.info({
        'action': 'test1',
        'loaded_data': loaded_data
        })
    loaded_data_type = type(loaded_data)
    logger.info({
        'action': 'test1',
        'loaded_data_type': loaded_data_type
        })
    return 'Success'


@app.route('/test2', methods=['POST'])
def test2():
    posted_data = request.data
    logger.info({
        'action': 'test2',
        'posted_data': posted_data
        })
    posted_data_type = type(posted_data)
    logger.info({
        'action': 'test2',
        'posted_data_type': posted_data_type
        })
    loaded_data = json.loads(posted_data)
    logger.info({
        'action': 'test2',
        'loaded_data': loaded_data
        })
    loaded_data_type = type(loaded_data)
    logger.info({
        'action': 'test2',
        'loaded_data_type': loaded_data_type
        })
    return 'Success'



@app.route('/test3', methods=['POST'])
def test3():
    posted_data = request.get_json()
    logger.info({
        'action': 'test3',
        'posted_data': posted_data
        })
    posted_data_type = type(posted_data)
    logger.info({
        'action': 'test3',
        'posted_data_type': posted_data_type
        })
    loaded_data = json.loads(posted_data)
    logger.info({
        'action': 'test3',
        'loaded_data': loaded_data
        })
    loaded_data_type = type(loaded_data)
    logger.info({
        'action': 'test3',
        'loaded_data_type': loaded_data_type
        })
    return 'Success'



@app.route('/test4', methods=['POST'])
def test4():
    posted_data = request.json
    logger.info({
        'action': 'test4',
        'posted_data': posted_data
        })
    posted_data_type = type(posted_data)
    logger.info({
        'action': 'test4',
        'posted_data_type': posted_data_type
        })
    loaded_data = json.loads(posted_data)
    logger.info({
        'action': 'test4',
        'loaded_data': loaded_data
        })
    loaded_data_type = type(loaded_data)
    logger.info({
        'action': 'test4',
        'loaded_data_type': loaded_data_type
        })
    return 'Success'



@app.route('/test5', methods=['POST'])
def test5():
    posted_data = request.value
    logger.info({
        'action': 'test5',
        'posted_data': posted_data
        })
    posted_data_type = type(posted_data)
    logger.info({
        'action': 'test5',
        'posted_data_type': posted_data_type
        })
    loaded_data = json.loads(posted_data)
    logger.info({
        'action': 'test5',
        'loaded_data': loaded_data
        })
    loaded_data_type = type(loaded_data)
    logger.info({
        'action': 'test5',
        'loaded_data_type': loaded_data_type
        })
    return 'Success'




#milage dataがPOSTされた際の処理
@app.route('/post_data', methods=['POST'])
def  post_data():
    pass



# if __name__ == "__main__":
    # app.debug = True
    # app.run()
    # app.run(host='0.0.0.0',port=5000,debug=True)