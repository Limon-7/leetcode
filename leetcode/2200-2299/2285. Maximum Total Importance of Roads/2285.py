class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        sum = 0
        for i, j in roads:
            degree[i] += 1
            degree[j] += 1

        degree.sort()

        for i in range(1, n + 1):
            sum += i * degree[i - 1]

        return sum
# TC: O(n)+O(r) + O(nlogN) + O(N) ~ O(N Log N)
# SC: O(n) + O(n) ~ O(n)