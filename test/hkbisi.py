#encoding=utf-8
import urllib
import urllib.request
import http.cookiejar
import re
from collections import deque
import os
import gzip

class browserTest:
    def __init__(self,from_p=1,end_p=1111,someone=False,name=None):#someone=true指定要下载的作者False就不指定，按顺序下载
        self.__url_login='http://hkbbcc.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1';#用来登录
        self.__url_host='http://hkbbcc.com/forum.php';#验证登录后的页面什么样
        self.__header_after={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
            };
        #色色贴图发帖时间排序第一页
        self.__urlStart='http://hkbbcc.com/forum.php?mod=forumdisplay&fid=18&orderby=dateline&orderby=dateline&filter=author&page=1';
        self.__start=from_p;#这页开始
        self.__end=end_p;#这页结束
        self.__name=name;
        self.__someone=someone;
        #self.__page_deque=deque();

    def createOpener(self,header,foo=1):#创建带cookie和header的opener
        if(1 == foo):#避免重复创建
            cookieJ=http.cookiejar.CookieJar();#添加cookie
            HCPro=urllib.request.HTTPCookieProcessor(cookieJ);
            self.__opener=urllib.request.build_opener(HCPro);
        headerTmp=[];
        for key,value in header.items():
            elem=(key,value);
            headerTmp.append(elem);
        self.__opener.addheaders=headerTmp;

    def get_xsrf(self,header):
        xsrf='';
        try:
            self.createOpener(header);
            res=self.__opener.open(self.__url_xsrf);
            resdata=res.read().decode();
            redata=re.compile('<input type="hidden" name="_xsrf" value="(.+)"/>');
            xsrf=redata.findall(resdata)[1].encode();
            #print(xsrf);
        except:
            print('erro');
        return xsrf;

    def createPostData(self):
        post_data={
            'fastloginfield':'username',
            'username':'w',
            'password':'3',
            'quickforward':'yes',
            'handlekey':'ls'
        };
        poster=urllib.parse.urlencode(post_data).encode();
        return poster;

    def go(self):
        header_post={
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
            'Cache-Control':'max-age=0',
            'Content-Length':'96',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'hkbbcc.com',
            'Origin':'http://hkbbcc.com',
            'Proxy-Connection':'keep-alive',
            'Referer':'http://hkbbcc.com/forum.php',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
            };
        self.createOpener(header_post);
        __back=self.__opener.open(self.__url_login,self.createPostData());
        print(__back.read().decode());

        #验证成功登录后的样子
        #self.createOpener(self.__header_after,0);#置个0，避免新的cookie覆盖登陆时的cookie
        #print(self.__opener.open(self.__url_host).read().decode());
        pageLike=re.compile('<a href=\"(.+?)\"  onclick=\"atarget\(this\)\" title=\"(.+?)\" class=\"z\">');
        authLike=re.compile('<em class=\"sum y xs0 xi1 xw1\" title=\".+?\">.+?</em><a href=\".+?\.html\">(.+?)<');
        picLike=re.compile('<img .+? zoomfile="(.+?)" file=');
        for i in range(self.__start,self.__end):
            print("正在爬取  "+str(i)+"   页---------->");
            page=self.__urlStart[:-1]+str(i);
            self.createOpener(self.__header_after,0);#置个0，避免新的cookie覆盖登陆时的cookie

            header_bs={
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
            'Host':'hkbbcc.com',
            'Proxy-Connection':'keep-alive',
            'Referer':page,
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
        };
            try:
                pageData=self.__opener.open(page).read().decode();#打开展示页
                b=pageData.replace('amp;','');#删掉这个特殊字符
                getUrl=pageLike.findall(b);
                getAuth=authLike.findall(b);
                #print(getAuth);
                j=0;
                self.createOpener(header_bs,0);#置个0，避免新的cookie覆盖登陆时的cookie
                for mypage,dirname in getUrl:
                    #print(getAuth[j]);
                    if(self.__someone and getAuth[j] not in self.__name):
                        #print(getAuth[j] ,"not in ",self.__name);
                        j +=1;
                        continue;
                    else:
                        j +=1;
                    mypage='http://hkbbcc.com/'+mypage;
                    print('+++++'+"此页第  "+str(j)+"  帖  当前页网址--->"+mypage);
                    print('+++++'+"当前页主题--->"+dirname+'');
                    try:
                        folder='e:/loadbs/'+str(i)+'/'+dirname;
                        if(not os.path.exists(folder)):
                            os.makedirs(folder);
                        try:
                            cur_page=self.__opener.open(mypage).read();
                            try:
                                print("正在解压当前网页...............");
                                unzip_page=gzip.decompress(cur_page);
                                cur_page=unzip_page.decode();
                                print("当前网页解压完毕...............");
                            except:
                                print("网页解压失败");
                                continue;
                            pic=picLike.findall(cur_page);
                            header_pic={
                                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                                'Accept-Encoding':'gzip, deflate, sdch',
                                'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
                                'Host':'img.bipics.net',
                                'Proxy-Connection':'keep-alive',
                                'Upgrade-Insecure-Requests':'1',
                                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
                            };
                            self.createOpener(header_pic,0);#置个0，避免新的cookie覆盖登陆时的cookie
                            for picUrl in pic:
                                try:
                                    picName=picUrl.split('/')[-1];
                                    print("正在保存---》"+picName);
                                    f=open(folder+'/'+picName,'wb');
                                    #print(folder+'/'+picName);
                                    #print(picUrl);
                                    picRes=self.__opener.open(picUrl);
                                    picR=picRes.read();
                                    #picRes=urllib.request.urlopen(picUrl);
                                    f.write(picR);
                                    f.close();
                                except:
                                    print('保存图片失败');
                                    continue;
                        except:
                            print('打开链接失败'+str(j));
                            continue;
                    except:
                        print("创建文件夹失败！"+dirname);
                        continue;
            except:
                print("打开展示页失败"+str(i));
                continue;

if __name__=='__main__':
    name=['魏晴','魔幻王'];
    app=browserTest(1,200,True,name);
    app.go();
    print('Done !');
