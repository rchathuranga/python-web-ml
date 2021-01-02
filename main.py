from flask import Flask

app = Flask(__name__)


@app.route("/")
def end_point():
    return "Hello World 2"


if __name__ == '__main__':
    app.run(port=8081)
