#대입연산자-----------------------------------------------------
# money = int(input('돈을 넣어주세요 :'))
# count = int(input('몇 장 넣어 드릴까요?:'))
# ticket = 1200
# money -=(ticket*count)
# print('거스름돈:',money)

#-관계연산자----------------
# a = 10
# b = 11
# c = 12
# d = 10
# print('a == b의 결과는:',a == b)
# print('a < b의 결과는:',a < b)
# print('a >= c의 결과는:',a >= c)
# print('a == d의 결과는:',a == d)

#논리연산자----------------------------------
# a = 10
# b = 11
# c = 12
# d = 10
# print('not(a < 10) 의 결과는:',not(a < 10))
# print('(a < b) and (a > c) 의 결과는:',(a < b) and (a > c))
# print('(a >= c) or (a == d) 의 결과는:',(a >= c) or (a == d))

#삼항연산자----------------------------------
money = int(input('돈을 넣어주세요 :'))
count = int(input('몇 장 넣어 드릴까요?:'))
ticket = 1200
money -=(ticket*count)
#money < 0 and print('잔액이 부족합니다.금액을 투입해주세요.') or print('거스름돈:',money)
rest = '거스름돈' + str(money)
result = money < 0 and print('잔액이 부족합니다.금액을 투입해주세요.') or  rest
print(result)