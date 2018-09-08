import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2
import time

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
The_training_data = []

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
            
    ##        print(choice)
    ##        if choice!=[0,0,0,0,1]:
    ##            time.sleep(3)
            if choice==[1,0,0,0,0]:
                pw+=1
                if(choice!=last):
                    w+=1
                    last=choice
                    The_training_data.append([img,choice])
                
            if choice==[0,1,0,0,0]:
                ps+=1
                if(choice!=last):
                    s+=1
                    last=choice
                    The_training_data.append([img,choice])
                
            if choice==[0,0,1,0,0]:
                pa+=1
                if(choice!=last):
                    a+=1
                    last=choice
                    The_training_data.append([img,choice])

            if choice==[0,0,0,1,0]:
                pd+=1
                if(choice!=last):
                    d+=1
                    last=choice
                    The_training_data.append([img,choice])

            if choice==[0,0,0,0,1]:
                pnk+=1
                if(choice!=last):
                    nk+=1
                    last=choice
                    The_training_data.append([img,choice])
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

def saveFrameSet(file_name,training_data):
    np.save(file_name,training_data)
    print(file_name,'SAVED')


    
saveFrameSet(file_name,The_training_data)
