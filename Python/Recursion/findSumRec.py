def findSum(arr, N):
    print(len(arr))
    if len(arr)== 1:
        return arr[0]
    elif len(arr) == 0:
        return 0
    else:
        return arr[0]+findSum(arr[1:], N-1)
         
    
arr = [1,2,3,4,5,6,7,8,9]
print(arr)
print(findSum(arr, 9))

arx = []
print(findSum(arx, 0))
