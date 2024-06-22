class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        d = Counter(students)
        total = len(sandwiches)

        for s in sandwiches:
            if s not in d or d[s] == 0:
                break
            else:
                d[s] -= 1
                total -= 1
        return total
## TC:O(N)+O(N)=O(N) SC: O(N) for storing in set