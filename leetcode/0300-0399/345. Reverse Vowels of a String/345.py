class Solution:
    def reverseVowels(self, s: str) -> str:
        sList = list(s)
        l, r = 0, len(s) - 1
        d = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}

        while l < r:
            if sList[l] in d and sList[r] in d:
                temp = sList[l]
                sList[l] = sList[r]
                sList[r] = temp
                l += 1
                r -= 1

            elif sList[l] not in d:
                l += 1

            else:
                r -= 1

        return "".join(sList)
