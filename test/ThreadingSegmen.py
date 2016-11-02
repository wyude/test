#coding=utf-8
import threading
import time

class Num:
    def __init__(self):
        self.num=0;
    def add(self):
        self.num +=1;
    def get(self):
        return self.num;

class threadingSema(threading.Thread):
    def __init__(self,s,n):
        threading.Thread.__init__(self);
        self.s=s;
        self.n=n;
    def run(self):
        #while(True):
            self.s.acquire();#内部计数器减1
            self.n.add();
            print("当前num=",self.n.get());
            time.sleep(3);
            self.s.release();#内部计数器加1
        
        

if __name__=="__main__":
    n=Num();
    s=threading.Semaphore(3);
    threads=[];
    for i in range(10):
        t=threadingSema(s,n);
        t.setDaemon(True);
        t.start();
    t.join();
       
