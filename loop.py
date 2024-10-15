#1、输入n的值，求出n的阶乘。
def question1(n) :
	times=1
	for i in range(1,n+1) :
		times*=i
	return times
#2、输入n的值，求1！+2！+3！+…+n！的和。
def question2(n) :
	sum=0
	for i in range(1,n+1) :
		sum += question1(i)
	return sum
#3、输出100以内的所有素数。
def question3(n) :
	for i in range(2,n+1) :
		isPrime = True
		for j in range(2,(int)(i**0.5+1)) :
			if i%j==0 :
				isPrime = False
				break
		if isPrime :
			print(f"{i} is prime")
#4、求和 求s= a + aa + aaa + … + aa…a 的值（最后一个数中 a 的个数为 n ），
#其中 a 是一个1~9的数字，例如： 2 + 22 + 222 + 2222 + 22222 
def question4(a,n) :
	sum=0
	current=0
	for i in range(1,n+1) :
		current=current*10+a
		sum+=current
	return sum
#5、百元买百鸡。假定小鸡每只5角，公鸡每只2元，母鸡每只3元，编程求解购鸡方案 
def question5( ) :
	for i in range(0,101) :
		for j in range(0,101) :
			k = 100-i-j
			if k>=0 and 0.5*i+2*j+3*k==100 :
				print(f"小鸡个数 ：{i},公鸡个数 ：{j},母鸡个数 ：{k}")
#6、我国现有13亿人口，设每年增长0.8%，编写程序，计算多少年后达到26亿？
def question6(begin,target) :
	year = 0
	while begin < target :
		begin *= 1.008
		year += 1
	return year
print(question1(4))
print(question2(4))
question3(100)
print(question4(1,3))
question5()
print(question6(13,26))