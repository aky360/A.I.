def squareRoot(x: int)->int:
    left, right, result=1, x, 0
    while(left<right):
        mid = int(left + (right-left)/2)
        if(mid<x/mid):
            left = mid+1
        else:
            right = mid
        
    return left if(left == x/left) else left-1
    
    
if __name__ == "__main__" :
        print(squareRoot(4096))
        print(squareRoot(1048))
        print(squareRoot(121))
