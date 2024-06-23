class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        n = len(nums)
        r = n - 1

        def reverse(nums: List[int], l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        k %= n  # this will handle overflow of array size
        reverse(nums, l, r)
        reverse(nums, 0, k - 1)
        reverse(nums, k, r)
#TC: O(N)