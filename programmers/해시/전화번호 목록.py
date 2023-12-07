# 내가 생각 한답 - 효율성 2/4
def solution(phone_book):
    phone_book.sort(key = lambda x : (len(x),x),reverse=True)
    while phone_book:
        phoneNum = phone_book.pop()
        for num in phone_book:
            if phoneNum == num[:len(phoneNum)]:
                return False
    return True

# 정답
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True