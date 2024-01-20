# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkSymmetry(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False

    return (left.val == right.val) and checkSymmetry(left.left, right.right) and checkSymmetry(left.right, right.left)

def isSymmetric(root):
    if root is None:
        return True

    return checkSymmetry(root.left, root.right)

if __name__ == '__main__':
    tree = TreeNode(1, left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)), right=TreeNode(2, left=TreeNode(4), right=TreeNode(3)))
    print(isSymmetric(tree)) 