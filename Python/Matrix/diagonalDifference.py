
def diagonalDifference(arr):
    x, y = 0, 0
    n = len(arr)
    
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            if(i == j):
                x += arr[i][j]
                
            if(j == n-i-1):
                y += arr[i][j]
    
    return abs(x-y)



arr = [[11, 2, 4],[4, 5, 6],[10, 8, -12]]
print("row ", len(arr))
print("column ",len(arr[0]))

print(diagonalDifference(arr))
  
  
  
