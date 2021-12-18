import json
import logging

from flask import Flask
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
import numpy as np
import pandas as pd
import bokeh
from bokeh.embed import components 

import bokeh_chart
import date
import db
import util
import controller


app = Flask(__name__)
app.secret_key = 'test_secret_key'
app.config['JSON_AS_ASCII'] = False
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



@app.route('/', methods=['GET'])
def index():
    logger.info({
        'action': 'app.py index',
        'message': 'index is called'
        })
    # sessionがあるか確認
    if session:
        #sessionがあればmain_menuメソッドへリダイレクト
        return redirect(url_for('main_menu'))
    else:
        return render_template('index.html') 


@app.route('/main_menu', methods=['GET'])
def main_menu():
    logger.info({
        'action': 'app.py main_menu',
        'message': 'main_menu is called'
        })
    # sessionがあるか確認
    if session:
        return render_template('main_menu.html')
    else:
        # sessionがなければindexメソッドへリダイレクト
        return redirect(url_for('index'))


@app.route('/user_registration', methods=['GET', 'POST'])
def user_registration():
    logger.info({
        'action': 'app.py user_registration',
        'message': 'user_registration is called',
        'request.method': request.method
        })
    # sessionがあるか確認
    if session:
        #sessionがあればmain_menuメソッドへリダイレクト
        return redirect(url_for('main_menu'))
    else:
        if request.method == 'GET':
            # GETリクエストの際の処理
            return render_template('user_registration.html')
        else:
            # POSTリクエストの際の処理。User情報をDBに登録する
            # クライアントから送られたデータを変数に格納
            user_datas = request.form
            logger.info({
                'action': 'app.py user_registration',
                'user_datas': user_datas,
                'user_datas type': type(user_datas)
            })

            # Usersテーブルにinsertする処理。返り値はboolian型
            response = controller.insert_user(datas=user_datas)
            logger.info({
                'response': response,
                'response type': type(response)
            })

            if response:
                return redirect(url_for('login'))

            return 'Fail to registration'


@app.route('/login', methods=['GET', 'POST'])
def login():
    logger.info({
        'action': 'app.py login()',
        'message': 'login is called'
        })
    # sessionがあるか確認
    if session:
        #sessionがあればmain_menuメソッドへリダイレクト
        return redirect(url_for('main_menu'))
    else:
        if request.method == 'GET':
            # GETリクエストの際の処理
            return render_template('login.html')
        else:
            # Todo User情報をDBに問い合わせる処理
            # クライアントから送られたデータを変数に格納
            login_datas = request.form
            logger.info({
                'action': 'app.py login',
                'login_datas': login_datas,
                'login_datas type': type(login_datas)
                })

            user_datas = controller.get_user(login_datas=login_datas)
            logger.info({
                'action': 'app.py login',
                'user_datas': user_datas,
                'user_datas type': type(user_datas)
                })

            if user_datas:
                session['user_id'] = user_datas[0]['user_id']
                session['user_name'] = user_datas[0]['user_name']
                return redirect(url_for('main_menu'))

            return 'Login Failed'


@app.route('/budget_main', methods=['GET', 'POST'])
def budget_main():
    logger.info({
        'action': 'app.py budget_main()',
        'message': 'budget_main is called'
        })
    # sessionがあるか確認
    if session:
        if request.method == 'GET':   
            # Todo DBから当月の予算の進捗のデータを取得しhtmlに付加する処理
            return render_template('budget_main.html')
        else:
            recieve_data = request.json
            logger.info({
                'action': 'app.py budget_main()',
                'recieve_data': recieve_data,
                'recieve_data type': type(recieve_data)
                })
            return 'success'
    else:
        # sessionがなければlogin.htmlへ遷移
        return redirect(url_for('login'))


@app.route('/select_items', methods=['GET'])
def select_items():
    logger.info({
        'action': 'app.py select_items()',
        'message': 'select_items is called'
        })
    if session:
        table_datas = controller.select_item()
        return jsonify(table_datas)
    else:
        return False





@app.route('/bicycle_contents', methods=['GET'])
def bicycle_contents():
    logger.info({
        'action': 'app.py bicycle_contents',
        'message': 'bicycle_contents is called'
        })
    return render_template('bicycle_contents.html')



@app.route('/get_diff_data', methods=['POST'])
def get_diff_data():
    # クライアントから送られてきたデータを受け取り、jsonからロードする処理
    posted_data = request.get_data()
    loaded_data = json.loads(posted_data)

    # date.pyのMy_dateクラスのインスタンスを作成し、今日の日付を取得する処理
    date_instance = date.My_date()
    today = date_instance.today_date()
    logger.info({
        'action': 'get_diff_data',
        'today': today
        })
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
    milage_database = db.My_log_database(datas)
    milage_response = milage_database.select_data()

    listed_response = []
    for data in milage_response:
        listed_data = list(data)
        listed_response.append(listed_data)

    #ここにdate関係を書く
    milage_date_instance = date.My_date(listed_response)
    changed_listed_response = milage_date_instance.change_to_date()

    #util.py のクラスのインスタンスを生成し、Pandas DataFrameオブジェクトを受け取る処理
    pandas_instance = util.My_pandas_data(datas=changed_listed_response, target_distance=target_distance)
    df = pandas_instance.df

    # 今月の合計走行距離の一番最新の値を取得
    sum_milage = df.iloc[-1]['Sum_milage']
    sum_milage = round(sum_milage, 2)   
    logger.info({
        'action': 'get_diff_data',
        'sum_milage': sum_milage,
        'sum_milage type': type(sum_milage)
        })

    sum_diff_result = pandas_instance.get_sum_diff()
    daily_diff_result = pandas_instance.get_daily_diff(today)
    datas = {
        'sum_diff_result': sum_diff_result,
        'daily_diff_result': daily_diff_result,
        'sum_milage': sum_milage
    }

    return jsonify(datas)



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
    df = pandas_instance.df

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


# ### 2021/04/10 Finance Account の追加 ###
# @app.route('/finance_account', methods=['GET'])
# def finance_account():
#     table = 'account_category'
#     category_datas = controller.select_from_table(table)
#     table = 'account_entries'
#     entries_datas = controller.select_from_table(table)
#     db_datas = {
#         'category_datas': category_datas, 
#         'entries_datas': entries_datas
#         }
#     return render_template('finance_data_input.html', db_datas=db_datas)



# if __name__ == "__main__":
    # app.debug = True
    # app.run()
    # app.run(host='0.0.0.0',port=5000,debug=True)