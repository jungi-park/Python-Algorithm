from collections import deque

n = int(input())

books = deque()

for _ in range(n):
    book = int(input())
    books.append(book)

result = 0

while books:
    if books.pop() == n:
        n -= 1
    else:
        result+=1

print(result)