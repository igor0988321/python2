arr1 = [1 , 2 , 3 , 4]
arr2 = [4 , 5 , 2 , 6]
arr3 = [7 , 4 , 2 , 8]

for i in arr1:
    for j in arr2:
        for k in arr3:
            if i==j==k:
                print(i)