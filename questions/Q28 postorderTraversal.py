class Solution:
    def postorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root is not None:
            self.helper(root.left, res)
            self.helper(root.right, res)
            res.append(root.val)