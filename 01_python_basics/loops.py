# two main loop: 1. while loop    2. for loop
# Printing 10 numbers
i=1
while(i<=10): # this is the condition
    print(i, end=" ")
    i+=1  # increment

 # through for loop
for i in range(1,11):
    print(i, end=" ")
students=['Amir bacha','Jawad Ali ','Haroon khan']
marks=[33,44,55]
for index,value in enumerate(students):
    print(index,value)

for name,marks in zip(students,marks):
    print(name,marks)

# Calculating the factorial problem
number=int(input('Enter to find the factorial : '))
factorial=1 # initilize from 1 because when some number is multiplited with 1 the number is returned
for i in range(number,1,-1): # here in range -1 to decrease the number by 1 upto 1
    factorial*=i # every time the factorial is multiplited with i and factorial will be updated
print('The factorial of ',number," is : ",factorial)

# Multiple of a number upto 10
num=int(input('Enter the number to find its multiple : '))
for i in range(1,11):
    mul=i*num
    print(i," * ",num, " = ", mul)



# Nested loop :  loop inside another loop note: for the single time of outer loop, the inner loop will be excuted of its n time

# poblem of star pattern
for i in range(1,6):
    for j in range(i):
        print(" * ", end=" ")
    print()
