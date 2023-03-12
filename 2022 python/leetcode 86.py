class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
a=ListNode(1)
b=ListNode(4)
c=ListNode(3)
d=ListNode(2)
e=ListNode(5)
f=ListNode(2)

a.next=b
b.next=c
c.next=d
d.next=e
e.next=f
f.next=None

class Solution(object):
    def partition(self, head, x):
        original,a=head,head
        new=ListNode()
        b=new
        while a.next:
            if a.next.val>=x:
                b.next=a.next
                a.next=a.next.next
                b=b.next
            else:
                a=a.next
        a.next=new.next
        return original

s=Solution()
print(s.partition(a,3))