num=int(input("enter the no."))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10

