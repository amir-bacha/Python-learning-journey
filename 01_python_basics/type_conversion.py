a=10
b=5
division=a/b
print(division, type(division))  # implicitly the ans is converted into float

c=10
d=20
sum=c+d
print(sum)
print(type(sum))
state=True
booleanSum=a + state
print(booleanSum,type(booleanSum)) # it will be eleven bc True is considered 1

#Explicit type conversio  / Type casting
a=123
string=str(a)
print(string,type(string))
number='1234'
print(number,type(number))
intNumber=int(number)
print(intNumber,type(intNumber))

statement=True
intStatement=int(statement)
print(intStatement,type(intStatement)) # True is equal to 1
# if we want to obtain int result while dividing the two nums
a=100
b=50 
division=int(a/b)
print(division,type(division))

# Practice with input and type casting
a=input('Enter value of a : ')
b=input('Enter value of b : ')
sum=a+b   #  if a=10 and b=20 the sum will be 1020 because input is considered str and it will concatenate both values
print(sum,type(sum)) # str data type
# to convert to int 
a= int (input('Enter value of a : '))
b= int(input('Enter value of b : '))
sum=a+b
print(sum,type(sum)) 


