#encoding:utf-8
uesernames = ['bob', 'admin', 'tom', 'rock', 'alice']
del uesernames[:]
if uesernames == []:
    print("we need some users ~")
for username in uesernames:
    if username == 'admin':
        print("Hello admin , would u like to see a status ?")
    else:
        print("Hello "+username, ", thank u for logging in again !")
