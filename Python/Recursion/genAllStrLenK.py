#Print all possible strings of length k that can be formed from a set of n characters
def printSubset(strs, k):
    n = len(strs)
    printAllLengthK(strs, "", n, k)
    
    
def printAllLengthK(strs, prefix, n, k):
    #base case 
    if(k == 0):
        print(prefix)
        return 
    
    for i in range(n):
        newPrefix = prefix + strs[i]
        
        printAllLengthK(strs, newPrefix, n, k-1) 
        

        
# Driver Code
if __name__ == "__main__":
	
	print("First Test")
	set1 = ['a', 'b']
	k = 3
	printSubset(set1, k)
	
	print("\nSecond Test")
	set2 = ['a', 'b', 'c', 'd']
	k = 1
	printSubset(set2, k)
