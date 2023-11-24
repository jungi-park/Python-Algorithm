def solution(today, terms, privacies):
    answer = []
    todayY,todayM,todayD = map(int,today.split("."))
    for term in terms:
        num = 1
        kind, plusMonth = map(str,term.split())
        for privacie in privacies:
            privacieDday,privacieKind = map(str,privacie.split())
            if kind == privacieKind:
                privacieY,privacieM,privacieD = map(int,privacieDday.split("."))
                privacieM += int(plusMonth)
                while privacieM>12:
                    privacieM -=12
                    privacieY +=1
                if todayY > privacieY or (todayY == privacieY and todayM > privacieM) or (todayY == privacieY and todayM == privacieM and todayD >= privacieD):
                    answer.append(num)
            num +=1
                
    answer.sort() 
    return answer