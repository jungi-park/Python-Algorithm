from itertools import combinations

n = int(input())

ingredients = [ list(map(int,input().split())) for _ in range(n)]
result = float("inf")
for i in range(1,n+1):
    someIngredients = combinations(ingredients,i)
    for ingredient in someIngredients:
        s = 1
        n = 0
        for one in ingredient:
            s *= one[0]
            n += one[1]
        result = min(result,abs(s-n))
    

print(result)