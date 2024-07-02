class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        currSet = []

        def helper(i: int) -> None:
            if i >= len(nums):
                subset.append(currSet.copy())
                return

            currSet.append(nums[i])
            helper(i + 1)

            currSet.pop()
            helper(i + 1)

        helper(0)
        return subset
#TC: O(n*2^n) SC: O(n)