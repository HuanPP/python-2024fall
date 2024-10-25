#1. 一张纸的厚度大约是0.08mm，对折多少次之后能达到珠穆朗玛峰的高度（8848.13米）？
def question1() :
	thick=0.08*10**(-3)
	sum=thick
	count=0
	while sum<8848.13 :
		sum=2*sum
		count+=1
	return count
#2. 某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
#每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
#求输入的四位整数加密后的值
def question2(x):
	four=x//1000
	three=(x//100)%10
	two=(x//10)%100
	one=x%10
	four=(four+5)%10
	three=(three+5)%10
	two=(two+5)%10
	one=(one+5)%10
	num=four+one*1000+two*100+three*10
	return num
#3. 求整数1~100的累加值，但要求跳过所有数位包含3的数（例如，3,13,311）
def question3():
	sum=0
	for i in range(1,1000):
		if '3' in str(i):
			continue
		sum+=i
	return sum
#4. 输入一个整数，将整数分解为质因数的积
#例如输入90，输出 2*3*3*5 = 90
def question4(x):
    factors = []
    divisor = 2
    while x > 1:
        while x % divisor == 0:
            factors.append(divisor)
            x //= divisor
        divisor += 1
    return factors

# 处理输入和格式化输出
def format_factors(factors):
    result = '*'.join(map(str, factors))
    return f"{result} = {eval(result)}"

def question5(x):
    units = ['', '拾', '佰', '仟', '万', '拾', '佰', '仟', '亿']  # 单位
    digits = '零壹贰叁肆伍陆柒捌玖'  # 数字
    result = ''
    num_str = str(x)  # 将数字转换成字符串

    # 处理小数点后部分（角和分）
    if '.' in num_str:
        integer_part, decimal_part = num_str.split('.')
    else:
        integer_part, decimal_part = num_str, ''

    # 处理整数部分
    integer_part = integer_part[::-1]  # 翻转字符串，便于处理单位
    zero_flag = False  # 用于连续零的标记
    for i, num in enumerate(integer_part):
        digit = int(num)
        if digit == 0:
            if not zero_flag:
                result = '零' + result
                zero_flag = True
        else:
            result = digits[digit] + units[i] + result
            zero_flag = False
    result = result.rstrip('零')  # 去掉结尾的零

    # 处理小数部分（角和分）
    if decimal_part:
        jiao = int(decimal_part[0]) if len(decimal_part) > 0 else 0
        fen = int(decimal_part[1]) if len(decimal_part) > 1 else 0

        if jiao == 0 and fen != 0:
            result += '元零' + digits[fen] + '分'
        elif jiao != 0 and fen == 0:
            result += '元' + digits[jiao] + '角'
        elif jiao != 0 and fen != 0:
            result += '元' + digits[jiao] + '角' + digits[fen] + '分'
        else:
            result += '元整'
    else:
        result += '元整'

    # 特殊情况去除多余的“零”
    result = result.replace('零万', '万')
    result = result.replace('零元', '元')
    result = result.replace('零零', '零')
    return '人民币' + result
x = 8
factors = question4(x)
print(f"对折的次数是{question1()}")
print(f"密码是{question2(3333)}")
print(f"总和是{question3()}")
print(f"{x} 的质因数分解为: {format_factors(factors)}")
print(question5(9887.98))