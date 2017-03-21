class classA:
    publicCnt=0;
    __privateCnt=0;
    __name="";
    def __init__(self,nameTmp):
        self.__class__.publicCnt +=1;
        self.__privateCnt +=1;
        self.__name=nameTmp;
        print('init publicCnt',self.__name,self.publicCnt);
        print('init privateCnt',self.__name,self.__privateCnt);
    def __del__(self):
        self.__class__.publicCnt -=1;
        self.__privateCnt -=1;
        print('del publicCnt',self.__name,self.publicCnt);
        print('del privateCnt',self.__name,self.__privateCnt);
    def function(self):
        print('just a function');

c=classA('c');
d=classA('d');
a=classA('a');
b=classA('b');

e=classA('e');

