# 链表转数组:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class ListNodeConvert:
    def ln2arr(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr
    def arr2ln(self, arr):
        cur = head = ListNode()
        for x in arr:
            cur.next = ListNode(x)
            cur = cur.next
        return head.next
    def ln_assign(self, head, arr):
        i = 0
        while head and i < len(arr):
            head.val = arr[i]
            head = head.next
            i += 1

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