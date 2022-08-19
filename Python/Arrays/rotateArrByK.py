class RotateArray:
    
    def rotateRight(self,arr, k):
        if(k>len(arr)):
            k = k%len(arr)
            
        result = [0]*len(arr)
        for i in range(0, k):
            result[i] = arr[len(arr)-k+i]
            
        j = 0
        for i in range(k, len(arr)):
            result[i] = arr[j]
            j += 1
        
        for i in result:
            print(i)
            
#Space is O(n) and time is O(n).

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    obj = RotateArray()
    obj.rotateRight(arr, 3)
