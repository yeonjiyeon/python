# 지역변수
# def kyungki():
#     print('2.lee=10 변수를 메모리에 적재합니다.')
#     lee = 10
#     print('3.junla()함수를 호출하였습니다.')
#     junla()
#     print('6.lee=10 변수를 메모리에서 소멸합니다.')

# def junla():
#     print('4.lee=20 변수를 메모리에 적재합니다.')
#     lee = 20
#     print('5.lee=20 변수를 메모리에서 소멸합니다.')

# print('1.kyungki()함수를 호출하였습니다.')
# kyungki()

#전역변수
# hap = 100
# def sum(value):
#     hap = 20
#     hap = hap + value
#     print('hap 출력:',hap)

# sum(10)
# print('hap출력:',hap)

hap = 100
num = 50

def sum(value):
    global hap
    hap = hap + value
    print('hap 출력:',hap)
    print('num 출력:',num)

sum(10)
print('hap출력:',hap)