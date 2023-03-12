import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        if not nums:
            return None
        large=[]
        for num in nums:
            heapq.heappush(large,num)
            if k<len(large):
                heapq.heappop(large)
        return large[0]

s=Solution()
print(s.findKthLargest([3,2,1,5,6,4],2))