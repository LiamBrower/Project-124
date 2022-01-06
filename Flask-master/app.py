from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Excercise',
        'description': u'Sunday, Monday, Tuesday, Wednesday, Thursday, Friday',
        'done': False
    },
    {
        'id': 2,
        'title': u'Read',
        'description': u'Find a good book at the library',
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Data Found!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Requesting sufficient data."
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
    }

    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    })

if (__name__ == "__main__"):
    app.run(debug=True)