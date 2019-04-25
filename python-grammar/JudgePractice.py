#encoding:utf-8
# '''条件判断'''
# age=input('age:')
# age=int(str)
# if age is not str:
#     print('请输入数字')
# if age>=1:
#     print('you are old',age)
# else:
#     print('young')

height=float(input('请输入身高(m)：'))
weight=float(input('请输入体重(kg)：'))
bmi=weight/(height*height)
if bmi <18.5:
    print( '过轻')
elif bmi >=18.5 and bmi <25:
    print('正常')
elif bmi>=25 and bmi <28:
    print('过重')
elif bmi>=28 and bmi <32:
    print('肥胖')
else:
    print('严重肥胖')
