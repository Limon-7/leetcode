class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxV = currV = l = 0
        v = ["a", "e", "i", "o", "u"]

        for r in range(len(s)):
            if s[r] in v:
                currV += 1

            maxV = max(maxV, currV)
            if r - l + 1 == k:
                if s[l] in v:
                    currV -= 1
                l += 1

        return maxV
