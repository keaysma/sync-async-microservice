import flask

from client.worker import TestTask

app = flask.Flask('main')

@app.route('/sync')
def sync_route():
    TestTask.run_sync()
    return {}, 200

@app.route('/async')
def async_route():
    TestTask.run_async()
    return {}, 200

if __name__ == '__main__':
    app.run(port=3210)