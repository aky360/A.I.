# Iterative way.
def revArray(A, start, end):
	while start < end:
		A[start], A[end] = A[end], A[start]
		start += 1
		end -= 1

A = [1,2,3,4,5,6,7]
revArray(A, 0, 6)
print("reversed list is :", A)



# Recursive python program to reverse an array
# Function to reverse A[] from start to end
def reverseList(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList(A, start+1, end-1)
 
# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
reverseList(A, 0, 5)
print("Reversed list is :", A)

