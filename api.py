from flask import Flask, request, Response
from query import get_company_information
from query_wallapop import get_wallapop
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/yahoo')
def get_company():
    symbol = request.args.get('ticker')
    if symbol is None:
        return Response(json.dumps({"error": "missing 'ticker' query-parameter"}), status=400, mimetype='application/json')
    return Response(json.dumps(get_company_information(symbol)), status=200, mimetype='application/json')


@app.route('/api/wallapop')
def get_product_and_price_average():
    query = request.args.get('search_text')
    if query is None:
        return Response(json.dumps({"error": "missing 'search_text' query-parameter"}), status=400, mimetype='application/json')

    return Response(json.dumps(get_wallapop(query)), status=200, mimetype='application/json')



if __name__ == '__main__':
    app.run()



