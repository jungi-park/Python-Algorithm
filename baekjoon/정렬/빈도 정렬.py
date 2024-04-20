n,c = map(int,input().split())

message = list(map(int,input().split()))

messageCount = []
already = set()

for i in message:
    if i not in already:
        already.add(i)
        messageCount.append({i:message.count(i)})

messageCount.sort(key= lambda x : list(x.values())[0],reverse=True)


for m in messageCount:
    d = list(m.items())[0]
    k = d[0]
    v = d[1]
    for _ in range(v):
        print(k,end=" ")