x ,y = map(int, input().split())

total = 0

height = list(map(int,input().split()))
for h in height:
    if h > y:
        total += 2
    else:
        total += 1

print(total)
