#!/usr/local/bin/python3

from selenium import webdriver
import os
from queue import Queue
import requests
from bs4 import BeautifulSoup
from anytree import AnyNode, RenderTree
from anytree.importer import DictImporter
from anytree.exporter import JsonExporter

import time
import json
from tpllist.modules.MainCrawling import Client


OPTIONS = webdriver.ChromeOptions()  # 크롬 옵션 객체 생성
OPTIONS.add_argument('headless')  # headless 모드 설정
OPTIONS.add_argument("window-size=1920x1080")  # 화면크기(전체화면)
OPTIONS.add_argument("disable-gpu")
OPTIONS.add_argument("disable-infobars")
OPTIONS.add_argument("--disable-extensions")

# 속도 향상을 위한 옵션 해제
prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'plugins': 2, 'popups': 2,
                                                    'geolocation': 2, 'notifications': 2,
                                                    'auto_select_certificate': 2, 'fullscreen': 2,
                                                    'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                                    'media_stream_mic': 2, 'media_stream_camera': 2,
                                                    'protocol_handlers': 2, 'ppapi_broker': 2,
                                                    'automatic_downloads': 2, 'midi_sysex': 2,
                                                    'push_messaging': 2, 'ssl_cert_decisions': 2,
                                                    'metro_switch_to_desktop': 2,
                                                    'protected_media_identifier': 2, 'app_banner': 2,
                                                    'site_engagement': 2, 'durable_storage': 2}}
OPTIONS.add_experimental_option('prefs', prefs)

# PATH = os.path.abspath(path="/home/none-31d/django-test/tpl-test/tpllist/modules/MainCrawling/CrawlingServer.py")
PATH = "/home/none-31d/django-test/tpl-test/tpllist/modules/MainCrawling/chromedriver"


class Server:
    def __init__(self, name, URL):
        super().__init__()

        self.DRIVER = webdriver.Chrome(PATH, options=OPTIONS)
        # self.DRIVER.implicitly_wait(5)  # 페이지가 로딩 될 때까지 최대 5초 기다리기...

        self.name = name
        self.SITEURL = URL
        self.SITESERVER = None
        self.INTERNAL_LINKS = set()
        self.EXTERNAL_LINKS = []
        self.EXTERNAL_LINKS_CHECK = set()
        self.JAVASCRIPTS = []
        self.JAVASCRIPTS_CHECK = set()
        self.RESOURCES = []
        self.RESOURCES_CHECK = set()

        self.HTML_CODE = None
        self.URL_QUEUE = None
        self.NEXT_URL = None

        self.SITETREE = [[] for _ in range(100)]
        self.ROOTNODE = None

        self.StartTime = None

    def GetServer(self):
        req = requests.get(self.SITEURL)
        ServerName = req.headers['server']

        l = ServerName.split(' ')
        if len(l) >= 3:
            ServerName = " ".join(l[:2])

        return ServerName


    def GetData(self):
        self.StartTime = time.time()

        # 루트노드 추가
        self.ROOTNODE = AnyNode(name=self.SITEURL, data=self.SITEURL)
        self.SITETREE[0].append(self.ROOTNODE)

        # BFS 시작
        self.URL_QUEUE = Queue()

        self.URL_QUEUE.put(self.SITEURL)
        self.INTERNAL_LINKS.add(self.SITEURL)

        while not self.URL_QUEUE.empty():
            self.NEXT_URL = self.URL_QUEUE.get()

            #print(self.NEXT_URL, "로 접근")

            self.DRIVER.get(self.NEXT_URL)

            try:
                alert = self.DRIVER.switch_to_alert()
                self.DRIVER.close()
                print("경고창 있음")
            except:
                pass

            self.GetLinks()
            self.GetJavaScripts()
            self.GetResources()


    def GetLinks(self):
        links = self.DRIVER.find_elements_by_xpath("//a[@href='https://' or 'http://']")
        for link in links:
            link = link.get_attribute('href')
            if link is None or link == '':
                continue

            cmd = self.CheckURL(link)

            if cmd == 0:
                continue

            link = self.LinkPreProcessing(link)

            if cmd == 1:  # External Link
                if link not in self.EXTERNAL_LINKS_CHECK:
                    self.EXTERNAL_LINKS_CHECK.add(link)
                    self.EXTERNAL_LINKS.append([self.NEXT_URL, link])
            elif cmd == 2:  # Internal Link
                if link not in self.INTERNAL_LINKS:
                    self.INTERNAL_LINKS.add(link)
                    self.URL_QUEUE.put(link)
                    # SITETREE에 추가
                    self.AddTree(link)

            elif cmd == 3:  # Resources
                if link not in self.RESOURCES_CHECK:
                    self.RESOURCES.append([self.NEXT_URL, link])


    def CheckURL(self, url):
        if url.endswith('.png') or url.endswith('.jpg') or url.endswith('.jpeg') or url.endswith('.gif'):  # Resources
            return 3
        if url.startswith(self.SITEURL):  # Internal Link
            return 2
        if url.startswith('http://') or url.startswith('https://'):  # External Link
            return 1
        return 0


    def LinkPreProcessing(self, link):
        if '?' in link:
            link = link[:link.index('?')]
        if '#' in link:
            link = link[:link.index('#')]
        if link[-1] == '/':
            link = link[:-1]
        return link


    def AddTree(self, link):
        link = link.replace(self.SITEURL, '')
        dict_link = [i for i in list(link.split('/')) if i != '']

        now_html = self.SITEURL

        for i in range(len(dict_link)):
            flag = 0
            pre_html = now_html
            now_html = pre_html + "/" + dict_link[i]
            for j in range(len(self.SITETREE[i + 1])):
                if self.SITETREE[i + 1][j].data == now_html:
                    flag = 1
                    break
            if flag:
                continue
            for j in range(len(self.SITETREE[i])):
                if self.SITETREE[i][j].data == pre_html:
                    newNode = AnyNode(name=dict_link[i], parent=self.SITETREE[i][j], data=now_html)
                    self.SITETREE[i + 1].append(newNode)
                    break


    def GetJavaScripts(self):
        links = self.DRIVER.find_elements_by_xpath('//script')
        for link in links:
            link = link.get_attribute('src')
            if link is None or link == '':
                continue

            link = self.LinkPreProcessing(link)

            if link not in self.JAVASCRIPTS_CHECK:
                self.JAVASCRIPTS_CHECK.add(link)
                self.JAVASCRIPTS.append([self.NEXT_URL, link])


    def GetResources(self):
        links = self.DRIVER.find_elements_by_xpath('//img')
        for link in links:
            link = link.get_attribute('src')
            if link is None or link == '':
                continue

            if link not in self.RESOURCES_CHECK:
                self.RESOURCES_CHECK.add(link)
                self.RESOURCES.append([self.NEXT_URL, link])


    def CreateJSON(self):
        exporter = JsonExporter(indent=4)
        filename = './sitemap.json'

        with open(filename, 'w') as f:
            exporter.write(self.ROOTNODE, f)

        # ex_dict = {"data": []}
        # js_dict = {"data": []}
        # re_dict = {"data": []}

        # for i in module.EXTERNAL_LINKS:
        #     ex_dict['data'].append({'url': i[0], 'ex_url': i[1]})

        # for i in module.JAVASCRIPTS:
        #     js_dict['data'].append({'url': i[0], 'js_url': i[1]})

        # for i in module.RESOURCES:
        #     re_dict['data'].append({'url': i[0], 're_url': i[1]})

        # with open('./ex.json', 'w') as f:
        #     json.dump(ex_dict, f, indent='\t')

        # with open('./js.json', 'w') as f:
        #     json.dump(js_dict, f, indent='\t')

        # with open('./resources.json', 'w') as f:
        #     json.dump(re_dict, f, indent='\t')
        
    def returnJSON(self):
        with open('./sitemap.json') as json_file:
            json_data = json.load(json_file)
            return json_data

    # def AddJSON(self):
    #     self.Client.file_upload('./sitemap.json', '/home/ubuntu/sitemap/maincrawling/bob9-MUZE.json')
    #     self.Client.file_upload('./ex.json', '/home/ubuntu/external_link/bob9-MUZE.json')
    #     self.Client.file_upload('./js.json', '/home/ubuntu/javascript/bob9-MUZE.json')
    #     self.Client.file_upload('./resources.json', '/home/ubuntu/image/bob9-MUZE.json')


# if __name__ == "__main__":
def showSitemap(URL):
    module = Server('bob9-MUZE', URL)

    print('크롤링 시작.')
    start = time.time()
    module.GetData()
    print('크롤링 및 데이터 추출 완료.')
    print('소요 시간 : ' + str(time.time() - start))

    start = time.time()
    module.CreateJSON()
    print('데이터 -> JSON 파일 변환 완료.')
    print('소요 시간 : ' + str(time.time() - start))

    # start = time.time()
    # module.AddJSON()
    # print('JSON 파일 -> DB 서버 업로드 완료.')
    # print('소요 시간 : ' + str(time.time() - start))
    # start = time.time()
    sitemap_json_data = module.returnJSON()

    print("작업 끝.")

    #module.CreateJSON()
    #module.Client.AddJsonData()
    #module.DB.Insert_Site()

    # 세션 닫기
    # module.Client.close()
    #module.Client.close()
    #module.DB.close()

    return sitemap_json_data


# res = showSitemap("http://3.131.17.188/")
# print(type(res))
