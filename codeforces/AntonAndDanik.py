x = int(input())
s = input().upper()
aCount = 0
dCount = 0
for i in range(x):
    if s[i] == 'A':
        aCount +=1
    else: 
        dCount +=1
if aCount>dCount:
    print('Anton\n')
elif dCount>aCount:
    print('Danik')
else:
    print('Friendship')
