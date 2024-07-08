class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        def helper(n, k):
            if n == 1:
                return 0 # 0 based index

            return (k + helper(n - 1, k)) % n

        return helper(n, k) + 1 # 0 based index but 1<=n
#TC:O(N)  #SC: O(n)