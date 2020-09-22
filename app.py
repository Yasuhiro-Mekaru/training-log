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



@app.route("/", methods=['GET'])
def hello():
    return render_template('index.html')



# @app.route('/login', methods=['GET'])
# def login():
#     return render_template('login.html')



@app.route('/bicycle_contents', methods=['GET'])
def bicycle_contents():
    return render_template('bicycle_contents.html')



@app.route('/get_diff_data', methods=['POST'])
def get_diff_data():
    # クライアントから送られてきたデータを受け取り、jsonからロードする処理
    posted_data = request.get_data()
    loaded_data = json.loads(posted_data)

    # date.pyのMy_dateクラスのインスタンスを作成し、今日の日付を取得する処理
    date_instance = date.My_date()
    today = date_instance.today_date()
    # 今日の日付から今月1日を取得する処理
    firstday = date_instance.get_first_day()
    # target_distanceテーブルから全行のデータを取得する処理
    database = db.My_log_database(loaded_data)
    response = database.select_data()

    listed_data = []
    for data in response:
        if data[1] == firstday:
            listed_data = list(data)

    target_id = listed_data[0]
    target_distance = listed_data[2]
    datas = {
        'table': 'milage_log',
        'target_id': target_id,
        'target_distance': target_distance
    }

    logger.info({
        'action': 'get_diff_data',
        'datas': datas
        })

    # Milage_log テーブルに9月のデータが入っていないため、下記はコメントアウトする

    milage_database = db.My_log_database(datas)
    milage_response = milage_database.select_data()
    # logger.info({
    #     'action': 'select_data',
    #     'response': response,
    #     'response type': type(response)
    #     })
    listed_response = []
    for data in milage_response:
        listed_data = list(data)
        listed_response.append(listed_data)

    logger.info({
        'action': 'get_diff_data',
        'listed_response': listed_response,
        'listed_response type': type(listed_response)
        })

    #ここにdate関係を書く
    milage_date_instance = date.My_date(listed_response)
    changed_listed_response = milage_date_instance.change_to_date()

    logger.info({
        'action': 'get_diff_data',
        'changed_listed_response': changed_listed_response,
        'changed_listed_response length': len(changed_listed_response)
        })

    pandas_instance = util.My_pandas_data(changed_listed_response, target_distance)
    df = pandas_instance.create_data_frame()

    logger.info({
        'action': 'get_diff_data',
        'df': df
        })

    result = pandas_instance.get_sum_diff()
    logger.info({
        'action': 'get_diff_data',
        'result': result
        })

    return jsonify(result)



@app.route('/get_data', methods=['POST'])
def get_data():
    # クライアントから送られてきたデータを受け取り、jsonからロードする処理
    posted_data = request.get_data()
    loaded_data = json.loads(posted_data)

    # date.pyのMy_dateクラスのインスタンスを作成し、今日の日付を取得する処理
    date_instance = date.My_date()
    today = date_instance.today_date()
    # 今日の日付から今月1日を取得する処理
    firstday = date_instance.get_first_day()

    # target_distanceテーブルから全行のデータを取得する処理
    database = db.My_log_database(loaded_data)
    response = database.select_data()
    #tuple型で返却された値をlist型に変換する処理
    listed_response = []
    for data in response:
        listed_data = list(data)
        listed_response.append(listed_data)

    # クライアントから送られてきた button_id の値に応じて処理を分岐
    if loaded_data['button_id'] == 'button_to_input_dialog':
        target_id = 0
        for data in listed_response:
            if data[1] == firstday:
                target_id = data[0]

        data = {
            'today': today,
            'target_id': target_id
            }
        return jsonify(data)

    elif loaded_data['button_id'] == 'button_to_chart_dialog':
        # datas = []
        # for data in listed_response:
        #     data.pop(2)
        #     datas.append(data)
        logger.info({
            'action': 'get_data elif',
            # 'datas': datas
            'listed_response': listed_response
            })
        # return jsonify(datas)
        return jsonify(listed_response)



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

    return jsonify('Success')


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
    chart_type = loaded_data['chart_type']
    width = loaded_data['width']
    height = loaded_data['height']

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

    # util.pyのMy_pandas_dataクラスのインスタンスを作成し、Pandasのdfオブジェクトを作成する
    pandas_instance = util.My_pandas_data(changed_listed_response, target_distance)
    df = pandas_instance.create_data_frame()

    logger.info({
        'action': 'select_data',
        'df': df,
        'df type': type(df)
        })

    # クライアントから送られてきたchart typeに応じて分岐する
    # milage chart の際の処理
    if chart_type == 1:
        bokeh_instance = bokeh_chart.My_bokeh_chart(df, width=width, height=height)
        bokeh_response = bokeh_instance.create_milage_chart()
        script, div = components(bokeh_response)
        response_datas = {
            'script': script,
            'div': div
        }
        response_datas = json.dumps(response_datas)
        return jsonify(response_datas)

    # elevation chart の際の処理
    elif chart_type == 2:
        bokeh_instance = bokeh_chart.My_bokeh_chart(df)
        bokeh_response = bokeh_instance.create_elevation_chart()
        script, div = components(bokeh_response)
        response_datas = {
            'script': script,
            'div': div
        }
        response_datas = json.dumps(response_datas)
        return jsonify(response_datas)



# if __name__ == "__main__":
    # app.debug = True
    # app.run()
    # app.run(host='0.0.0.0',port=5000,debug=True)