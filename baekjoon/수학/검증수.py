array = [i**2 for i in map(int, input().split())]

result = 0

for i in array:
    result+=i

print(result%10)