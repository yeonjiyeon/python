import sqlite3
conn = sqlite3.connect('bookStoreDB')
print('1.DB연결성공')

cur = conn.cursor()
print('2.커서 생성성공')

cur.execute("create table if not exists bookItem(item char(100),author char(50),publisher char(50),stock int)")
print('3.테이블생성')

cur.execute("insert into bookItem values('AppInventor','ch.lee','digitalbook',100)")
cur.execute("insert into bookItem values('Python','ch.lee','digitalbook',200)")
cur.execute("insert into bookItem values('C#Programming','ch.lee','hyejiwon',300)")
cur.execute("insert into bookItem values('Javascript','ch.lee','hyejiwon',400)")
print('4.데이터 입력')

conn.commit()
print('5.데이터 저장')

cur.execute("select * from bookItem")
print('5.데이터 조회')

while(True):
    row = cur.fetchone()
    if(row == None):
        break
    print(row)
    print('7.데이터출력')

    conn.close()
    print('8.DB 연결종료')