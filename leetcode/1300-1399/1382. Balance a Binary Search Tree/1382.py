# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []

        def inOrder(node: TreeNode):
            if node is None:
                return
            inOrder(node.left)
            nums.append(node.val)
            inOrder(node.right)

        def insert(l, r) -> TreeNode:
            if l > r:
                return None

            mid = l + ((r - l) >> 1)
            rootNode = TreeNode(nums[mid])
            rootNode.left = insert(l, mid - 1)
            rootNode.right = insert(mid + 1, r)

            return rootNode

        inOrder(root)
        return insert(0, len(nums) - 1)
# TC: O(N) + O(logN)-> O(N) SC: O(N)+ O(logN)->O(N)