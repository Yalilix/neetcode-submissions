# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        cur = head
        while cur:
            cur = cur.next
            count += 1

        nthdel = 1 + (count - n)
        prev, cur = None, head
        while cur:
            nthdel -= 1
            if nthdel == 0:
                if prev:
                    prev.next = cur.next
                else:
                    head = head.next
                break
            tmp = cur.next
            prev = cur
            cur = tmp
        return head
