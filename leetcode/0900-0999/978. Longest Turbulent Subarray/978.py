class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = inc = dec = 1  # 1<=L

        for r in range(1, len(arr)):
            if arr[r] > arr[r - 1]:
                inc = dec + 1
                dec = 1
            elif arr[r] < arr[r - 1]:
                dec = inc + 1
                inc = 1
            else:
                inc = dec = 1
            res = max(res, inc, dec)

        return res