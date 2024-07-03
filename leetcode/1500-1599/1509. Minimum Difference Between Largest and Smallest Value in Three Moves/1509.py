class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0

        nums.sort()
        res = float("inf")

        for l in range(4):
            r = 3 - l
            res = min(res, nums[n - 1 - r] - nums[l])

        return res
#TC: O(nlogn)+O(C) # SC:O(1)