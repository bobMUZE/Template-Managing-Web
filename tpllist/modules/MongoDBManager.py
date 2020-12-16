import pymongo
from time import time
import datetime
import numpy as np 

class MongoDbManager:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://muze_root:this-is-root-passwd@3.13.31.198:27017/")
        self.collection = self.client['muzeDB']['logCollection']

    def searchDB(self, query):
        return self.collection.find(query).sort("time", -1)          

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


def getStatusCodeData(period) :
    dbManager = MongoDbManager()
    data = filterByDate(dbManager, period)
    
    statusCodeData = {}
    statusCodeData['time'] = []
    statusCodeData['200'] = [ 0 for _ in range(0, data.count())]
    statusCodeData['300'] = [ 0 for _ in range(0, data.count())]
    statusCodeData['400'] = [ 0 for _ in range(0, data.count())]
    statusCodeData['500'] = [ 0 for _ in range(0, data.count())]

    for idx, d in enumerate(data):
        time = convert_datetime(d['time'])
        time = [time.split('T')]
        status_code = d['status_code']
        statusCodeData['time'].append(time)
        statusCodeData[str(status_code)][idx] += 1
    
    return statusCodeData

def getPerformanceData(period):
    dbManager = MongoDbManager()
    data = filterByDate(dbManager, period)
    
    performance_data = []

    for d in data:
        row = []
        time = convert_datetime(d['time'])
        url = d['url']
        status_code = d['status_code']
        module = d['module']
        detection = d['detection']
        try:
            request_time = d['response_time']
        except:
            request_time = d['request_time']
        
        row.append(time)
        row.append(url)
        row.append(status_code)
        row.append(request_time)
        row.append(module)
        row.append(detection)

        performance_data.append(row)    
    dbManager.client.close()

    return performance_data

def getMonitoringData(period):
    dbManager = MongoDbManager()
    data = filterByDate(dbManager, period)
    
    monitoring_data = []

    for d in data:
        row = []
        time = convert_datetime(d['time'])
        url = d['url']
        module = d['module']
        detection = d['detection']

        row.append(time)
        row.append(url)
        row.append(module)
        row.append(detection)

        monitoring_data.append(row)    
    dbManager.client.close()

    return monitoring_data

def getLoadData(period):
    dbManager = MongoDbManager()
    data = filterByDate(dbManager, period)
    
    load_data = {}
    load_data['time'] = []
    load_data['request_time'] = []

    for d in data:
        time = convert_datetime(d['time'])
        try:
            request_time = d['response_time']
        except:
            request_time = d['request_time']

        load_data['time'].append(time)
        load_data['request_time'].append(request_time)

    dbManager.client.close()

    return load_data

def getApdexData(period):
    dbManager = MongoDbManager()
    data = filterByDate(dbManager, int(period))
    
    apdex_data = {}
    apdex_data['status_code'] = [0, 0]
    apdex_data['url'] = []

    total_cnt = data.count()

    for d in data:
        status_code = d['status_code']
        if status_code == 200 or status_code == 300:
            apdex_data['status_code'][0] += 1

        elif status_code == 400 or status_code == 500:
            apdex_data['status_code'][1] += 1
            apdex_data['url'].append(d["url"])
    
    apdex_data['apdex'] = f"{(apdex_data['status_code'][0] + apdex_data['status_code'][1]*0.5) / total_cnt:.3f}"
    apdex_data['200'] = f"{apdex_data['status_code'][0]/total_cnt:.3f}"
    apdex_data['400'] = f"{apdex_data['status_code'][1]/total_cnt:.3f}"


    dbManager.client.close()

    return apdex_data

def getModuleData(period):
    dbManager = MongoDbManager()
    data = filterByDate(dbManager, int(period))
    
    module_data = {}
    module_data['xss'] = [0, 0, 0]
    module_data['code'] = [0, 0, 0]  # HTML 위변조 탐지
    module_data['url_safe'] = [0, 0, 0]  # URL 안정성 검사
    module_data['jquery'] = [0, 0, 0]  # 제이쿼리 위변조
    module_data['iframe'] = [0, 0, 0]  # Iframe 도메인 탐지 
    module_data['phishing'] = [0, 0, 0]  # phishing 

    for d in data:
        detection = d['detection']
        module = d['module']
        if detection:
            logdata = d['logdata']
            for log in logdata:
                try:
                    submodule = log['submodule']
                    # HTML XSS_Detection_Server ML_PhishingDetected
                    if module == 'ML_PhishingDetected' and submodule == 0:
                        module_data['phishing'][2] += 1
                    elif module == "XSS_Detection_Server":
                        module_data['xss'][0] += 1
                    # HTML 위변소 모듈 1, 2, 3, 4 번 발생 SUB모듈 
                    elif module == "HTML":
                        if submodule == 1:
                            module_data["code"][1] += 1
                        elif submodule == 2:
                            module_data["url_safe"][1] += 1
                        elif submodule == 3:
                            module_data["jquery"][1] += 1
                        elif submodule == 4:
                            module_data["iframe"][1] += 1
                except:
                    pass

    dbManager.client.close()

    return module_data

def changeLogProgress(time, progress, change):
    # time(datetime) -> unix
    dbManager = MongoDbManager()
    query = {"time": time}
    dbManager.collection.update_one(query, {"$set" : {'progress': progress + change}})

    return True

    # 지금 해야하는거 : 로그 문서 하나 찾아서 거기 progress를 -1에서 0으로 바꾸기

def getLogProgressData(period):
    dbManager = MongoDbManager()
    data = filterByDate(dbManager, period) 
    
    log_progress_data = {}
    log_progress_data['-1'] = [] # 이벤트 발생
    log_progress_data['0'] = [] # 처리중
    log_progress_data['1'] = [] # 완료
    log_progress_data['2'] = [] # 완료
    log_progress_data['3'] = [] # 완료

    for d in data:
        unixtime = d['time']
        time = datetime.datetime.fromtimestamp(unixtime).strftime('%H:%M:%S')
        module = d['module']
        progress = d['progress']
        
        row = [unixtime, time, module]

        log_progress_data[f'{progress}'].append(row)

    dbManager.client.close()

    return log_progress_data

def getLoadTimeMinMax(period):
    dbManager = MongoDbManager()
    data = filterByDate(dbManager, period) 
    #  Min max median
    load_data = {}
    load_data["min"] = []  # float 
    load_data["max"] = []  # float
    load_data["median"] = []  # float

    request_times = []

    for d in data:
        # url_data = d["url"]d -> db sorting
        try:
            request_time = d['response_time']
        except:
            request_time = d['request_time']
        request_times.append(request_time)
    
    load_data["min"] = min(request_times)
    load_data["max"] = max(request_times)
    load_data["median"] = np.median(request_times)

    dbManager.client.close()

    return load_data

def getTotalData(period):
    dbManager = MongoDbManager()
    data = filterByDate(dbManager, period) 

    total_data = []

    for d in data:
        time = d['time']
        time = datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%dT%H:%M:%S.%f')
        url = d['url']
        xpath = d['xpath']
        status_code = d['status_code']

        try:
            request_time = d['response_time']
        except:
            request_time = d['request_time']

        detection = d['detection']
        module = d['module']
        progress = d['progress']

        try:
            logdata = d['logdata']
        except:
            logdata = "-"

        row = [time, url, xpath, status_code, request_time, module, str(detection), progress, logdata]

        total_data.append(row)
    
    return total_data