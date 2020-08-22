import json
import logging

from flask import Flask, jsonify, render_template, request
import numpy as np
import pandas as pd
import bokeh

import db
import util


app = Flask(__name__)
app.debug = True

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logging.info({
    'action': 'numpy',
    'version': np.__version__
    })

logging.info({
    'action': 'pandas',
    'version': pd.__version__
    })

logging.info({
    'action': 'bokeh',
    'version': bokeh.__version__
    })



@app.route("/", methods=['GET'])
def hello():
    return render_template('index.html')




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





# DBのテーブルにPOSTする際の処理
@app.route('/insert_data', methods=['POST'])
def  insert_data():
    posted_data = request.get_data()
    loaded_data = json.loads(posted_data)

    logger.info({
        'action': 'insert_data',
        'loaded_data': loaded_data
        })

    datebase = db.My_log_database(loaded_data)
    datebase.insert_data()

    return 'Success', 201


# DBのテーブルのデータをDELETEする際の処理
@app.route('/delete_data', methods=['DELETE'])
def delete_data():
    posted_data = request.get_data()
    loaded_data = json.loads(posted_data)

    logger.info({
        'action': 'delete_data',
        'loaded_data': loaded_data
        })

    datebase = db.My_log_database(loaded_data)
    datebase.delete_data()

    return 'Deleted'


# DBのテーブルからデータをGETする際の処理
@app.route('/select_data', methods=['POST'])
def select_data():
    posted_data = request.get_data()
    loaded_data = json.loads(posted_data)

    logger.info({
        'action': 'select_data',
        'loaded_data': loaded_data
        })

    datebase = db.My_log_database(loaded_data)
    response = datebase.select_data()
    logger.info({
        'action': 'select_data',
        #'response': response,
        'response type': type(response)
        })
    change_type_response = tuple(response)
    logger.info({
        'action': 'select_data',
        'change_type_response': change_type_response,
        'change_type_response type': type(change_type_response)
        })

    return change_type_response


# if __name__ == "__main__":
    # app.debug = True
    # app.run()
    # app.run(host='0.0.0.0',port=5000,debug=True)