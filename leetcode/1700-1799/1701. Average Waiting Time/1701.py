class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        prevTime = waitingTime = 0

        for arrival, interval in customers:
            if prevTime > arrival:
                prevTime += interval
            else:
                prevTime = arrival + interval
            # prevTime = max(prevTime, arrival) + interval
            waitingTime += prevTime - arrival

        return waitingTime / len(customers)
