from flask import Flask
from flask_restful import Resource, Api
import json
import random

app = Flask(__name__)
api = Api(app)

# Load the json file
with open('quotes.json', encoding='utf-8') as file:
    data = json.load(file)
    quotes = data["quotes"]

class quote(Resource):
    def get(self, quote_id=None, sfw=None):
        # If quote needs to be sfw
        if sfw != None:
            q = quotes[random.randint(0, len(quotes) - 1)]
            while q["sfw"] != "True":
                q = quotes[random.randint(0, len(quotes) - 1)]

            return q

        # If no id is specified retrun a random quote
        if quote_id == None:
            return quotes[random.randint(0, len(quotes) - 1)]

        # Otherwise find the quote with the id
        for q in quotes:
            if q["id"] == quote_id:
                return q

api.add_resource(quote, '/api/quote/', '/api/quote/<int:quote_id>', '/api/quote/<sfw>/')

if __name__ == '__main__':
    app.run(debug=True)