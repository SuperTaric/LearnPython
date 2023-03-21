"""
剑指Offer 22.链表中倒数第K个节点
快慢指针
"""

def getKthFromEnd(head, k):
    fast, slow = head, head
    while fast and k > 0:
        fast, k = fast.next, k -1
    while fast:
        fast, slow = fast.next, slow.next
    return slow

"""
141.环形链表
快慢指针
"""

def hasCycle(head):
    if not head or not head.next:
        return False
    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True


