class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

a=ListNode(4)
b=ListNode(1)
c=ListNode(8)
d=ListNode(4)
e=ListNode(5)
f=ListNode(5)
g=ListNode(1)

a.next=b
b.next=c
c.next=d
d.next=e
f.next=g
g.next=c
e.next=None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        node=set()
        a=headA
        b=headB
        while a:
            node.add(a)
            a=a.next
        while b:
            if b in node:
                return b
            b=b.next
        return None

s=Solution()
print(s.getIntersectionNode(a,f))
