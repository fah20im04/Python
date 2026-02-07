y = int(input())
def next_beautiful_year(year):
    while True:
        year += 1
        if len(set(str(year))) == len(str(year)):
            return year
        
print(next_beautiful_year(y))