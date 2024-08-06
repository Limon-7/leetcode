class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = [0] * 26
        res = dist = 0

        for char in word:
            cnt[ord(char) - ord("a")] += 1

        cnt.sort(reverse=True)

        for c in cnt:
            res += c * (1 + dist // 8)
            dist += 1

        return res