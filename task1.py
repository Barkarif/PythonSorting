import numpy as np
from utils import * 


def run():
    while True:
        sizeOfArray = input("Enter the size of the array larger then 0: ")
        if int(sizeOfArray) > 0:
            break
    randArray= np.random.randint(1,100,size=(int(sizeOfArray)))
    arrayOfSortingFunction = {bubblesort, merge_sort, insertion_sort}

    for key in arrayOfSortingFunction:
        key(randArray)