#기본 if문 동작원리----------------------------------------
# a = 9
# if a > 10:
#     '''
#     print('a는 10보다 큽니다.') if문 범위
#     '''
# print('a는 10보다 작습니다.')    #if문 밖

# 기본 if문 동작원리2----------------------------------------
# a = 11
# if a > 10:
#     print('a는 10보다 큽니다.') 
#     print('콘솔에 출력이 됩니다')
#     print('조건문 참 쉽죠잉~!')

# else문 동작원리----------------------------------------
# a = int(input('정수를 입력하세요:'))
# if a > 10:
#     print('a는 10보다 큽니다.') 
# else:
#     print('a는 10보다 작습니다.')

# if문 중첩----------------------------------------
# id = 'jamsuham75'
# pw = '1234'

# userid = input('사용자 아이디:')
# userpw = input ('사용자 비밀번호:')

# if id == userid:
#     if pw == userpw:
#         print('로그인 되었습니다')
#     else:
#         print('패스워드가 틀렸습니다')
# else:
#     print('아이디가 틀렸습니다')

# if elif else---------------------------------------
# subject = input('favorite subject:')

# if subject == 'python':
#     print('내가 좋아하는 과목은 파이썬입니다')
# elif subject == 'java':
#     print('내가 좋아하는 과목은 자바입니다')
# elif subject == 'C#':
#     print('내가 좋아하는 과목은 C#입니다')
# else:
#     print('내가 좋아하는 과목은 없습니다')

#if~elif~else~------------------------
# shortcut = int(input('단축키를 입력하세요:'))
# if shortcut == 1:
#     print('엄마 :010-1234-xxxx')
# elif shortcut == 2:
#     print('아빠 :010-5234-xxxx')
# elif shortcut == 3:
#     print('동생 :010-6234-xxxx')
# elif shortcut == 4:
#     print('친구 :010-7234-xxxx')
# else:
#     print('해당 단축키가 없습니다')

#if~elif~else2------------------------
# month = int(input('월을 입력하세요: '))
# if month == 12 or month < 3 and month> 0:
#     print('겨울입니다')
# elif month > 2 and month < 6:
#      print('봄입니다')
# elif month > 5 and month < 9:
#      print('여름입니다')
# elif month >8 and month < 12:
#      print('가을입니다')
# else:
#     print('입력값이 잘못되었습니다')

#if~elif~else3------------------------
# point = int(input('점수를 입력하세요:'))
# if point <=100 and point > 90:
#     print('A')
# elif point <=90 and point > 80:
#     print('B')
# elif point <=80 and point > 70:
#     print('C')
# elif point <=70 and point > 60:
#     print('D')
# elif point <=60 and point > 0:
#     print('F')
# else:
#     print('입력값이 잘못되었습니다')
    
#if~elif~else4------------------------
# print('====자판기 메뉴====')
# print('1.음료 1000원 2.과자 2000원 3.껌 500원')

# craker = 2000
# drink = 1000
# ggum = 500
# money = int(input('insert Coin :'))

# if money >= craker:
#     print('과자,음료,껌 모두 구매할 수 있습니다')    
# elif money < craker and money >= drink:
#     print('음료,껌 구매할 수 있습니다')
# elif money < drink and money >= ggum:
#     print('껌 구매할 수 있습니다')
# else:
#     print('아무것도 구매할 수 없습니다')
#pass-------------------------------
idnum = input('나이를 입력하세요:')
if int(idnum) >= 19:
    pass
else:
    print('신분증을 제시하세요')