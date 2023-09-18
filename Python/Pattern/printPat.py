"""
For N = 2 the pattern will be 
2 2 1 1
2 1
Input: 2
Output:
2 2 1 1 $2 1 $ 


For N = 3 the pattern will be 
3 3 3 2 2 2 1 1 1
3 3 2 2 1 1
3 2 1
Input: 3
Output:
3 3 3 2 2 2 1 1 1 $3 3 2 2 1 1 $3 2 1 $
"""
def printPat(n):
    #Code here
    y = n
    for i in range(n):
        x = n
        for j in range(n):
            for k in range(y):
                print(x, end=" ")
            x = x-1
        print('$', end="")
        y = y-1
