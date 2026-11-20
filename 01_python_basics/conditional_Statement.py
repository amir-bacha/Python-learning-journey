# Conditional statement : Statement is excuted when certein condition becomes true
 # if statement
age=int(input("Enter value of age : "))
if (age>=18):
    print('You can vote')
score=int(input('Enter the batsman score : '))
if (score>=100):
    print('Century is completed')

# if else statement : excute the statements when base condition becomes true other wise excute the others
day=input('Enter day : ')
if (day=='sunday'):
    print('Today is off')
else :
    print('institute will remain opened')
   # to check whether the number is negative or positive
number=int(input('Enter number to check whether it is positive or negative : '))
if (number>0):
    print('the number is positive')
else :
    print('The number is zero or negative ')

# elif : to check multiple condition
# Checking age
age=int(input('Enter value of age : '))

if (age>0 and age<=13):
    print('Child')
elif (age>13 and age<=18):
    print('Teenager')
elif (age>=18):
    print('Adult')
else :
    print('Negative is not allowed! ')

# to check whether the number is multiple of 5 or not
num=int(input('Check the multiple of 5 : '))

if (num % 5==0):
    print(num,' is multiple of 5 ')
else :
    print('The number is not multiple of 5 ')

# To log an admin
username=input('Enter username : ')
password=int(input('Enter password : '))

if (username=='admin' and password==123):
    print('LOGIN Successfull! ')
elif(username!='admin'):
    print('Wrong username')
else : 
    print('Wrong password')