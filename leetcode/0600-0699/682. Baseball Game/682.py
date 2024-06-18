class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for i in operations:
            if i == "+":
                scores.append(scores[len(scores) - 1] + scores[len(scores) - 2])
            elif i == "C":
                scores.pop()
            elif i == "D":
                scores.append(2 * scores[-1])
            else:
                scores.append(int(i))
                
        return sum(scores)
# SC:O(N)+O(N)=O(N)