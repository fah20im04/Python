x = int(input())
diffi = list(map(int, input().split()))

for i in range(x):
    if diffi[i] > 0:
        print("HARD")
        break
else:
    print("EASY")
