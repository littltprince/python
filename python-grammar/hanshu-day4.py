#C:\Users\勺子课堂\PycharmProjects\debin\python-grammar\hanshu-day4.py
#encoding:utf-8
# def my_abs(c):
#     if c <0:
#         return -c
#     return c
# # print(my_abs(-11.88))
# '''计算ax2+bx+c=0的方程解'''
# import math
# def quadratic(a,b,c):
#     data=b*b-4*a*c
#
#     if data <0:
#         return ("此方程无实根哦")
#     else:
#         if a==0:
#             return c / b
#         x1 = (-b + math.sqrt(data)) / 2 * a
#         x2 = (-b - math.sqrt(data)) / 2 * a
#         return  (x1,x2)
# print(quadratic(7,5,1))
# '''定义幂次方的函数，幂的参数参数默认值2'''
# import math
# def power(x,n=2):
#     s=1
#     while n >0:
#         n=n-1
#         s=s*x
#     return s
# print(power(2))
# '''默认参数'''
# def login(name,gender,city='上海'):
#     print('name',name)
#     print('gender',gender)
#     print('city',city)
# login('a','a')
# '''参数可变的函数，例如计算a**2+b**2+C**2+...'''
# def value(*numbers):
#     sum=0
#     for n in numbers:
#         sum=sum+n*n
#     return sum
# # print(value(1,2,3))
# '''自定义的可变参数'''
#
# def person(age,name,**kw):
#     kw = ['city:','beijing','country:','china']
#     print('age:',age,'name:',name,'other:',kw)
# person(12,'fuas')
'''递归函数'''
def fact(m):
    return fact_1(m,1)
def fact_1(num,product):
    if num==1:
        return product
    return fact_1(num-1,num*product)
# print(fact(10))

def facy(n):
    if n==1:
        return 1
    return n*facy(n-1)
print(facy(4))
