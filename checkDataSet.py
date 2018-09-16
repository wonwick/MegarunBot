import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2
import time
from random import shuffle

i=1
j=0
w=0
s=0
a=0
d=0
nk=0
pw=0
ps=0
pa=0
pd=0
pnk=0

last=[0,0,0,0,0]
k=0
train_data=[]
The_training_data_w = []
The_training_data_s = []
The_training_data_a = []
The_training_data_d = []
The_training_data_nk= []
The_training_data = []


flag=True

while (k<5):
    k+=1
    j=0
    
    while (j<211):
        j+=1
        datafile='G:/mlDataset{}/training_data-{}.npy'.format(k,j)
        try:
            train_data = np.load(datafile)
        except Exception as e: 
            print(e)
            continue
        
        #print(df.head())
        #print(Counter(df[1].apply(str)))
        print(j)

        for data in train_data:
            img = data[0]
            choice = data[1]
            #cv2.imshow('test',cv2.resize(img,(300,560)))
            img=cv2.resize(img,(30,56))
            
    ##        print(choice)
    ##        if choice!=[0,0,0,0,1]:
    ##            time.sleep(3)
            if choice==[1,0,0,0,0]:
                pw+=1
                if(choice!=last or flag):
                    w+=1
                    last=choice
                    The_training_data_w.append([img,choice])
                
            if choice==[0,1,0,0,0]:
                ps+=1
                if(choice!=last or flag):
                    s+=1
                    last=choice
                    The_training_data_s.append([img,choice])
                
            if choice==[0,0,1,0,0]:
                pa+=1
                if(choice!=last or flag):
                    a+=1
                    last=choice
                    The_training_data_a.append([img,choice])

            if choice==[0,0,0,1,0]:
                pd+=1
                if(choice!=last or flag):
                    d+=1
                    last=choice
                    The_training_data_d.append([img,choice])

            if choice==[0,0,0,0,1]:
                pnk+=1
                if(choice!=last or flag):
                    nk+=1
                    last=choice
                    The_training_data_nk.append([img,choice])
    print("next folder")
                
##            if cv2.waitKey(25)& 0xFF==ord('q'):
##                cv2.destroyAllWindows()
##                break

print("w:",w)
print("s:",s)
print("a:",a)
print("d:",d)
print("nk:",nk)
print("pw:",pw)
print("ps:",ps)
print("pa:",pa)
print("pd:",pd)
print("pnk:",pnk)

file_name = 'G:/TheMLDataset/The_training_data.npy'

def balanceDataset(w,s,a,d,nk):
    minim=min(len(w),len(s),len(a),len(d),len(nk))
    print(minim)
    shuffle(w)
    shuffle(s)
    shuffle(a)
    shuffle(d)
    shuffle(nk)
    result=[]
    length=minim-1
    result+=w[:length]
    result+=s[:length]
    result+=a[:length]
    result+=d[:length]
    result+=nk[:length]
    return result
    
    
def saveFrameSet(file_name,training_data):
    np.save(file_name,training_data)
    print(file_name,'SAVED')

The_training_data=balanceDataset(The_training_data_w,The_training_data_s,The_training_data_a,The_training_data_d,The_training_data_nk)
print(len(The_training_data))
saveFrameSet(file_name,The_training_data)
