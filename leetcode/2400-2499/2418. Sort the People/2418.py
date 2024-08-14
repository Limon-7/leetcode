class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {}
        for i, h in enumerate(heights):
            d[h] = names[i]
        
        res = []
        for h in reversed(sorted(heights)):
            res.append(d[h])
        
        return res
