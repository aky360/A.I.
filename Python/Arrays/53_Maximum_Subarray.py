
class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    maxSubArr = nums[0]
    currSubArr = 0
    
    for n in nums:
      if currSubArr < 0:
        currSubArr = 0
      currSubArr += n
      maxSubArr = max(maxSubArr, currSubArr)
    return maxSubArr
