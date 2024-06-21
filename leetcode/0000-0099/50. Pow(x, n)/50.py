class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        nn = abs(n)
        while nn:
            if nn % 2:
                res *= x
                nn -= 1
            else:
                x = x * x
                nn = nn // 2
        return res if n > 0 else 1 / res
# TC: O(log N)