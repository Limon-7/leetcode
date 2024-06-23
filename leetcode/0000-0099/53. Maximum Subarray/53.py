class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]  # 1<=length
        currSum = 0
        for r in range(len(nums)):
            currSum = max(currSum, 0) + nums[r]
            maxSum = max(maxSum, currSum)
        
        return maxSum
#TC:O(N)