class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def buildTree(self,preorder,inorder):
        if inorder:
            i=inorder.index(preorder.pop(0))
            root=TreeNode(inorder[i])
            root.left=self.buildTree(preorder,inorder[0:i])
            root.right=self.buildTree(preorder,inorder[i+1:])
            return root

s=Solution()
print(s.buildTree([3,9,20,15,7],[9,3,15,20,7]))