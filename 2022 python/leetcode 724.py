def pivotIndex(nums):
    for i in range(0, len(nums)):
        k=sum(nums[:i + 1])
        if (k - nums[i]) == sum(nums)-k:
            return i
    return -1


print(pivotIndex(nums=[1,7,3,6,5,6])) #3
print(pivotIndex(nums=[1,2,3])) #-1
print(pivotIndex(nums=[2,1,-1])) #0

'''
    for i in range(0,len(nums)):
        if (sum(nums[:i+1])-nums[i])==sum(nums[i+1:]):
            return i
    return -1
'''