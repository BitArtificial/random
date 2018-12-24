# -*- coding: utf-8 -*-
import time

class Random:
    def __init__(self):
        self.result=[]
        
    def run(self,seed=int(time.time())%100,idx=-1,num_of_rand=1): 
        if idx==num_of_rand:
            return
        a=69069
        b=2019110513
        m=4294967296
        x=(a*seed+b)%m
        if idx!=-1:
            x_dom=x/10**int(len(str(x)))
#            print(x_dom)
            self.result.append(x_dom)
        idx+=1
        return self.run(seed=x,idx=idx,num_of_rand=num_of_rand)
    
    def randint(self,start=1,stop=100,num_of_rand=1,seed=int(time.time())%100):
        self.run(seed=seed,idx=-1,num_of_rand=10)
        return [int(num*stop) for num in self.result]
    def random(self,num_of_rand=1,seed=int(time.time())%100):
        self.run(seed=seed,idx=-1,num_of_rand=1)
        return self.result
    def uniform(self,start=1,stop=100,num_of_rand=1,seed=int(time.time())%100):
        #等我有时间看了均匀分布的相关概念再说，不想写了
        pass
if __name__ == '__main__':
    rm=Random()
    result=rm.randint(start=1,stop=100,num_of_rand=20)
