#coding=utf-8

import threading;
import time;

class Goods:
    def __init__(self):
        self.__num=0;
    def add(self):
        self.__num+=2;
    def sub(self):
        self.__num-=1;
    def get(self):
        return self.__num;
    def empty(self):
        if(self.__num > 0):
            return False;
        else:
            return True;

class Producer(threading.Thread):
    def __init__(self,name,con,num):
        threading.Thread.__init__(self);
        self.__name=name;
        self.__con=con;
        self.__goods=num;
        print('creat Producer\n');
        

    def run(self):
        print('start Producer\n');
        con=self.__con;
        goods=self.__goods;
        while(True):
            con.acquire();#取得条件变量
            if(not goods.empty()):
                con.wait();#有足够的产品，就可以停下来等待，也就是释放资源了
            else:
                goods.add();
                print('producer>>>>>>%d'%goods.get());
                con.notify();#发出消息，我准备好了，释放资源了，可以来用了
                print('producer done !');
            con.release();#彻底释放了
            time.sleep(2);

class Consumer(threading.Thread):
    def __init__(self,name,con,num):
        threading.Thread.__init__(self);
        self.__name=name;
        self.__con=con;
        self.__goods=num;
        print('create Consumer');

    def run(self):
        print('start Consumer');
        con=self.__con;
        goods=self.__goods;
        while(True):
            con.acquire();#取得条件变量
            if(goods.empty()):
                print('consumer waiting......');
                con.wait();#没有产品，等待生产，
            else:
                goods.sub();
                print('consuming......%d'%goods.get());   
                con.notify();#发出通知，没货了，快生产
                print('consumer done !');
            con.release();
            time.sleep(5); 




if __name__=='__main__':
    
    con=threading.Condition();#条件变量
    goods=Goods();

    c=Consumer('consumer',con,goods);
    p=Producer('producer',con,goods);

    c.setDaemon(True);
    p.setDaemon(True);

    c.start();
    p.start();

    c.join();
    p.join();