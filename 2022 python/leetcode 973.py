import heapq
class Solution(object):
    def kClosest(self, points, k):
        if len(points)<=1:
            return points
        distance=[(x**2+y**2, x, y) for x,y in points]
        heapq.heapify(distance)
        res=heapq.heappop(distance)
        ans=[list(res[1:])]
        for w in range(k-1):
            p=heapq.heappop(distance)
            ans.append(list(p[1:]))
        return ans

'''
heap=[]
for (x,y) in points:
    dist=-(x*x+y*y)
    if len(heap)==k:
        heapq.heappushpop(heap,(dist,x,y))
    else:
        heapq.heappush(heap,(dist,x,y))
return [(x,y) for (dist,x,y) in heap]
'''

s=Solution()
print(s.kClosest([[1,3],[-2,2]],k=1))
print(s.kClosest([[3,3],[5,-1],[-2,4]],k=2))