class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = gMax = -inf
        currMin = 0
        gMin = inf
        total = 0

        for n in nums:
            total += n
            currMax = max(currMax + n, n)
            currMin = min(currMin + n, n)
            gMax = max(gMax, currMax)
            gMin = min(gMin, currMin)

        return max(gMax, total - gMin) if gMax > 0 else gMax

#TC: O(N)