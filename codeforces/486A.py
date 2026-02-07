x = int(input())

evenSum = x//2
oddSum = (x+1)//2

total = evenSum*(evenSum+1) - oddSum*oddSum
print(total)

