#练习1
a=eval("1")
print(a)
#练习2
a=eval('print("Hello")')
#练习3
t=("1+2+3+4")
a=eval(t)
print(a)
#练习4
print(pow(10,2))
#练习5
a=pow(10,2)
print(a)
#练习6
a=pow(10,pow(3,2))
print(a)
#练习7
a=round(4.222,0)
print(a)
#练习8
a=round(0.3,0)
print(a)
#练习9
a=abs(-10)
print(a)
#练习10
a=divmod(10,3)
print(a)
#练习11
a=max(1,2,3,4,5,6,7,8,9,0,)
print(a)
b=min(1,2,3,4,5,6,7,8,9,0)
print(b)
#练习12
a=int(18.123)
print(a)
#练习13
a=float(18)
print(a)
#练习14
a=complex(18)
print(a)
#练习15
a="1,2,3,4,5,6,7,8,9"[0:-1:2]
print(a)
#练习16
a="1,2,3,4,5,6,7,8,9"[::-2]
print(a)
#练习17
print(len("abcdcfghijk"))
#练习18
a=len("123456789")
print(a)
#练习19
a="1+1=2"+chr(10004)
print(a)
b="1+1=3"+chr(10005)
print(b)
#练习20
a=chr(9801)
print(a)
#练习21
b=str(ord("♉"))
print(b)
#练习22
a="bcDFGHjkL".lower()
print(a)
#练习23
b="L,I,B,O,X,I,A,N,G".split(',')
print(b)
#练习24
c="liboxiang iiiiiiiiii".count("i")
print(c)
#练习25
d="LIBOXIANG".replace("G","G-love")
print(d)
#练习26
a="LIBOXIANG".center(20,"=")
print(a)
#练习27
b="LIBOXIANG".strip("LGINA")
print(b)
#练习28
c=",".join("LIBOXIANG")
print(c)
#练习29
a="{}:计算机{}的CPU使用率{}%".format("2019-9-13","LI","10")
print(a)
#练习30
a="{1}:计算机{0}的CPU使用率{2}%".format("2019-9-13","LI","10")
print(a)
#练习31
a="{0:,.2f}".format(1234555.6789)
print(a)
#练习32
a="{0:.2f}".format(1234555.6789)
print(a)
#练习33
a="{0:=^20}".format("LIBOXIANG")
print(a)
#练习34
a="{:10}".format("LBX")
print(a)
#练习35
for i in range(12):
    print(chr(9800+i),end="")
#复习36
import time
a=time.time()
print(a)
a=time.ctime()
print(a)
a=time.gmtime()
print(a)
t=time.gmtime()
a=time.strftime("%Y-%m-%d %H:%M:%S",t)
print(a)
#复习37
#程序计时器实例
import time
start=time.perf_counter()
end=time.perf_counter()
a=end-start
print(a)
#复习38
#停顿计时器实例
import time
def wait():
    time.sleep(10)
a=wait()
print(a)
#复习39
#进度条的实例
import time
scale = 10
print("----执行开始----")
for i in range(scale+1):
    a='*' * i
    b='.' * (scale-i)
    c=(i/scale)*100
print("{:^3.0f}%[{}->{}]".format(c,a,b))
time.sleep(10)
print("-----执行结束-----")
#复习40
#单行进度条的实例
import time
for i in range(101):
    print("\r{:3}".format(i),end="")
    time.sleep(0.1)
#复习41
#文本进度条完整效果实例
import time
scale=50
print("执行开始".center(scale//2,"-"))
start=time.per_counter()
for i in range(scale+1):
    a='*' * i
    b='.' * (scale - i)
    c=(i/scale) * 100
    dur=time.perf_counter()-start
    print("\r{:^3.0f}%[{}- > {}]{:.2f}s".format(c,a,b,dur),end="")
    time.sleep(0.1)
    print("\n"+"执行结束".center(scale//2,'-'))
#练习42
guess=eval(input(""))
if guess==99:
    print("猜对了")
#练习43
guess = eval(input())
if guess==99:
    print("猜对了")
else:
    print("猜错了")
#练习44
guess=eval(input())
print("猜{}了".format("对"if guess==99 else"错"))
#练习45
score=eval(input())
if score>=60:
    grade="D"
elif score>=70:
    grade="C"
elif score>=80:
    grade="B"
elif score>=90:
    grade="A"
print("请输入成绩属于级别{}".format(grade))
#练习46
guess=eval(input())
if guess>99 or guess<99:
    print("猜错了")
else:
    print("猜对了")
#练习47
try:
 num =eavl (input("请输入一个整数："))
 print(num**2)
except:
    print("输入不是整数")
#练习48
try:
    num=eval(input("请输入一个整数"))
    print(num**2)
except NameError:
    print("输入不是整数")
#练习49
height,weight = eval(input("请输入身高(米)和体重\(公斤)[逗号隔开]："))
bmi = weight / pow(height,2)
print("BMI数值为:{:.2f}".format(bmi))
who,nat="",""
if bmi<18.5:
    who,nat="偏瘦","偏瘦"
elif 18.5<=bmi<24:
    who,nat="正常","正常"
elif 24<=bmi<25:
    who,nat="正常","偏胖"
elif 25<=bmi<28:
    who,nat="偏胖","偏胖"
elif 28<=bmi<30:
    who,nat="偏胖","肥胖"
print("BMI指标为：国际'{0}',国内'{1}'".format(who,nat))
