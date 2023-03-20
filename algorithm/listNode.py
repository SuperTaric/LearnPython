"""
剑指Offer 22.链表中倒数第K个节点
快慢指针
"""

def getKthFromEnd(head, k):
    fast, slow = head, head
    while fast and k > 0:
        fast, k = fase.next, k -1
    while fast:
        fast, slow = fast.next, slow.next
    return slow


