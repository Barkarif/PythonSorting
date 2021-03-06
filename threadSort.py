import threading 
import time

class threadSort(threading.Thread):
    def __init__(self, randArray, sortName):
        threading.Thread.__init__(self)
        self.randArray = randArray
        self.sortName = sortName

    def run(self):
        startTime = time.time()
        copyOfRandArray = self.randArray.copy()
        sortedArray = self.sortName(copyOfRandArray)
        print(self.sortName.__name__ , sortedArray, (time.time()-startTime))