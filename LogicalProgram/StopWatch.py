"""
*Author : Prathamesh Tibile
*Date   : 30-07-21
*Time   : 10-00 AM
*Title  : Simulate StopWatch program
"""
import time

try:
    while True:
        # print("Enter 1 to Start Time:");
        start = int(input("Enter 1 to Start:"))
        startTime = time.time()
        stop = int(input("Enter 0 to Stop Time:"))
        endTime = time.time()
        timeElapsed = endTime - startTime
        print("Time elapsed from Start to Stop is: ", timeElapsed, " Sec")
except ValueError:
    print("Invalid input ")