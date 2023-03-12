class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list2tree(values):
    def create(it):
        value=next(it)
        return None if value is None else TreeNode(value)
    if not values:
        return None
    it=iter(values)
    root=TreeNode(next(it))
    nextlevel=[root]
    try:
        while nextlevel:
            level=nextlevel
            nextlevel=[]
            for node in level:
                if node:
                    node.left=create(it)
                    node.right=create(it)
                    nextlevel+= [node.left, node.right]
    except StopIteration:
        return root
    raise ValueError("Invalid list")

class Solution:
    def pathSum(self, root, targetSum):
        res = []
        self.dfs(root, targetSum, [], res)
        return res

    def dfs(self, root, sum, ls, res):
        if root:
            if not root.left and not root.right and sum == root.val:
                ls.append(root.val)
                res.append(ls)
            self.dfs(root.left, sum - root.val, ls + [root.val], res)
            self.dfs(root.right, sum - root.val, ls + [root.val], res)


s = Solution()
root = list2tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
print(s.pathSum(root, 22))