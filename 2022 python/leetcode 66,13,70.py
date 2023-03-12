def plusOne(digits):
    for i in range(0,len(digits)):
        digits[i]=str(digits[i])
    digit=''.join(digits)
    digit=int(digit)+1
    digits=list(map(int,str(digit)))
    return digits

print(plusOne([1,2,3]))

'''
def climbStairs(n):
    
'''

def romanToInt(s):
    roman=['I','V','X','L','C','D','M']
    integ=[1,5,10,50,100,500,1000]
    sum=0
    for i in range(0,len(s)):
        if s[i]
        index1=roman.index(s[i])
        sum+=integ(index1)
    return sum