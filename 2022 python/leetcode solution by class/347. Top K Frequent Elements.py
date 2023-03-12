from typing import List
from collections import defaultdict
import heapq


def topKFrequent(nums: List[int], k: int) -> List[int]:
    if k == 0:
        return []

    # hash table 선언
    count_table = defaultdict(int)

    # nums내 각 key들의 빈도를 계산
    for num in nums:
        count_table[num] += 1

    # heap size k인 min heap 사용
    topK_heap = []
    for num in count_table:
        heapq.heappush(topK_heap, (count_table[num], num))  # 튜플로 삽입
        if k < len(topK_heap):
            heapq.heappop(topK_heap)

    # return list
    topK = []
    for count, num in topK_heap:
        topK.append(num)

    return topK


topK = topKFrequent(nums=[1, 3, 5, 3, 9, 3, 7, 5], k=2)
print(topK)