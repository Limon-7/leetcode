class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle = time // (n - 1)
        remain_time = time % (n - 1)

        if cycle & 1:
            return n - remain_time
        else:
            return remain_time + 1
