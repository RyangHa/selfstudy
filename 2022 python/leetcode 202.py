def twoSum(numbers, target):
    i,j= 0, len(numbers)-1
    while numbers[i]+numbers[j]!=target:
        if (numbers[i]+numbers[j])<target:
            i+=1
        else:
            j-=1
    return [i+1,j+1]

print(twoSum([2,7,11,15], 9))
print(twoSum([2,3,4], 6))
print(twoSum([-1,0], -1))
print(twoSum([0,0,3,4], 0))


        #처음 pointer index(0)
        #두 번째 pointer i: 1칸씩 이동하면서 해당 슬라이스 안에 합이 있는지 체크.