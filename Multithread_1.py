from time import  sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range (100):
            print("Hello")
            sleep(1)


class name(Thread):
    def run(self):
        for i in range(100):
            print("Pratham")
            sleep(1)

t1=Hello()
t2=name()

t1.start()
# sleep(0.2)
t2.start()