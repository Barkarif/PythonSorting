import numpy as np
from utils import * 
from threadSort import *

def run():
    while True:
        sizeOfArray = input("Enter the size of the array larger then 0: ")
        if int(sizeOfArray) > 0:
            break
    randArray= np.random.randint(1,100,size=(int(sizeOfArray)))
    arrayOfSortingModels = {bubblesort, selection_sort, insertion_sort}
    for i in arrayOfSortingModels:
        threadSorting = threadSort(randArray, i)
        threadSorting.start()
        