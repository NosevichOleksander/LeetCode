# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
        def addTwoNumbers(self, l1, l2):

            dummy = ListNode()
            cur = dummy

            carry = 0

            while l1 or l2 or carry:

                i1 = l1.val if l1 else 0
                i2 = l2.val if l2 else 0

                add = i1 + i2 + carry

                carry = add // 10

                cur.next = ListNode(add % 10)
                cur = cur.next

                if l1:
                    l1 = l1.next
                if l2:
                    l2 = l2.next

            return dummy.next