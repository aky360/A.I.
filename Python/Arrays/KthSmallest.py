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
