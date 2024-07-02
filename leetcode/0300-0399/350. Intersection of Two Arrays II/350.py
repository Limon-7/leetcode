class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        res = []

        for val in nums1:
            if val in d:
                d[val] += 1
            else:
                d[val] = 1

        for val in nums2:
            if val in d and d[val] >= 1:
                res.append(val)
                d[val] -= 1

        return res
#TC: O(n) Spc:O(min(n,m))
# Approach 2
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return res
# TC: O(n Log n + m Log n) SC: O(min(n,m))