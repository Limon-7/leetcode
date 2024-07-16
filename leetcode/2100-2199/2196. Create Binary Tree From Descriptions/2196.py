# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        childrenSet = set()

        for p, c, isLeft in descriptions:
            if p not in nodes:
                nodes[p] = TreeNode(p)
            if c not in nodes:
                nodes[c] = TreeNode(c)
            if isLeft:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]

            childrenSet.add(c)

        for p, c, isLeft in descriptions:
            if p not in childrenSet:
                return nodes[p]

        return None
# TC: O(N)+O(N)~O(N)
## SC:O(N)+O(N)~O(N)