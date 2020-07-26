import json

from flask import Flask, jsonify, request

import db

app = Flask(__name__)
app.debug = True


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
      "Content-Type": "application/json",
      "Answer":{"Text": answer}
    }
    return jsonify(result)

# if __name__ == "__main__":
    # app.debug = True
    # app.run()
    # app.run(host='0.0.0.0',port=5000,debug=True)