#encoding=utf-8
import urllib;
import urllib.request;
import http.cookiejar;

class browserTest:
    def __init__(self):
        self.__url='http://www.jianshu.com/';
        self.__cookieJ=http.cookiejar.CookieJar();#添加cookie
        self.__HCPro=urllib.request.HTTPCookieProcessor(self.__cookieJ);
        self.__header={#从fiddler复制的header，当然还有别的东西
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
            'Connection': 'keep-alive',
            'Host': 'www.jianshu.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.jianshu.com/sign_in',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6''
            };
        self.__opener=urllib.request.build_opener(self.__HCPro);
        self.__opener.addheaders=self.__header;

    def go(self):
        #self.__req=urllib.request.Request(url=self.__url,headers=self.__header);
        #self.__res=urllib.request.urlopen(self.__req);
        #print(self.__res.read());
        self.__url +='sign_in';
        f=open('e:/a.html','w',encoding='utf-8');
        f.write(self.__res.read().decode('utf-8'));
        f.close();
        print('Done !');

if __name__=='__main__':
    app=browserTest();
    app.go();