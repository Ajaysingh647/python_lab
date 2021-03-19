n=int(input('Enter the year'))
if(n%4)==0:
    if(n%100)!=0:
        print('Year is a leap year',n)
else:
    print('year is not leap year',n)
