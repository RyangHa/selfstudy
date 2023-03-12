class Stack():
    def __init__(self):
        self.top=[]
    def peek(self):
        if len(self.top)!=0:
            return self.top[-1]
    def pop(self):
        if len(self.top)!=0:
            last=self.top.pop(-1)
            return last
    def push(self,item):
        self.top.append(item)
    def isEmpty(self):
        if len(self.top)!=0:
            return False
        else:
            return True

class Solution():
    def Basic_calculator(self, string):
        s_ope=Stack()
        new=""
        for w in string:
            if w is ")":
                k=s_ope.pop()
                new+=k
            elif w in "(+-*/":
                s_ope.push(s)
            else:
                new+=w
        while not s_ope.isEmpty():
            new+=s_ope.pop()

        for w in new:
            if w not in "+-*/":
                s_ope.push(w)
            else:
                a=s_ope.pop()
                b=s_ope.pop()
                if w=="+":
                    now=a+b
                elif w=="-":
                    now=a-b
                elif w=="*":
                    now=a*b
                else:
                    now=a/b
                s_ope.push(now)

        return now



s=Solution()
print(s.Basic_calculator("2*(5+5*2)/3+(6/2+8)")) #21
print(s.Basic_calculator("(2+6*3+5-(3*14/7+2)*5)+3")) #-12