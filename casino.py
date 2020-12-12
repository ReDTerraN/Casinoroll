#!/usr/bin/python3
import os
import glob
import time
import threading
# generate random integer values
from random import seed
from random import randint

#global variables
fileList = glob.glob('/home/andpol/Python/*.txt')

def deleteoldfiles(): #remove the files from before
    for filePath in fileList:
        try:
            os.remove(filePath)  
        except:
            print("Error while deleting file : ", filePath)

# generate some integers
def generatedata():
    amountoftimes=0
    while amountoftimes != 200:
        value=0
        money=0
        rolls=0
        while value != 1000000:
            value = randint(0, 1000000)
            money += 1
            rolls += 1
            actualmoneyspent=0
            if value == 1000000:
                actualmoneyspent= money*0.4
                amountoftimes += 1
                file1 = open("AMS.txt","a") 
                file1.write(str(actualmoneyspent))
                file1.write ('\n')
                file1.close()
                file2 = open("rolls.txt","a")
                file2.write(str(rolls))
                file2.write ('\n') 
                file2.close()
                print("Thread {0} is on loop:".format(threading.current_thread().name), amountoftimes) 
def threadcreation():
    t1 = threading.Thread(target=generatedata, name='Thread-1')
    t2 = threading.Thread(target=generatedata, name='Thread-2')
    t3 = threading.Thread(target=generatedata, name='Thread-3')
    t4 = threading.Thread(target=generatedata, name='Thread-4')
    t5 = threading.Thread(target=generatedata, name='Thread-5')
    # starting threads 1-->5 
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    # Waiting for all threads to finish..
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
def finalresults():
    print("_________________________________________________")
    with open('AMS.txt') as fh:
        sum = 0 # initialize here, outside the loop
        count = 0 # and a line counter
        for line in fh:
            count += 1 # increment the counter
            sum += float(line.split()[0]) # add here, not in a nested loop
        average = sum / count
        print ('here is the average amount of money spent:', average)
    print("_________________________________________________")
    with open('rolls.txt') as fh:
        sum = 0 # initialize here, outside the loop
        count = 0 # and a line counter
        for line in fh:
            count += 1 # increment the counter
            sum += float(line.split()[0]) # add here, not in a nested loop
        average = sum / count
        print ('here is the average amount of rolls done:', average)



#####################################################
###################### MAIN #########################
#####################################################
deleteoldfiles()

threadcreation()

finalresults()