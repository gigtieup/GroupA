from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime


from facts import Facts


fact_api = Blueprint('fact_api', __name__,
                  url_prefix='/api/facts')


# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(fact_api)


class FactsAPI:       
   class _Create(Resource):
       def post(self):
           ''' Read data for json body '''
           body = request.get_json()
          
           ''' Avoid garbage in, error checking '''
           # validate fact
           fact = body.get('fact')
           if fact is None or len(fact) < 2:
               return {'message': f'fact is missing, or is less than 2 characters'}, 210
           # validate uid
           stock = body.get('stock')
           if stock is None or len(stock) < 2:
               return {'message': f'User ID is missing, or is less than 2 characters'}, 210
           # look for knew and dob


           ''' #1: Key code block, setup USER OBJECT '''
           uo = Facts(fact=fact,
                     stock=stock)
          
           ''' Additional garbage error checking '''
          
           ''' #2: Key Code block to add user to database '''
           # create user in database
           fact = uo.create()
           # success returns json of user
           if fact:
               return jsonify(fact.read())
           # failure returns error
           return {'message': f'Processed {fact}, either a format error or User ID is duplicate'}, 210


   class _Read(Resource):
       def get(self):
           facts = Facts.query.all()    # read/extract all users from database
           json_ready = [fact.read() for fact in facts]  # prepare output in json
           return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps


   # building RESTapi endpoint
   api.add_resource(_Create, '/create')
   api.add_resource(_Read, '/')



