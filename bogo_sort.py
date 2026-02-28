import random
import os
import time

def bogo_sort(arr):
    while True:
        random.shuffle(arr)
        print(arr)
        os.system('cls')
        time.sleep(0.5)
        prev = arr[0]
        sort = True
        for i in range(1, len(arr)):
            if prev > arr[i]:
                sort = False
                break
            prev = arr[i]
        if sort:
            break
lst = [1,23,5,1,5,2,5,5,65,6,2]

bogo_sort(lst)