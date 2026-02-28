arr = [1,2,3,4,5,6,7,8,9, 10, 55, 98]
print(arr)
a = int(input("enter the number you want to find in the list:"))
target = a

left = 0
right = len(arr)-1

while left <= right:

    mid = (left + right)//2

    if arr[mid] == target:
        print('index:', mid)
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

