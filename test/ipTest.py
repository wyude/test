import urllib;
import urllib.request;

ipList=['123.7.115.141:9999',
        '183.129.151.130:80',
        '27.184.133.128:8888',
        '27.151.220.13:8888',
        '119.28.19.222:8888',
        '27.8.190.68:8888',
        '121.204.165.9:8118',
        '60.21.209.114:8080',
        '113.3.74.103:8118',
        '122.193.14.106:82',
        '123.56.74.13:8080',
        '122.96.59.107:843',
        '124.88.67.63:80',
        '202.171.253.72:80',
        '175.17.227.36:8888',
        '111.162.16.191:8888',
        '218.3.177.36:8089',
        '123.170.10.93:8888',
        '182.203.4.176:8888',
        '115.28.32.191:8081',
        '113.0.110.68:8118',
        '221.219.184.76:81',
        '183.129.178.14:8080'
        ];

def AIpTest():
    for ip in ipList:
        try:
            ipStr="'"+ip+"'";
          #  #proxy_handler=urllib.request.ProxyHandler({'http':'jp02.ipip.re:1080'});
           # proxy_auth_handler=urllib.request.ProxyBasicAuthHandler();
           # opener=urllib.request.build_opener(proxy_handler);
            #data=opener.open('http://www.baidu.com',timeout=3);

          #  data=opener.open('http://www.google.com');
            data=urllib.request.urlopen('http://www.google.com');
            dataR=data.read();
            #print(dataR);
            if(dataR):
                print('ok');
            else:
                print('no');
        except:
            print("except");
            continue;

AIpTest();