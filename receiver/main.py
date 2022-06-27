import flask

app = flask.Flask('receiver')

@app.route('/')
def main():
    print('hit')
    return {}, 200

if __name__ == '__main__':
    app.run(port=5001)