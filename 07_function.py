# 사칙연산 계산기 만들기
# def plus(a,b):
#     return a + b

# def minus(a,b):
#     return a - b

# def multiple(a,b):
#     return a * b

# def divide(a,b):
#     return a/b

# num1 = int(input('첫 번째 수를 입력하시오 :'))
# num2 = int(input('두 번째 수를 입력하시오 :'))
# result = plus(num1,num2)
# print(result)
# result = minus(num1,num2)
# print(result)
# result = multiple(num1,num2)
# print(result)
# result = divide(num1,num2)
# print(result)

#구구단 출력 코드를 함수로 만들기
# def gugudan(dan):
#     for val in range(1,10,1):
#         print('%d * %d = %d' % (dan,val,dan*val))

# val = int(input('단수를 입력하세요:'))
# gugudan(val)

#계정 정보 검사 코드 함수로 만들기 
# id = 'jamsuham75'
# pw = '1234'

# def account(userid,userpw):
#     if id == userid:
#         if pw == userpw:
#             print('로그인되었습니다')
#         else:
#             print('패스워드가 틀렸습니다')
#     else:
#         print("아이디가 틀렸습니다")

# userid = input('사용자 아이디:')
# userpw = input('사용자 비밀번호:')
# account(userid,userpw)

#커피 자판기 코드 작성
# coffee = ''
# coffee = input('커피를 선택하시오(아메리카노,카페라떼,카페모카):')
# print()
# print('1.물을 준비한다')
# print('2.컵을 준비한다')

# if coffee == '아메리카노':
#     print('3.아메리카노를 탄다.')
# elif coffee == '카페라떼':
#     print('3.카페라떼를 탄다.')
# elif coffee == '카페모카':
#     print('3.카페모카를 탄다.')
# else:
#     print('3.아무거나 탄다')

# print('4. 물을 붓는다')
# print()
# print(coffee,'한잔 서비스 완료')

#커피 자판기 코드 작성
# coffee = '아메리카노'

# def coffee_machine(sel_coffee):
#     print('1.물을 준비한다')
#     print('2.컵을 준비한다')

#     if sel_coffee == '아메리카노':
#         print('3.아메리카노를 탄다.')
#     elif sel_coffee == '카페라떼':
#         print('3.카페라떼를 탄다.')
#     elif sel_coffee == '카페모카':
#         print('3.카페모카를 탄다.')
#     else:
#         print('3.아무거나 탄다')
#     print('4. 물을 붓는다')

# for i in range(0,3):
#     print('-------------------------------------------------------')
#     coffee = input('커피를 선택하시오(아메리카노,카페라떼,카페모카):')
#     print()
#     coffee_machine(coffee)
#     print()
#     print(coffee,'한잔 서비스 완료')