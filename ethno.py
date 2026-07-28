'''a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
if a>b:
    print("hello")
print("hii")
'''
'''a = int(input("enter a year:"))
if a%400==0:
    print("it is a leap year")
elif a%4==0 & a%100!=0:
    print("it is aleap year")
else:
    print("it is a leap year")'''

'''a=10
if a>0:
    print("positive")
elif a<0:
    print("negative")
else:
    print("zero")'''
    
'''def count_occurence(ar,k):
    count=0
    for i in range(0,len(ar)):
        if ar[i]==k:
            count = count+1
            print(count)
n= int(input())
ar=list(map(int,input().split()))
k=int(input())
count_occurence(ar,k)'''

'''a = int(input("enter a number"))
b = 0
while a>0:
    a//10
    b =+ 1
print(b)'''

'''num = []
for i in range(4):
    num1 = int(input())
    num.append(num1)
num.sort()
print("second largest",num[2])'''

'''username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "123":
    print("Success")
else:
    print("Invalid username or password")'''
    
'''n=int(input())
for i in range(1,n+1):
     for j in range(1,i+1):
        print("*",end="")
     print()'''
     
'''a=int(input())
if a%2==0:
    print("even")'''
    
'''p=int(input("enter a value"))
q=int(input("enter b value"))
r=int(input("enter c value"))
a=75
b=80
c=65
print(a+b+c)'''


'''if a+b+c/3>=40:
    print("result=pass")'''
    

'''def calculate_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + (units - 100) * 7
    else:
        bill = (100 * 5) + (100 * 7) + (units - 200) * 10
    return bill

units = int(input("Enter the number of units consumed: "))
amount = calculate_bill(units)

print(f"Electricity Bill = ₹{amount}")'''

'''a=10000
b=int(input())
if b<a:
    print("your remaining balance:",a-b)
else:
    print("insufficient balance")'''
    
'''a=int(input("enter total sum of values" ))
b=int(input("enter average of values"))
c=int(input("enter grade of sum values" ))
print(a+b+c)
aveg=((a+b+c)/3)
print(aveg)
if aveg>=90:
    print("grade a")
elif aveg>=75:
    print("grade b")
elif aveg>=60:
    print("grade c")
else:
    print("fail")'''
    
'''a=10000
b=int(input())
if b<a:
    print("your remaining balance:",a-b)
else:
    print("insufficient balance")'''
    
'''a=int(input())
count=0
even=0
odd=0
while a>0:
    digit = a%10
    if a%2==0:
        even+=1
    else:
        odd+=1
    count+=1
    a=a//10
print("total",count)
print("even",even)
print("odd",odd)'''

'''quantity=int(input())
price=3000
total=quantity*price
print("product name:laptop")
print("quantity",quantity)
print(price)
print("total",total)
if total>5000:
    discount=(total*10)/100
else:
    print("no discount")
print("final amount",total-discount)'''


'''balance=10000
while True:
    print("____bank menu___")
    print("1.bank balance")
    print("2.deposite")
    print("3.withdraw")
    print("4.exit")
    choose_1=int(input("enter your checking number"))
    if choose_1==1:
        print("your balance is:",balance)
    elif choose_1==2:
        deposite=int(input("enter amount"))
        amount=deposite+balance
        print("your balance after deposite:",amount)
    elif choose_1==3:
        withdraw=int(input())
        if withdraw<balance:
            balance-amount'''
            
            
            
            
'''a=(1,2,3);b=a
print(a is b)
print(a is not b)'''

fruits=['apple','mango']
print('mango'in fruits)
print('grape'not in fruits)
        
    
    
    