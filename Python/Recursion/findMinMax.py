def getMin(arr, n):
	if(n==1):
		return arr[0]
	else:
		return min(getMin(arr[1:], n-1), arr[0])
		
def getMax(arr, n):
	if(n==1):
		return arr[0]
	else:
		return max(getMax(arr[1:], n-1), arr[0])

# Driver code
arr = [12, 1234, 45, 67, 1]
n = len(arr)

for i in range(len(arr)):
    print(arr[i:])

print("Minimum element of array: ",getMin(arr, n));
print("Maximum element of array: ",getMax(arr, n));
