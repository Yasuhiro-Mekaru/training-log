import json

from flask import Flask, jsonify, request

import db

app = Flask(__name__)
app.debug = True


@app.route("/", methods=['GET'])
def hello():
    # datebase = db.My_log_database()
    # res = datebase.insert_data()
    return 'Hello World.'
    # return 'The response is {}!!'.format(res)



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
    r = data["key"]
    return jsonify(r)

@app.route('/test2', methods=['POST'])
def test2():
    data = request.data()
    r = data["key"]
    return jsonify(r)

@app.route('/test3', methods=['POST'])
def test3():
    data = request.get_json()
    r = data["key"]
    return jsonify(r)

@app.route('/test4', methods=['POST'])
def test4():
    data = request.json()
    r = data["key"]
    return jsonify(r)




#milage dataがPOSTされた際の処理
@app.route('/post_data', methods=['POST'])
def  post_data():
    pass



# if __name__ == "__main__":
    # app.debug = True
    # app.run()
    # app.run(host='0.0.0.0',port=5000,debug=True)