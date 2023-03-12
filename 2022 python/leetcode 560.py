def subarraySum(nums, k):
    dictK={0:1}




print(subarraySum([1,1,1],2)) #2
print(subarraySum([1,2,3],3)) #2
print(subarraySum([1],0)) #0
print(subarraySum([-1,-1,1],0)) #1

'''
    while i<len(nums):
        if i>=len(nums):
            break
        elif sum==k:
            arraynum+=1
            if j==len(nums)-1:
                break
            j+=1
            sum+=nums[j]
        elif sum>=k:
            sum-=nums[i]
            i+=1
        elif j<len(nums)-1:
            j+=1
            sum+=nums[j]
        else:
            break
    return arraynum
'''