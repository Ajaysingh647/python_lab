#perfect no.
n=int(input('Enter the num,ber:- '))
s=0
for i in range(1,n):
    if(n%i==0):
        s=s+1
    if(s==n):
         print('perfect no.')
    else:
        print('No.  is not perfect')
