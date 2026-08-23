
class Solution:
    def preorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root is not None:
            res.append(root.val)
            self.helper(root.left, res)
            self.helper(root.right, res)