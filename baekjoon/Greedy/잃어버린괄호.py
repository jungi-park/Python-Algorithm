'''
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
'''

n=input()

k = n.split("-")
result = []

for num in k:
    y = 0
    n = num.split("+")
    for i in n:
        y = y+ int(i)
    result.append(y)

anser = result[0]
for n in range(1,len(result)):
    anser -= result[n]

print(anser)

    







