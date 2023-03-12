class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

a=ListNode(1)
b=ListNode(2)
c=ListNode(4)
d=ListNode(1)
e=ListNode(3)
f=ListNode(4)

a.next=b
b.next=c
c.next=None
d.next=e
e.next=f
f.next=None

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        first=list1
        second=list2
        result=head=ListNode()
        while list1 and list2:
            if list1.val<=list2.val:
                head.next=list1
                list1=list.next
            else:
                head.next=list2
                list2=list2.next
        

s=Solution()
print(s.mergeTwoLists(a,d))
