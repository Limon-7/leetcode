class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for i, log in enumerate(logs):
            if log == "./":
                continue
            elif log == "../":
                if res > 0:
                    res -= 1
                else:
                    res = 0
            else:
                res += 1

        return res