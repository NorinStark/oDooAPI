# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, redirect, session, url_for
from pymongo import MongoClient
import requests
import re, math
from flask_csv import send_csv
import csv
import io
import json
from datetime import datetime
import random
from bson.objectid import ObjectId
from flask_api import status
from bson.json_util import dumps
import base64
from twilio.rest import Client
import requests
import bcrypt
import random
from flask_login import LoginManager
from flask_login import login_required
import jwt
import time
# from flask_uploads import UploadSet, configure_uploads,IMAGES
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

import xmlrpc.client
import datetime
import csv

# application = app = Flask(__name__)


class Odoo():
	def __init__(self):

		self.DATA = "bitnami_odoo"
		self.USER = "user@example.com"
		self.PASS = "x1pTCyyawECg"
		self.PORT = "8069"
		self.URL = "http://54.165.199.203"
		self.URL_COMMON = "{}:{}/xmlrpc/2/common".format(self.URL, self.PORT)
		self.URL_OBJECT = "{}:{}/xmlrpc/2/object".format(self.URL, self.PORT)

	def authenticateOdoo(self):
		self.ODOO_COMMON = xmlrpc.client.ServerProxy(self.URL_COMMON)
		self.ODOO_OBJECT = xmlrpc.client.ServerProxy(self.URL_OBJECT)
		self.UID = self.ODOO_COMMON.authenticate(
			self.DATA
			, self.USER
			, self.PASS
			, {})

	def userAdd(self, userRow):
		user_id = self.ODOO_OBJECT.execute_kw(
			self.DATA
			, self.UID
			, self.PASS
			, 'res.partner'
			, 'create'
			, userRow)
		return user_id

	def userCheck(self, userName):
		odoo_filter = [[("name", "=", userName)]]
		partner_id = self.ODOO_OBJECT.execute_kw(
			self.DATA
			, self.UID
			, self.PASS
			, 'res.partner'
			, 'search'
			, odoo_filter)
		return partner_id

	def userRead(self, user_id):
		odoo_filter = [[("id", "=", user_id)]]
		result = self.ODOO_OBJECT.execute_kw(
			self.DATA
			, self.UID
			, self.PASS
			, 'res.partner'
			, 'read'
			, [user_id]
			, {"fields": ["name", "id", "website"]})
		return result

	def userUpdate(self, user_id, odoo_filter):
		update_result = self.ODOO_OBJECT.execute_kw(
			self.DATA
			, self.UID
			, self.PASS
			, 'res.partner'
			, 'write'
			, [user_id, odoo_filter])
		return update_result

	def userDelete(self, partner_id):
		delete_result = self.ODOO_OBJECT.execute_kw(
			self.DATA
			, self.UID
			, self.PASS
			, 'res.partner'
			, 'unlink'
			, [partner_id])
		return delete_result


	def importCSV(self, customer_template):
		template_id = self.ODOO_OBJECT.execute_kw(
			self.DATA
			, self.UID
			, self.PASS
			, 'res.partner'
			, 'create'
			, customer_template)
		return template_id


def main():
	od = Odoo()
	od.authenticateOdoo()
	# print(od.UID)
	# userRow = [{"name": "Norin Lee666"
	# 			   , "phone": "077280578"
	# 			   , "email": "Norinlee.007@gmail.com"}]
	# od.userAdd(userRow)
    #
	# print("Done!")
    #
	# result = od.userCheck("Norin")
	# print(result)

	with open('client_file.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')

	for row in csv_reader:
		for i in row:
			customer_template = {
				'name': row[i+1]
				, 'birthdate': row[i+1]
				, 'phone': row[i+1]
				, 'email': row[i+1]
				, 'website': row[i+1]
			}

	od.importCSV(customer_template)
	print(csv_file.closed)

if __name__ == '__main__':
	main()





################################################# API #################################################

# @app.route("/api/k2/add-user", methods=['POST'])
# def add_users():
# 	data = json.loads(request.data.decode('utf-8'))
# 	data = [data]
#
# 	# data = [{"name": "Eii Chen", "phone": "012345678", "email": "Eiichen.k001@gmail.com"}]
#
# 	if data and request.method == "POST":
# 		try:
# 			od = Odoo()
# 			od.authenticateOdoo()
# 			od.userAdd(data)
#
# 		except Exception as e:
# 			print("error: ", str(e))
# 			return dumps({'error': "There was an error"}), status.HTTP_500_INTERNAL_SERVER_ERROR
#
# 	return dumps(data)
#
# @app.route("/api/k2/add-policy", methods=['POST'])
# def add_policy():
# 	data = [{'policy_holder': "Norin Stark", 'policy_term': "Immediate Payment", 'policy_schemes': "K2 Screen", 'branch_name': "K2 Norodom", 'agent_name': "Djibril", 'duration': "2", 'issu_date': "09/30/2019", 'policy_amount': "5", 'emi': "Yearly"}]
#
# 	if data and request.method == "POST":
# 		try:
# 			od = Odoo()
# 			od.authenticateOdoo()
# 			od.policyAdd(data)
#
# 		except Exception as e:
# 			print("error: ", str(e))
# 			return dumps({'error': "There was an error"}), status.HTTP_500_INTERNAL_SERVER_ERROR
#
# 	return dumps(data)

################################################# API #################################################

