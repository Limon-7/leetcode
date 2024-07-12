class Solution:
    def removePair(self, s: str, pair: str, score: int) -> int:
        stack = []
        res = 0
        for ch in s:
            if ch == pair[1] and stack and stack[-1] == pair[0]:
                stack.pop()
                res += score
            else:
                stack.append(ch)

        self.s = "".join(stack)
        return res

    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        self.s = s
        pair = "ab" if x > y else "ba"
        res += self.removePair(self.s, pair, max(x, y))
        res += self.removePair(self.s, pair[::-1], min(x, y))
        return res
# TC: O(N)+O(N) ~O(N)
# SC: O(N)+O(N)+O(N)+O(N)~O(N)