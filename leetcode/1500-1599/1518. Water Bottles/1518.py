class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles

        while numBottles >= numExchange:
            numBottles = numBottles - numExchange + 1
            res += 1

        return res
