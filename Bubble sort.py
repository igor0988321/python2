import time
import os
import random

def show(arr):
    show_lst = [[" " for _ in range(len(arr))] for _ in range(max(arr))]

    for i in range(len(arr)):
        for j in range(arr[i]):
            show_lst[j][i] = "*"

    show_lst.reverse()

    for row in show_lst:
        print(' '.join(row))

    time.sleep(0.1)
    os.system('cls')




def sort(arr):

    for i in range(len(arr)):
        for j in range(len(arr)- 1):
            if arr[j] >= arr[i+1]:
                arr[j], arr[j+1] =  arr[j+1], arr[j]
                show(arr)



lst = [random.randint(1,12) for _ in range(20)]
sort(lst)