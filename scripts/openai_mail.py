import random
import string
 
# 生成随机密码的字符串，字符串中只包括字母和数字
# 可以指定字符串的位数
 
# 定义函数
mail = "@kudaohang.com"
account = "账号："
password = "密码："
letter = "openai"
 
 
def gen_random_mail(length):
 
    # 随机生成字母和数字的位数
    numcount = length
    # lettercount = length - numcount
 
    # 随机抽样生成数字序列
    numlist = [random.choice(string.digits) for _ in range(numcount)]
 
    # 随机抽样生成字母序列
    # letterlist = [random.choice(string.ascii_letters) for _ in range(lettercount)]
 
    # 合并字母数字序列
    alllist = numlist
 
    # 生成目标结果字符串
    result = "".join([i for i in alllist])
 
    return result
 
def gen_random_pw(length):
 
    punctuation = "!@#$%^&*()_+-="
    length = length - 7
    # 随机生成字母和数字的位数
    # numcount = random.randint(2, length - 6)
    # lettercount = random.randint(3, length - numcount -2)
    # punctuationCount = random.randint(2, length - numcount - lettercount)
 
    # 随机抽样生成数字序列
    numlist = [random.choice(string.digits) for _ in range(2)]
 
    # 随机抽样生成字母序列
    letterlist = [random.choice(string.ascii_letters) for _ in range(3)]

    punctuationlist = [random.choice(punctuation) for _ in range(2)]

    remain = [random.choice(string.digits + punctuation + string.ascii_letters) for _ in range(length)]
 
    # 合并字母数字序列
    alllist = numlist + punctuationlist + letterlist + remain
 
    # 生成目标结果字符串
    result = "".join([i for i in alllist])
 
    return result
 
# 循环生成账号密码（10是数量）
num = 0
while num < 100:
    randMail = gen_random_mail(8)
    randPw = gen_random_pw(12)
    print(account + letter + randMail + mail +"   " + password + randPw)
    num += 1