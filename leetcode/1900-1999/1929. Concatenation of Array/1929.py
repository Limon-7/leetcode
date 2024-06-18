class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for _ in range(2):
            for i in nums:
                ans.append(i)
        return ans
# TC:O(n) and SC: O(N)