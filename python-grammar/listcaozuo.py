#encoding:utf-8
'''列表解析，利用for循环列出1-20的数字'''
# list1=[value for value in range(1,1000001)]
# print(list1)
#
# lisy2=[a**2 for a in range(2,11)]
# print(lisy2)
# '''列表内的简单计算，sum，min，max'''
# list1=[a for a in range(1,1000001)]
# print(sum(list1))
# print(max(list1))
# print(min(list1))
# '''列表的修改'''
# phone=['apple','xiaomi','redmi','huiwei','rongyao','oneplus','oppo','vivo']
# phone[0]='fix'
# print(phone)
#
# '''列表元素的增加'''
# phone1=[]
# phone1.append('a')
# phone1.append('b')
# print(phone1)
#
# '''列表元素的删除'''
# phone=['apple', 'xiaomi', 'redmi', 'huiwei', 'rongyao', 'oneplus', 'oppo', 'vivo']
# del phone[0]
# print(phone)

# '''pop 删除列表最后一个元素'''
# phone=['apple', 'xiaomi', 'redmi', 'huiwei', 'rongyao', 'oneplus', 'oppo', 'vivo']
# last_buy=phone.pop()
# print("the last phone i bought was "+last_buy.title())
# print(phone)
# '''remove根据列表的值出现'''
# phone.remove('xiaomi')
# print(phone)
# '''列表排序'''
# '''sort对列表进行永久排序按字母:规则：数字>大写字母>小写字母'''
# phone=['apple', 'xiaomi', 'redmi', 'huiwei', 'rongyao', 'oneplus', 'oppo', 'vivo']
# phone.sort()
# print(phone)
# '''反转排序'''
# phone.sort(reverse=True)
# print(phone)
#
# number=['2', '1 ', '3', '4']
# number.sort()
# print(number)
# number.sort(reverse=True)
# print(number)
#
# phonenumber=['apple', 'A','B','xiaomi', 'redmi', 'huiwei', 'rongyao', 'oneplus', 'oppo', 'vivo','2', '1 ', '3', '4']
# phonenumber.sort()
# print(phonenumber)

# '''sorted临时排序'''
# car=['奔驰', '宝马', '吉利', '马自达', '丰田', '奥迪']
# print("开始的排序是这样的：")
# print(car)
#
# print("\n临时排序后的列表是这样的：")
# print(sorted(car, reverse=True))
# print("\n在来看看原始的排序吧：")
# print(car)

# '''列表顺序反转reverse,第一个变为最后一个'''
# car=['奔驰', '宝马', '吉利', '马自达', '丰田', '奥迪']
# car.reverse()
# car.reverse()
# print(car)
# '''sort是对排序后在反转'''
# car.sort(reverse=True)
# print(car)
#
# len(car)
# print(len(car))

# '''练习'''
# target_goal = ['大理', '丽江', '上饶', '南京', '石家庄']
# print(target_goal)
# print(sorted(target_goal))
# print(target_goal)
# print(sorted(target_goal,reverse=True))
# print(target_goal)
# target_goal.reverse()
# print("首次反转列表的顺序：")
# print(target_goal)
# target_goal.reverse()
# print("\n又反转回来查看和原来的顺序一致吗：")
# print(target_goal)
# target_goal.sort()
# print(target_goal)
# target_goal.sort(reverse=True)
# print(target_goal)
'''切片'''
number = ['1', '2', '3 ', '4', '5', '6', '7', '8', '9']
print(number[-3:])
