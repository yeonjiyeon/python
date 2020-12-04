#while-------------------------
# iloop = 0
# while iloop < 5:
#     print('programming')
#     iloop += 1

#while문 활용-------------------------
# sum = 0
# val = 1
# while val < 101:
#     sum += val
#     val += 2
# print('1에서 100까지의 홀수의 합',sum)


#while문 활용2-------------------------
# val = 1
# dan = int(input('단수를 입력하시오:'))
# while val < 10:
#     print(dan,'*',val,'=',dan*val)
#     val += 1

#while문 활용3-------------------------
# dan = 2
# while dan < 10:
#     val = 1
#     while val < 10:
#         print("%d * %d = %d" % (dan,val,dan*val),end=' ')
#         val += 1
#     dan += 1
#     print()

#while문 무한루프-------------------------빠져나갈 조건문이 주어지지 않았다
# iloop = 0
# while iloop < 5:
#     print('programming')

hap = 0
inum = 0
while True:
    inum = int(input('정수를 입력하세요:'))
    hap += inum
    print('누적된 합은:'+ str(hap))