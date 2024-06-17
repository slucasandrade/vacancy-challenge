from flask import Flask # type: ignore

app = Flask(__name__)

@app.route('/')
def hello_devops():
    return "Hello, DevOps!"

if __name__ == '__main__':
    app.run(debug=True)
