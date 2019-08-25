# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ans = []
        stack = []
        curr = root

        def traverse_left(curr):
            while curr.left:
                stack.append(curr)
                curr = curr.left
            stack.append(curr)

        traverse_left(curr)
        while stack:
            curr = stack.pop()
            ans.append(curr.val)
            if curr.right:
                traverse_left(curr.right)

        return ans
