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
def login(name,gender):
    print('name',name)
    print('gender',gender)
login('a','a')