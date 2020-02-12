import random
n=0
b=0
d=0
while True:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if  username=='123' and password=='123':
        print("请输入下面四位数的验证吗")
        for i in range(10):
            d+=1
            a=random.randrange(1000,10000)
            print(a)
            b=input()
            c=int(b)
            if a==c:
                print("登录成功")
                exit()
            elif d<3:
                print("验证码错误")
            else:
                print("验证码输入三次错误，请重新登录")
                break
    else:
        print("输入密码错误或请注意大小写")
        if n==0:
            print("今天还剩三次机会")
            n+=1
            continue
        elif n==1:
            print("今天还剩两次机会")
            n+=1
            continue
        elif n==2:
            print("今天还剩一次机会")
            n+=1
            continue
        elif n==3:
            print("今天输入密码已上限")
            break
