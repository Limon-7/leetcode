class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

# TC:O(1) and SC:O(1)