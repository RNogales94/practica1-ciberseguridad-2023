from flask import Flask
from query import get_company_information
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/yahoo')
def get_company():
    symbol = "DIS"
    return get_company_information(symbol)


if __name__ == '__main__':
    app.run()



