# ktx = [1,2,3]
# sum = ktx[0] + ktx[1] + ktx[2]
# print(sum)

#-----------------------------------------------------------------
# ktx = [1,2,3,4,5,6,7,8,9,10]
# sum = ktx[0] + ktx[1] + ktx[2] + ktx[3] + ktx[4] + ktx[5] + ktx[6] + ktx[7] + ktx[8] + ktx[9]
# print(sum)

# sum = 0
# ktx = [1,2,3,4,5,6,7,8,9,10]
# for i in range(0,10,1):
#     sum += ktx[i]
# print(sum)


#append사용해서 추가하기---------------------------------------
'''
sum = 0
ktx = []#ktx=[]초기값이 없는 상태
ktx.append(1)
ktx.append(2)
ktx.append(3)
ktx.append(4)
ktx.append(5)
for i in range(0,5):
    sum += ktx[i]
print(sum)    
'''

# sum = 0
# ktx = []#ktx=[]초기값이 없는 상태
# for i in range(1,101):
#     ktx.append(i)
# for j in range(0,100):
#     sum += ktx[j]
# print(sum)

#리스트 접근 범위 지정
#ktx = [10,20,30,40,50,60,70]
# print(ktx[0:2])
# print(ktx[0:5])
# print(ktx[2:6])
# print(ktx[:3])
# print(ktx[3:])

#리스트연산
# ktx = [10,20,30]
# tgv = [40,50,60]
# print(ktx + tgv)
# print(ktx * 3)

# ktx = [10,20,30,40]
#리스트 수정
# ktx[0] = 100
# ktx[2] = 300
#리스트의 값추가
# ktx[2:3] = [300, 301, 302]
#리스트 삭제
# del(ktx[2])
#리스트 여러 항목 한 번에 삭제
# ktx[1:3] = []
# print(ktx)
