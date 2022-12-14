class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        return all(min(len(set(row)), len(set(col))) == len(matrix) for row, col in zip(matrix, zip(*matrix)))   # all() checks all data in all() function are equal or not return T/F
