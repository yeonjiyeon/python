# import os
# srcfile = 'iu.jpg'
# destfile = 'iucpy.jpg'

# if os.path.exists(srcfile):
#     sfp = open(srcfile,'rb')
#     dfp = open(destfile,'wb')
    
#     while True:
#         sbyte = sfp.read()
#         if not sbyte:
#             break
#         dfp.write(sbyte)
#     sfp.close()
#     dfp.close()
#     print('복사')
# else:
#     print('존재안함')

import os
srcfile = 'SleepAway.mp3'


if os.path.exists(srcfile):
    sfp = open(srcfile,'rb')
    
    sfp.seek(-128,2) #
    tdata = sfp.read(128)
    title = tdata[3:33].decode()
    print('제목: '+ title)
    artist = tdata[33:63].decode()
    print('음악가: '+ artist)
    mdate = tdata[93:97].decode()
    print('출시년도: '+ mdate)
    etc = tdata[97:127].decode()
    print('기타 정보: '+ etc)
    sfp.close()
    
    print('복사')
else:
    print('존재안함')
