def minSubArrayLen(target, nums):
    i, j= 0,0
    leng=set()
    while True:
        if sum(nums[i:i+j])==target:
            leng.add(j)
            if i+j==len(nums):
                return min(leng) if leng else 0
            j+=1
        elif sum(nums[i:i+j])>target:
            leng.add(j)
            if i+j==len(nums):
                return min(leng) if leng else 0
            elif i+j>len(nums):
                i+=1
                j=0
            j+=1
        elif i+j==len(nums):
            if i == len(nums)-1 :
                return min(leng) if leng else 0
            i+=1
            j=0
        else:
            j+=1

print(minSubArrayLen(7,[2,3,1,2,4,3])) #2
print(minSubArrayLen(4,[1,4,4])) #1
print(minSubArrayLen(11,[1,1,1,1,1,1,1,1])) #0
print(minSubArrayLen(11,[1,2,3,4,5])) #3