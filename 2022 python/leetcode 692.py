import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        count=[]
        for w in set(words):
            count.append((-words.count(w),w))
        heapq.heapify(count)
        res=[]
        for _ in range(k):
            k1=heapq.heappop(count)
            res.append(k1[1])
        return res

'''
ans=[]
counter= Counter(words)
heap=[]
for key in counter:
    heapq.heappush(heap,(-counter[key],key))
for _ in range(k):
    if heap:
        ans+=[heapq.heappop(heap)[1]]
return ans
'''

s=Solution()
print(s.topKFrequent(["i","love","leetcode","i","love","coding"], k = 2))
print(s.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4))