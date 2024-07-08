class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = set(nums1), set(nums2)
        res = []

        for i in n1:
            if i in n2:
                res.append(i)

        return res
# TC: O(n) SC: O(n+m)

## Built-in set methods
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = set(nums1), set(nums2)
        intersection=n1.intersection(n2) # n1&n2
        return list(intersection)
# TC: O(min(n,m)) 