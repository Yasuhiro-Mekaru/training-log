import json
import logging

from flask import Flask, jsonify, render_template, request, redirect
import numpy as np
import pandas as pd
import bokeh
from bokeh.embed import components 

import bokeh_chart
import date
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

TARGET_DISTANCE = []


@app.route("/", methods=['GET'])
def hello():
    data = {'table': 'target_distance'}
    database = db.My_log_database(data)
    response = database.select_data()
    logger.info({
        'action': 'root',
        'response': response,
        'response type': type(response)
        })
    for datas in response:
        listed_data = list(datas)
        TARGET_DISTANCE.append(listed_data)

    logger.info({
        'action': 'root',
        'TARGET_DISTANCE ': TARGET_DISTANCE 
        })
    date_instance = date.My_date()
    today = date_instance.today_date()
    logger.info({
        'action': 'root',
        'today': today,
        'today type': type(today)
        })

    return render_template('index.html', datas=TARGET_DISTANCE)


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')



@app.route('/bicycle_contents', methods=['GET'])
def bicycle_contents():
    return render_template('bicycle_contents.html')



@app.route('/reply', methods=['POST'])
def reply():
    data = json.loads(request.data)
    answer = "Yes, it is %s!\n" % data["keyword"]
    result = {
      "Answer":{"Text": answer}
    }
    return jsonify(result)



# DBのテーブルにPOSTする際の処理
@app.route('/insert_data', methods=['POST'])
def  insert_data():
    posted_data = request.get_data()
    loaded_data = json.loads(posted_data)

    logger.info({
        'action': 'insert_data',
        'loaded_data': loaded_data
        })

    database = db.My_log_database(loaded_data)
    database.insert_data()

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

    database = db.My_log_database(loaded_data)
    database.delete_data()

    return 'Deleted'


# DBのテーブルからデータをGETする際の処理
@app.route('/select_data', methods=['POST'])
def select_data():
    posted_data = request.get_data()
    loaded_data = json.loads(posted_data)

    target_distance = loaded_data['target_distance']

    logger.info({
        'action': 'select_data',
        'loaded_data': loaded_data,
        'target_distance': target_distance
        })

    database = db.My_log_database(loaded_data)
    response = database.select_data()
    # logger.info({
    #     'action': 'select_data',
    #     'response': response,
    #     'response type': type(response)
    #     })
    listed_response = []
    for data in response:
        listed_data = list(data)
        listed_response.append(listed_data)

    logger.info({
        'action': 'select_data',
        'listed_response': listed_response,
        'listed_response type': type(listed_response)
        })

    #ここにdate関係を書く
    date_instance = date.My_date(listed_response)
    changed_listed_response = date_instance.change_to_date()

    logger.info({
        'action': 'select_data',
        'changed_listed_response': changed_listed_response,
        'changed_listed_response length': len(changed_listed_response)
        })

    # date_instance.set_datas()

    pandas_instance = util.My_pandas_data(changed_listed_response, target_distance)
    df = pandas_instance.create_data_frame()

    logger.info({
        'action': 'select_data',
        'df': df,
        'df type': type(df)
        })

    bokeh_instance = bokeh_chart.My_bokeh_chart(df)
    bokeh_response = bokeh_instance.create_chart()

    script, div = components(bokeh_response)

    logger.info({
        'action': 'select_data',
        'script type': type(script),
        })

    response_datas = {
        'script': script,
        'div': div
    }

    # logger.info({
    #     'action': 'select_data',
    #     'response_datas type': type(response_datas),
    #     })

    response_datas = json.dumps(response_datas)

    # logger.info({
    #     'action': 'select_data',
    #     'response_datas changed type': type(response_datas),
    #     })


    return jsonify(response_datas)


# if __name__ == "__main__":
    # app.debug = True
    # app.run()
    # app.run(host='0.0.0.0',port=5000,debug=True)