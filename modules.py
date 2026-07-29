'''def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def divide(a, b):
    return a%b
def flordivision(a, b):
    return a//b'''
    
from datetime import datetime, date, timedelta
now = datetime.now()
print(now.year, now.month, now.day)
print(now.strftime('%H : %M : %S'))
today= date.today()
print(today)
tomorrow = today + timedelta(days = 3)
print(tomorrow)
diff =datetime(2025,1,1) - datetime.now()
print(diff)