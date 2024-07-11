class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        res = ""
        for ch in s:
            if ch == "(":
                stack.append(len(res))
            elif ch == ")":
                start = stack.pop()
                res = res[:start] + res[start:][::-1]
            else:
                res += ch

        return res
