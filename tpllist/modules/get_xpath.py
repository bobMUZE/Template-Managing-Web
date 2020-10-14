import webview
from bs4 import BeautifulSoup
import requests

'''
Function List..

1. 선택 or id 속성 값 Template화 (완료)
1-1. 선택 Template 영역을 확인하는 기능을 넣어야 됨 (완료)
2. HTML Injection을 이용한 웹 데이터 제어 (완료)
2-1. a 태그 href 속성 지우고 호출 (완료)
3. Response 기능 추가로 반환 값을 이용한 Beautifulsoup 데이터 제어 추가 (완료)
3-1. Return Value = Xpath (완료)
4. href 기능 비활성화 (완료)
'''
class Show:
    def __init__(self, site, template):
        try:
            self.template = '\"' + template + '\"'
            self.site = site
            self.ShowResult()
        except:
            pass

    def ShowResult(self):
        window = webview.create_window('Template Result', self.site)
        webview.start(self.ShowTemplate, window, debug=True)

    def ShowTemplate(self, window):
        window.move(200, 100)
        window.resize(1500, 850)
        print(self.template)
        result = window.evaluate_js(
            r"""
            var id = """ + r'{}'.format(self.template) + """
            document.getElementById(id).setAttribute("style", "background-color:rgba(255, 99, 71, 0.7); border-width:thick; border-color:red");
            """
        )

def IdRun(target, select_target):
    req = requests.get(target)
    req.encoding = 'utf-8'
    res = req.text

    soup = BeautifulSoup(res, 'html.parser')
    try:
        text = soup.find('div', class_=select_target).attrs
        return GetTemplate(text)
    except:
        GetTemplate('Selector is Not Defined...')

def TemplateRun(target):
    window = webview.create_window('Template', target, js_api=api)
    webview.start(HTMLInjection, window)
    try:
        return {'xpath': api.xpath, 'divid': api.divid}
    except:
        GetTemplate('Selector is Not Defined...')

def GetTemplate(text):
    if type(text) == str:
        print(text)
        return text
    elif text.get('id'):
        print('id:', text['id'])
        return text['id']
    else:
        print('Selector is Not Defined...')
        return 'Selector is Not Defined...'

def HTMLInjection(window):
    window.move(200, 100)
    window.resize(1500, 850)
    result = window.evaluate_js(
        r"""
        var arr = [];
        var d = document.getElementsByTagName('div');
        var div_blacklist = [undefined, null, "", "container", "NM_INT_LEFT"];
        var ptag_blacklist = [undefined, "BODY"];

        // div 중분류
        for (var i in d) {
            if (div_blacklist.indexOf(d[i].id) == -1){
                if (ptag_blacklist.indexOf(d[i].parentNode.tagName) == -1){
                    arr.push(document.getElementById(d[i].id));
                }
            }
        }

        // div 하이라이팅
        for (var j in arr) {
            arr[j].setAttribute("onclick", "template(this)");
            arr[j].setAttribute("onmouseover", "this.style.backgroundColor=\"rgba(255, 99, 71, 0.7)\"; this.style.borderWidth=\"thick\"; this.style.borderColor=\"rgba(255, 99, 71, 0.7)\"");
            arr[j].setAttribute("onmouseout", "this.style.backgroundColor=''; this.style.borderWidth=''; this.style.borderColor=''");
        }

        // href 비활성화
        var ahref = document.querySelectorAll('a[href]');
        for (var x in ahref) {
            var abs = ahref[x].attributes;
            for (var y in abs) {
                if (abs[y].name == "href") {
                    ahref[x].setAttribute(abs[y].name, "javascript:void(0)");
                } else if (abs[y].name == "class") {
                } else if (abs[y].name != "href") {
                    ahref[x].setAttribute(abs[y].name, "");
                }
            }
        }

        // Get XPath Function
        var xpath = ''; 
        function xPath(elem) {
            if ( elem.parentNode == document ) {
                xpath = '/' + xpath;
            }
            else {
                var siblingIndex = 1;
                var prevSibling = elem.previousSibling;

                while(prevSibling != null) {
                    if(prevSibling.tagName == elem.tagName)
                    siblingIndex++;
                    prevSibling = prevSibling.previousSibling;
                }

                if (elem.tagName == "HTML" || elem.tagName == "BODY")
                    xpath = '/' + elem.tagName + xpath;
                else
                    xpath = '/' + elem.tagName + '[' + siblingIndex + ']' + xpath;
                xPath(elem.parentNode);
            }
        }

        function getXPath(elem) {
            xpath = '';
            xPath(elem);
            return xpath;
        }

        function wait(msecs) {
            var start = new Date().getTime();
            var cur = start;
            while(cur - start < msecs) {
                cur = new Date().getTime();
            }
        }

        // div Response
        function template(test) {
            var divid = test.id;
            var xpath = getXPath(document.getElementById(divid));
            wait(10);
            pywebview.api.GetJSValue(xpath, divid, 1);
        }
        """
    )
    api.SetDestory(window)

class Api:
    def __init__(self):
        self.flag = 0
        self.xpath = ''
        self.divid = ''

    def GetJSValue(self, xpath, divid, flag):
        self.xpath = xpath
        self.flag = flag
        self.divid = divid
        if self.flag == 1:
            try:
                self.window.destroy()
                exit(0)
            except:
                exit(0)
            
    def SetDestory(self, window):
        self.window = window
        
'''
0 : Run Template
1 : input id Attribute
'''
def TemplateFunction(num, target, select_target):
    if num == 1:
        return IdRun(target, select_target)
    else:
        return TemplateRun(target)

def get_xpath():
    # Webview Setting
    api = Api()

    # Web Site
    # 네이버, 워드프레스, 그누보드, 제로보드
    target_url = ['http://61.251.255.136/main', 'http://218.146.55.65/wordpress/index.php/about/', \
    'http://218.146.55.65/g5/', 'http://218.146.55.65/xe/']

    # Web Site DIV Tag Attribute (id, class)
    select_target = 'group_title'
    #select_target = 'a'

    # 0 is Run Webview Template
    # 1 is Run input id Attribute Template
    # TemplateFunction(TemplateStyle, SiteURL, IDAttribute)
    # template = {xpath, divid}
    template = TemplateFunction(0, target_url[0], select_target)

    # Show Template Result
    show = Show(target_url[0], template['divid'])
