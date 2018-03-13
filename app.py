# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_restful import Resource, Api
from firebase import firebase
from difflib import SequenceMatcher
from json import dumps
from flask.ext.jsonpify import jsonify


app = Flask(__name__)
api = Api(app)

class Menu(Resource):
	def similar(self,a, b):
		return SequenceMatcher(None, a, b).ratio()

	def get(self, menu_image):
		# firebases = firebase.FirebaseApplication('https://test-82b73.firebaseio.com/')
		# result = firebases.get('/menues', None)

		# keys = result.keys()
		var menu = ['ข้าวมันไก่','ผัดกระเพราหมู','ข้าวผัดไก่']
		max_ratio = 0

		a = menu_image
		# print(type(a))
		data = {}
		for key in keys:
			result2 = firebases.get('/menues', menu)
			word = result2["nameThai"]
			ratio = self.similar(a, word)
			# print(word)
			# print(ratio)
			if ratio == 1:
				aaa = word
				data = result2
				break
			elif ratio > max_ratio:
				aaa = word
				data = result2
			max_ratio = max(ratio, max_ratio)
		result3 = {'data': data}
		return result3	

api.add_resource(Menu, '/menu/<menu_image>')

if __name__ == '__main__':
     app.run(host="0.0.0.0", debug=True)
	
