from pymongo import MongoClient
import os

#connect to server
client = MongoClient()

#navigate to data collection in uber db
db = client.uber
collection = db.data

#structure query string
    #curl -H 'Authorization: Token ZzkhvINvcmuPEq-kZpefsO5ijoK02zdsCCkQ2xkC' \n-H 'Accept-Language: en_US' \n-H 'Content-Type: application/json' \n
    #'https://api.uber.com/v1.2/estimates/price?start_latitude=NNNNNNN&start_longitude=NNNNNNNNN&end_latitude=NNNNNNNN&end_longitude=NNNNNNNN'

#collect data output from command line

#insert data into db

#LOOP IN 5 MINUTE INCREMENTS
