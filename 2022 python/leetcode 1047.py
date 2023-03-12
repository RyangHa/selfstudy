class Stack:
    def __init__(self):
        self.top=[]

    def push(self,item):
        self.top.append(item)

    def peek(self):
        if len(self.top)!=0:
            last=self.top[-1]
            return last

    def pop(self):
        if len(self.top)!=0:
            last=self.top.pop(-1)
            return last
    def isEmpty(self):
        if len(self.top)==0:
            return True
        else:
            return False

class Solution(object):
    def removeDuplicates(self,s):
        stack = Stack()
        new=""
        for w in s:
            stack.push(w)

        prev = stack.pop()
        while not stack.isEmpty():
            crnt = stack.pop()
            if prev==crnt:
                if len(new)!=0:
                    prev=new[-1]
                    new=new[:-1]
                    continue
                prev=stack.pop()
            else:
                new+=prev
                prev=crnt
        return new[::-1]

s=Solution()
print(s.removeDuplicates("abbaca"))