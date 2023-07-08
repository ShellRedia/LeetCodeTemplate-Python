# 链表转数组:
def ListNode2Array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr
arr = ListNode2Array(head)

# 数组转链表:
def Array2ListNode(arr):
    cur = head = ListNode()
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return head.next
head = Array2ListNode(arr)

# 数组转BST(二叉搜索树):
def Array2BST(arr):
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
root = Array2BST(arr)