# # Function : A reusable block of code that performs specific task
# def hello():
#     print('Hello world')
# hello()

# def addition(a, b):
#     return a+b
# result=addition(200,100)
# print(result)

# # with default arguments
# def mul(a,b=5):
#     return a*b

# print(mul(3,5)) 
# print(mul(4)) # 20 
# def sum(*nums):
#     print(nums[3])
# sum(1,2,3,4)

# def avarage_function(*nums):
#     total=0
#     lenth=0
#     for i in nums:
#         total+=i
#         lenth+=1
#     return total/lenth
# result=avarage_function(1,2,3)
# print(result)


def sum(*tuple):
    sum=0
    for i in tuple:
        sum+=i
    return sum

print(sum(2,3,4,5))



def factorial(n):
    if(n==1):
        return 1
    return n*factorial(n-1)

fact=factorial(6)
print(fact)