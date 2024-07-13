class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        d = {}
        for i, n in enumerate(positions):
            d[n] = i
        positions.sort()
        stack = []

        for i in positions:
            if directions[d[i]] == "R":
                stack.append(i)
            else:
                while stack and directions[d[stack[-1]]] == "R" and healths[d[i]] > 0:
                    j = stack.pop()
                    if healths[d[j]] > healths[d[i]]:
                        healths[d[j]] -= 1
                        healths[d[i]] = 0
                        stack.append(j)

                    elif healths[d[j]] < healths[d[i]]:
                        healths[d[j]] = 0
                        healths[d[i]] -= 1

                    else:
                        healths[d[j]] = 0
                        healths[d[i]] = 0

                if healths[d[i]]:
                    stack.append(i)

        return [h for h in healths if h > 0]
    
# TC: O(N)+O(NLogN)+O(N)~O(NlogN)
# SC:O(N)