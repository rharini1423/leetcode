# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp=head
        while temp:
            while temp.next!=None and temp.val == temp.next.val:
                temp.next=temp.next.next
            temp=temp.next
        return head
            