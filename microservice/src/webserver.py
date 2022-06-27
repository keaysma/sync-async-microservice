import flask

from kernel.actions import test

app = flask.Flask('microservice')

@app.route('/test')
def test_route():
    test()
    return {}, 200

if __name__ == '__main__':
    app.run()