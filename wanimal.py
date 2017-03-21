# encoding=utf-8
import urllib;
import urllib.request;
import re;
from collections import deque;

class DownLoadPic:#先来个类，用它来下载wanimal的图喽
    #######################################
    #学到点什么呢，就是类里面的这个全局变量更类似于C++里面的static
    #是所有类共享的
    #哈哈，事实不是这样的
    #self.value这样访问变量就不是static，即非共享，
    #self.__class__.value这样访问才是static，原来还和访问方式有关！！！
    #######################################
    __m_deque=deque();#存放将要访问的下一页
    __m_visited=set();#根据集合的特性，存放已经访问过网址，包括图片的和下一页的
    #存放解析出来的网址，就是为了看结果对不对
    #__file=open('e:/forLook.txt','w',encoding='utf-8');
    #__adress=open('e:/adress.txt','w',encoding='utf-8');
    __url_init="";#入口初始化
    __m_cnt=0;#当前第几页
    __page_limit=0;#入口开始的页数限制
    #######################################
    #学到点什么呢，这个就是构造函数了，而且所有的函数都必须有参数self
    #注意到这些变量和函数前面的__了吧，加了__就是私有的
    #######################################
    def __init__(self,url_tmp,cnt_limit=99999999):#初始化
        self.__url_init=url_tmp;
        self.__m_deque.append(self.__url_init);
        self.__m_cnt=0;
        self.__page_limit=cnt_limit;

    def __del__(self):
        self.__url_init='';
        self.__m_cnt=0;
        self.__m_visited={};
        self.__m_deque=[];
        #self.__file.close();
        #self.__adress.close();
    
    def DLP(self):#有了网址就开始解析下载了
        while(self.__m_deque and self.__m_cnt<=self.__page_limit):
            #print(self.__m_deque);
            cur_url=self.__m_deque.popleft();
            self.__m_visited |={cur_url};
            print("已经抓取 ",self.__m_cnt," 页 +++","当前网页--->",cur_url,"\n");
            self.__m_cnt +=1;
            try:
                url_opening=urllib.request.urlopen(cur_url);
            except:
                #self.__file.write("网页打开失败--->"+cur_url+"\n");
                continue;
            if 'html' not in url_opening.getheader('Content-Type'):
                continue;
            try:
                page_data=url_opening.read().decode('utf-8');
            except:
                #self.__file.write("网页解码失败--->"+cur_url+"\n");
                continue;
            linkNext='http://wanimal1983.org/page/'+str(self.__m_cnt);#哈哈，先默认从第一页开始吧
            self.__m_deque.append(linkNext);#把下一页放到待解析队列
            self.__m_visited |={linkNext};#访问过的网页
            imageDiv=re.compile('<img src=.+?>');#img标签
            imageLink=re.compile('http:.+?\.jpg');#图片连接
            nameLike=re.compile('[^/]+\.jpg');#取出图片名称
            for img in imageDiv.findall(page_data):#取出当前页所有ima标签
                #print(len(imageDiv.findall(page_data)));
                imgLink=imageLink.findall(img);#从当前img标签取出图片连接
                if(1 <= len(imgLink)):
                    get_img=imgLink[0];
                else:
                    continue;
                if 'http' in get_img and get_img not in self.__m_visited:
                    self.__m_visited |={get_img};
                    name=nameLike.findall(get_img)[0];#取出图片名字
                    #self.__file.write("图片名字-->"+name+"\n");
                    #self.__file.write("图片链接-->"+get_img+"\n");
                    print("正在保存图片",name,end="==========\n");
                    #self.__adress.write(get_img+"\n");
                    try:
                        #添加代理
                        #proxy_handler=urllib.request.ProxyHandler({'http':'218.66.253.146:8800'});
                        #proxy_auth_handler=urllib.request.ProxyBasicAuthHandler();
                        #opener=urllib.request.build_opener(proxy_handler,proxy_auth_handler);
                        #请求数据
                        #pic=opener.open(get_img);
                        pic=urllib.request.urlopen(get_img);
                        #好像可以用这个保存文件直接
                        #urllib.request.urlretrieve(link,saveFile(link));
                        picResource=pic.read();
                        picFile=open("e:/"+name,"wb");#暂时直接爬是不行的，好像图片服务器禁止了简单爬虫，那就下一次在伪装浏览器行为，先把链接都保存下来，用其他下载器下载吧
                        picFile.write(picResource);
                        picFile.close();
                    except:
                        #self.__file.write("图片打开失败-->\n\n\n");
                        continue;

if __name__=="__main__":
    a=DownLoadPic("http://wanimal1983.org/",10);
    a.DLP();
    #del a;
