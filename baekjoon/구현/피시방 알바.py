N = int(input())
people = list(map(int,input().split()))
result = set()
for p in people:
    if p not in result:
        result.add(p)

print(N-len(result))