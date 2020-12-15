import pymongo
from time import time
import datetime
import numpy

class MongoDbManager:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://muze_root:this-is-root-passwd@3.13.31.198:27017/")
        self.collection = self.client['muzeDB']['logCollection']

    def searchDB(self, query):
        return self.collection.find(query).sort("time")          

def filterByDate(manager, date):
    time_query = {"time": {'$gte':time()-86400*date}}
    data = manager.searchDB(time_query)
    return data

def sortByColumn(data):
    sorted_data = {}
    sorted_data['time'] = []
    sorted_data['url'] = []
    sorted_data['status_code'] = []
    sorted_data['request_time'] = []

    # print(f"{'time':20}|{'url':60}|{'status_code':5}|{'request_time':20}")
    for d in data:
        time = d['time']
        url = d['url']
        status_code = d['status_code']
        try:
            request_time = d['response_time']
        except:
            request_time = d['request_time']
        
        sorted_data['time'].append(convert_datetime(time))
        sorted_data['url'].append(url)
        sorted_data['status_code'].append(status_code)
        sorted_data['request_time'].append(request_time)

    return sorted_data

def convert_datetime(unixtime):
    date = datetime.datetime.fromtimestamp(unixtime).strftime('%Y-%m-%dT%H:%M:%S.%f')
    return date[:-3] # format : str


# dbManager = MongoDbManager()

# printed_data = filterByDate(dbManager, 7)
# data = sortByColumn(printed_data)
# print(data)
