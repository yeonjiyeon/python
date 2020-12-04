# for문의 기본원리
# for num in range(0,5,1):
#     print('Programming')

# for문의 기본원리---------------------------
# for num in range(0,5,1):
#     print(num+1,':Programming')

# for문의 기본활용---------------------------
# sum = 0
# '''
# for i in range(1,11,1):
#     sum += i
# print('1에서 10까지의 합:',sum)
# '''
# for i in range(1,1001,1):
#     sum += i
# print('1에서 1000까지의 합:',sum)

# for문의 기본활용2---------------------------
# for i in range(1,366,1):
#     print(i,'일 지났습니다')

#for문의 기본활용3---------------------------
# sum = 0
# for i in range(0,101,2):
#     sum += i
# print('1부터 100까지의 짝수합',sum)

# sum = 0
# for i in range(1,101,2):
#     sum += i
# print('1부터 100까지의 홀수합',sum)

#for문의 기본활용4 내가 좋아하는 숫자 찾기---------------------------
# start = int(input('범위 시작값:'))
# end = int(input('범위 끝값:'))
# favorite = int(input('내가 가장 좋아하는 숫자는?'))
# while True:
#     for i in range(start,end,1):
#         if(favorite == i):
#             print('내가 좋아하는 숫자가 있습니다')
#     num = int(input('이건가?'))
#     if num == favorite:
#         print('찾았습니다...')
#         break

#구구단 출력하기---------------------------
# for val in range(1,10,1):
#     print('2 * %d = %d' % (val, 2*val))
#     #print('2*',val,"=",2*val)

#구구단 출력하기--------------------------
# dan = int(input('단수를 입력하세요:'))
# for val in range(1,10,1):
#     print('%d*%d = %d' % (dan,val,dan*val))

#이중 반복문 구구단 출력하기--------------------------
# for dan in range(2,10,1):
#     for val in range(1,10,1):
#         print('%d*%d = %d' % (dan,val,dan*val),end=' ')
#     print()

#이중 반복문 별표직각삼각형 출력하기--------------------------
#해보기!!!
star = "*"
for i in range(1,6,1):
    for j in range(0,i,1):
        print(star,end=" ")
    print('')
    
