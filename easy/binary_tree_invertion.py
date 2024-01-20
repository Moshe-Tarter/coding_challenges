# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self) -> str:
        return f'{self.val}\n{self.left.val}  {self.right.val}'
        
        
        
def invert(root: TreeNode) -> TreeNode:
    if root is None or (root.left is None and root.right is None):
        return True
    if root.left and root.right:
        root.left, root.right = root.right, root.left
    else:
        invert(root.left)
        invert(root.right)
        
        
def invert2(root: TreeNode) -> TreeNode:
    if root is None:
        return None
    if root:
        print(root.left, root.right)
    root.left, root.right = invert2(root.right), invert2(root.left)
    
    return root
    
def print_tree(node):
    if node is not None:
        print_tree(node.left)
        print(node.value, end=' ')
        print_tree(node.right)

if __name__ == '__main__':

    tree = TreeNode(1, left=TreeNode(1, left=TreeNode(3), right=TreeNode(4)), right=TreeNode(2, left=TreeNode(4), right=TreeNode(3)))
    new_tree = invert2(tree)

