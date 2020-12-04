#read()함수사용------------------------
# fName = 'poem.txt'
# fp = open(fName, 'r')
# print(fp.read())
# fp.close()


#readline---------------------------------
# fName = 'poem.txt'
# fp = open(fName, 'r')
# strline = fp.readline()
# print(strline)

# strline = fp.readline()
# print(strline)
# fp.close()

# fName = 'poem.txt'
# fp = open(fName, 'r')
# while True:
#     strline = fp.readline()
#     if strline == '':
#         break
#     print(strline)
# fp.close()


# fName = 'poem.txt'
# fp = open(fName, 'r')
# strline = fp.readlines()
# for strlist in strline:
#     print(strlist)
# fp.close()


#파일체크함수
# -------------------
# import os #파일을 관리하는 것은 운영체제이므로 운영체제를 임포트해야한다
# fName = input('파일명을 입력하세요:')
# print()
# if os.path.exists(fName):
#     fp = open(fName, 'r')
#     strline = fp.readlines()

#     for strlist in strline:
#         print(strlist)
#     fp.close()
# else: #예외처리를 해주는 것은 필요하다
#     print('%s파일은 존재하지 않습니다' % fName)    


#with파일을 자동으로 닫아줌-----------------------------------
# import os
# fName = input('파일명을 입력하세요:')
# if os.path.exists(fName):
#     with open(fName, 'r') as fp:
#         strline = fp.readlines()
#         for strlist in strline:
#             print(strlist) 
# else: #예외처리를 해주는 것은 필요하다
#     print('%s파일은 존재하지 않습니다' % fName) 

#파일에 데이터 쓰기
# fName = 'file2.txt'
# with open(fName,'w') as fp:
#     while True:
#         instr = input('데이터 입력:')

#         if instr == '\q':
#             break
#         fp.writelines(instr + '\n')

import os
srcfile = 'poem.txt'
destfile = 'dest.txt'
if os.path.exists(srcfile):
    sfp = open(srcfile,'r')
    dfp = open(destfile,'w')

    slist = sfp.readlines()
    for instr in slist:
        dfp.writelines(instr)
    sfp.close()
    dfp.close()

    print('복사')
else:
    print('존재하지 않음')