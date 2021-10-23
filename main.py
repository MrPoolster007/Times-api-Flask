from flask import Flask, jsonify
import base

app =  Flask(__name__)
res = base.finale_result

@app.route('/')
def hello():
    res = {
        'id':1,
        'name':'Tekmonks',
        'place':'banglore'
    }
    return jsonify(res)

@app.route('/getTimeStories')
def get_time_stories():
    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True)