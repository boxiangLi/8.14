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
#
