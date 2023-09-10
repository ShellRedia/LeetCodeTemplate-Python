class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def Array2BST(arr: list):
    if not arr: return None
    root = TreeNode(arr[0])
    for x in arr[1:]:
        o = root
        while o:
            if x > o.val:
                if o.right: o = o.right
                else:
                    o.right = TreeNode(x)
                    break
            else:
                if o.left: o = o.left
                else:
                    o.left = TreeNode(x)
                    break
    return root