# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cont = True
        prev = None
        curr = head
        if head == None:
            return None
        if curr.next == None:
            return head
        next_node = curr.next
        
        while cont:
            curr.next = prev
            prev = curr
            curr = next_node
            if curr != None:
                next_node = curr.next
            else:
                cont = False
                
        return prev
            
