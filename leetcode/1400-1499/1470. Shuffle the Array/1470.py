class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arrs = []
        for i in range(n):
            arrs.append(nums[i])
            arrs.append(nums[i + n])
        return arrs

# TC:O(N) SC:O(N)