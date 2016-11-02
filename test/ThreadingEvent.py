#coding=utf-8

import threading,time

class threadingEvent(threading.Thread):
    def __init__(self,name,e):
        threading.Thread.__init__(self);
        self.name=name;
        self.e=e;
    def run(self):
        print("我是%s，我先睡一会\n"%self.name);
        self.e.wait();#默认为False，所以阻塞在这了
        print("我是%s，我被唤醒了\n"%self.name);

if __name__=='__main__':
    event=threading.Event();
    for i in range(3):
        t=threadingEvent('X'+str(i),event);
        t.setDaemon(True);
        t.start();
    print("sleep 5 seconds\n");
    time.sleep(5);
    event.set();
    t.join();
    print("Done !");