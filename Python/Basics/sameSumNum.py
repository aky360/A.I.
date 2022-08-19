# Python3 implementation of the approach
from collections import defaultdict

# Function to return the maximum
# count of pairs with equal sum
def maxCountSameSUM(arr, n):

	# Create a map to store frequency
	M = defaultdict(lambda:0)
	print("M ", M.keys())
	print("M ", M.values())

	# Store counts of sum of
	# all pairs in the map
	for i in range(0, n - 1):
		for j in range(i + 1, n):
		  #  print(arr[i],"+", arr[j])
			M[arr[i] + arr[j]] += 1
# 			print(M[arr[i] + arr[j]])

	max_count = 0
	
	print("updata ",M[9])
	M[9] = M[9] + 1
	print("updata ",M[9])
	
	print("Mk ", M.keys())
	print("Mv ", M.values())
	
	print("MM ", M.items())
	
# 	print("updata ",M[9]+1)

	# Find maximum count
	for ele in M:
		if max_count < M[ele]:
			max_count = M[ele]

	return max_count

# Driver code
if __name__ == "__main__":

	arr = [1, 8, 3, 11, 4, 9, 2, 7]
	n = len(arr)
	print(maxCountSameSUM(arr, n))
