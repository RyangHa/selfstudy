def runningSum(nums):
    running_Sum=[]
    for i in range(0,len(nums)):
        Sum=sum(nums[:i+1])
        running_Sum.append(Sum)
    return running_Sum

print(runningSum([1,2,3,4])) #[1,3,6,10]
print(runningSum([1,1,1,1,1])) #[1,2,3,4,5]
print(runningSum([3,1,2,10,1])) #[3,4,6,16,17