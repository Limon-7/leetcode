class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        h1, h2 = {}, {}
        for x, y in zip(s, t):
            if (x in h1 and h1[x] != y) or (y in h2 and h2[y] != x):
                return False
            h1[x] = y
            h2[y] = x
        return True
#TC:O(n) and SC: O(C) > C= charecter set: 256