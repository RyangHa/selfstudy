import heapq
from collections import Counter
class Solution(object):
    def reorganizeString(self, s):
        res=[]
        c=Counter(s) #dict형태로 key, 갯수 저장
        re=[(-value,key) for key,value in c.items()]
        heapq.heapify(re)
        p_a, p_b= 0, ''
        while re:
            a, b= heapq.heappop(re)
            res+=[b]
            if p_a<0:
                heapq.heappush(re,(p_a,p_b))
            a+=1
            p_a, p_b= a,b
        res=''.join(res)
        if len(res)!=len(s):
            return ''
        return res

s=Solution()
print(s.reorganizeString("aab"))
print(s.reorganizeString("tndsewnllhrtwsvxenkscbivijfqnysgvaaucewehob"))