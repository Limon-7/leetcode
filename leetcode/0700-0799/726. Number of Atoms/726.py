class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [{}]
        l, r = 0, len(formula)

        while l < r:
            atom = formula[l]
            if atom == "(":
                stack.append({})
                l += 1
            elif atom == ")":
                currMap = stack.pop()
                l += 1
                cnt = ""
                
                while l < r and formula[l].isdigit():
                    cnt += formula[l]
                    l += 1

                cnt = 1 if not cnt else int(cnt)
                for e in currMap:
                    currMap[e] *= cnt

                prevMap = stack[-1]
                for e in currMap:
                    if e in prevMap:
                        prevMap[e] += currMap[e]
                    else:
                        prevMap[e] = currMap[e]
            else:
                cnt = ""
                if l + 1 < r and formula[l + 1].islower():
                    atom = formula[l : l + 2]
                    l += 1

                while l + 1 < r and formula[l + 1].isdigit():
                    cnt += formula[l + 1]
                    l += 1
                cnt = 1 if not cnt else int(cnt)

                currDic = stack[-1]
                if atom in currDic:
                    currDic[atom] += cnt
                else:
                    currDic[atom] = cnt
                l += 1

        cntMap = stack[-1]
        res = ""

        for atom in sorted(cntMap.keys()): ## O(nlogN)
            cnt = "" if cntMap[atom] == 1 else str(cntMap[atom])
            res += atom + cnt

        return res
## TC: O(N^2) + O(klogK)~O(N^2)
## SC: O(K)