text = input().strip().split()
print(text)
result = text[0][0].upper()
noneWords = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']

for word in text[1:]:
    if word not in noneWords:
        result += word[0].upper()

print(result)