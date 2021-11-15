from calendarModule import *
import sqlite3
conn=sqlite3.connect('Calendar.db')
curs=conn.cursor()
n=0
while n != -1:
    print('1. 달력보기')
    print('2. 일정추가')
    print('3. 일정확인')
    print('4. 일정삭제')

    n = int(input( 'Choose the option please. (EXIT=-1): '))

    if n==1:
        year, month =map(int, input('년, 월을 입력해주세요(ex.2000 01) : ').split())
        print('-'*28)
        print('         {0:4d}년 {1:2d}월'.format(year, month))
        print('-'*28)
        print(' 일  월  화  수  목  금  토 ')
        print('-'*28)

        for i in range(weekDay(year, month, 1)):
            print('    ', end='')

        for i in range(1, lastDay(year, month)+1):
            print(' {0:2d} '.format(i), end='')

            if weekDay(year, month, i) == 6 and i != lastDay(year, month):
                print()

        print('\n'+'-'*28)
        print('\n')

    if n==2:
        curs.execute('create table if not exists Calendar (date, value) ')

        date=input('날짜를 입력하세요 : ')
        value=input('일정을 입력하세요 : ')
        schedule=[date, value]

        curs.execute('insert into Calendar values(?, ?)', schedule)

        conn.commit()
        conn.close

    if n==3:
        search=input('일정을 확인하고 싶은 날짜를 입력해주세요(ex.2000 01 01) : ')
        sql="select * from Calendar where date='{}'". format(search)
        rows=curs.fetchall()
        for row in rows:
            print(row)

    if n==4:
        search=input('일정을 확인하고 싶은 날짜를 입력해주세요(ex.2000 01 01) : ')
        sql1="select * from Calendar where date='{}'". format(search)
        rows=curs.fetchall()
        for row in rows:
            print(row)
        
        delete=input('삭제하고 싶은 일정의 내용을 입력해주세요 : ')
        sql2="delete from Calendar where value= '{}'". format(delete)
        curs.execute(sql2)

        conn.commit()
        conn.close






