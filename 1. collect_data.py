import numpy as np
from grabscreen import grab_screen
import cv2
import time
from getkeys import key_check
import os

w = [1,0,0,0,0]
s = [0,1,0,0,0]
a = [0,0,1,0,0]
d = [0,0,0,1,0]
nk= [0,0,0,0,1]

starting_value = 1
lastFile="asd.npy"
while True:
    file_name = 'G:/mlDataset4/training_data-{}.npy'.format(starting_value)

    if os.path.isfile(file_name):
        print('File exists, moving along',starting_value)
        starting_value += 1
    else:
        print('File does not exist, starting fresh!',starting_value)
        
        break


def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array
     0  1  2  3  4   5   6   7    8
    [W, S, A, D, WA, WD, SA, SD, NOKEY] boolean values.
    '''
    output = [0,0,0,0,0]


    if 'W' in keys:
        output = w
    elif 'S' in keys:
        output = s
    elif 'A' in keys:
        output = a
    elif 'D' in keys:
        output = d
    else:
        output = nk
    return output


def main(file_name, starting_value):
    file_name = file_name
    starting_value = starting_value
    training_data = []
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    paused = False
    print('STARTING!!!')
    while(True):
        
        if not paused:
            screen = grab_screen(region=(0,40,300,560))
            last_time = time.time()
            # resize to something a bit more acceptable for a CNN
            screen = cv2.resize(screen, (int(300/2),int(560/2)))
            # run a color convert:
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
            
            keys = key_check()
            output = keys_to_output(keys)
            training_data.append([screen,output])

            print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            cv2.imshow('window',cv2.resize(screen,(300,560)))
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

            if len(training_data) % 100 == 0:
                print(len(training_data))
                
                if len(training_data) == 100:
                    np.save(file_name,training_data)
                    print(file_name,'SAVED')
                    training_data = []
                    starting_value += 1
                    lastFile=file_name
                    file_name = 'G:/mlDataset4/training_data-{}.npy'.format(starting_value)

                    
        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)
        if 'E' in keys:
            if paused:
                training_data=[]
                time.sleep(1)
                os.remove(lastFile)           
                print('emptying current array and remove last file')
                

            else:
                print('Pausing!')
                paused = True
                time.sleep(1)
                training_data=[]
                os.remove(lastFile)           
                print('emptying current array and remove last file')



main(file_name, starting_value)
