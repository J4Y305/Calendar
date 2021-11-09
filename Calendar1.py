from calendarModule import *
n=0
while n != -1:
    print('1. 달력보기')
    print('2. 일정추가')
    print('3. 일정확인')
    print('4. 일정삭제')

    n = int(input( 'Choose the option please. (EXIT=-1): '))

    if n==1:
        year, month =map(int, input('type the year and month please. : ').split())
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

