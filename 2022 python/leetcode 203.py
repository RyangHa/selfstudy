class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def removeElements(self,head, val):
        if head is None:
            return head

        new=ListNode(next=head)
        p=new
        while p.next:
            if p.next.val==val:
                p.next=p.next.next
            else:
                p=p.next
        return new.next

#s=Solution()