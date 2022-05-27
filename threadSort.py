import threading 

class threadSort(threading.Thread):
    def __init__(self, randArray, methodName):
        threading.Thread.__init__(self)
        self.randArray = randArray
        self.methodName = methodName

    def run(self):
        copyOfRandArray = self.randArray
        self.methodName(copyOfRandArray)
        print(self.methodName , copyOfRandArray)