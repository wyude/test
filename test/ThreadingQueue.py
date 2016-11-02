#coding=utf-8

import queue
import threading
import time

class threadingQueue(threading.Thread):
    def __init__(self,name,q):
        threading.Thread.__init__(self);
        self.name=name;
        self.q=q;
    def run(self):
        while(True):
            #time.sleep(5);
            #print("%s threading start \n"%self.name);
            a=self.q.get();
            print('------',a,'-----\n');
            self.q.task_done();
            

if __name__=='__main__':
    data=[1,2,3,4,5,6,7,8,9,0];
    qTmp=queue.Queue();
    for i in data:
        qTmp.put(i);
    for j in range(3):
        t=threadingQueue(str(j),qTmp);
        t.setDaemon(True);
        t.start();
    qTmp.join();
    print('All Done !');