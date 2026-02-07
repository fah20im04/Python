x = int(input())

max = 0
current = 0
    
for _ in range(x):
    exit, enter = map(int, input().split())
    current -= exit
    current += enter
    
    if current > max:
        max = current
            
    
print(max)