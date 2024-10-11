from datetime import datetime
#1.输入一个整数，判断该整数是否能被 3 或 7 整除，若能被 3 或 7 整除，则输出“Yes”，否则输出“No”
def modd(num):
	if num%3==0 or num%7==0 :
		return "Yes"
	else :
		return "No"
#2.输入一个整数，若为奇数则输出其平方根，否则输出其立方根。要求分别用 单分支，双分支以及条件运算实现
def oddoreven(num):
	if num%2==0:
		return num**(1/3)
	else :
		return num**(1/2)
#3.输出整数 x,y,z，若𝑥2 + 𝑦2 + 𝑧2大于 1000，则输出𝑥2 + 𝑦2 + 𝑧2千位以上的 数字，否则输出三个数之和
def threeplus(x,y,z):
	sum=x*x+y*y+z*z
	if(sum>1000):
		return sum/1000
	else:
		return x+y+z 
#4.输入三个数，判断它们能否组成三角形。
def threenumber(x,y,z):
	minnum=min(x,y,z)
	second=0
	third=0
	if minnum==x :
		second=min(y,z)
		third=max(y,z)
	elif minnum==y :
		second=min(x,z)
		third=max(x,z)
	else :
		second=min(x,y)
		third=max(x,y)
	if minnum+second>third:
		if minnum==second:
			if minnum==third:
				return "等边三角形"
			else :
				return "等腰三角形"
		elif minnum**(2)+second**(2)==third**(2):
			return "直角三角形"
		else :
			return "普通三角形"
	else :
		return "不能组成三角形"
#若能，则输出三角形是等腰三角形， 等边三角形，直角三角形，还是普通三角形；
#若不能，则输出“不能组成三角形” 提示信息
#5.输入一个人的出生日期和当前的日期（年、月、日），输出其实足年龄
def age(birth_year,birth_month,birth_day,current_year,current_month,current_day):
	age=current_year-birth_year
	if (current_month,current_day)<(birth_month,birth_day) :
		age-=1
	return age
#6.8.某运输公司在计算运费时，按运输距离（s）对运费打一定的折扣（d）,其标准如下：
#输入基本运费 p，货物重量 w，距离 s，计算总运费 f。总运费的计算公式f = p × w × s × (1 − d)，
#其中 d 为折扣，由距离 s 根据上述标准求得。
#0-250，没折扣；
#250-500,折扣2.5%，
#500-1000，折扣4.5%；
#1000-2000，折扣7.5%；
#2000-2500，折扣9%；
#2500-3000,12%，
#3000以上15%
def price(p,w,s):
	d=0
	if s<0 :
		return false
	elif s>=0 and s<250 :
		d=0
	elif s>=250 and s<500 :
		d=0.025
	elif s>=500 and s<1000 :
		d=0.045
	elif s>=1000 and s<2000 :
		d=0.075
	elif s>=2000 and s<2500 :
		d=0.09
	elif s>=2500 and s<3000 :
		d=0.12
	else :
		d=0.15
	return p*w*s*(1-d)
#测试部分
testnum=9
print("the first question is "+modd(testnum))
print(f"the second question is {oddoreven(testnum)}")
x=10
y=10
z=10
print(f"the third question is {threeplus(x,y,z)}")
print(f"the forth question is {threenumber(x,y,z)}")
birth_year=1999
birth_month=10
birth_day=25
current_year=2024
current_month=9
current_day=13
print(f"the fifth question is {age(birth_year,birth_month,birth_day,current_year,current_month,current_day)}")
p=500
w=3000
s=2000
print(f"the sixth question is {price(p,w,s)}")