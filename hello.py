from flask import Flask

hello = Flask(__name__)

@hello.route('/')
def hello_world():
    return 'Hello, from a web server in Cloud Shell!'

if __name__ == '__main__':
    hello.run(host='0.0.0.0', port=8080)