class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] in edges[1]:
            return edges[0][0]
        else:
            return edges[0][1]


# Brute Force: TC: O(N^2) and SC:O(N)
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d = {}
        for row in edges:
            for col in row:
                if col in d:
                    d[col] += 1
                else:
                    d[col] = 1

        return max(d, key=d.get)
