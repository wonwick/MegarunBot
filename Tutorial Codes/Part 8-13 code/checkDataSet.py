import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2
import time

i=1


train_data = np.load('G:/mlDataset/training_data-210.npy')
df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

for data in train_data:
    img = data[0]
    choice = data[1]
    cv2.imshow('test',cv2.resize(img,(300,560)))
    
    print(choice)
    if choice!=[0,0,0,0,1]:
        time.sleep(3)

    if cv2.waitKey(25)& 0xFF==ord('q'):
        cv2.destroyAllWindows()
        break
   
