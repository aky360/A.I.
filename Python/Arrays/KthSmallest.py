"""
A Min-Heap and a Max-Heap can be implemented in Python using the heapq library for the Min-Heap and modifying its behavior to achieve a Max-Heap. 
Python does not provide a built-in Max-Heap, but you can simulate it by pushing the negative of each element into the heapq Min-Heap.
"""

import heapq
class Solution:

    def kthSmallest(self, arr,k):
        arr.sort()
        return arr[k-1]


    def kthSmallest(self, arr,k):
        heapq.heapify(arr)
        ans,i = 0,1
        while arr:
            if(i==k):
                ans = arr[0]
                break
            i+=1
            heapq.heappop(arr)
        return ans


    def kthSmallest(self, arr,k):
        heapq.heapify(arr)
        for i in range(1,k):
            heapq.heappop(arr)
        return heapq.heappop(arr)


==========================================================================================================================================

"""
Alternative in one single line code for find the kth smallest and kth largest value from the heap in python. 
You can also use built-in functions heapq.nsmallest() and heapq.nlargest() for a simpler solution.
"""
import heapq
arr = [10000, 11, 445, 1, 330, 30000,-1]
heapq.heapify(arr)
print(arr)        # arr is converted into min heap
# removed=heapq.heappop(arr)
# print(removed)
k=3
kth_smallest = heapq.nsmallest(k, arr)[-1]
kth_largest = heapq.nlargest(k, arr)[-1]
print(kth_smallest,kth_largest)




