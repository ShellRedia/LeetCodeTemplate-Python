class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
--- 从此处复制 ---
'''
def ListNode2Array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

def Array2ListNode(arr):
    cur = head = ListNode()
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return head.next