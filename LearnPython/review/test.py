
# 多行语句
def multiline_statement():
    # Python语句中一般以新行作为语句的结束符。
    # 但是我们可以使用斜杠（ \）将一行的语句分为多行显示，如下所示：
    item_one = 1
    item_two = 2
    item_three = 3

    total = item_one + \
            item_two + \
            item_three

    print(total)
    # 语句中包含 [], {} 或 () 括号就不需要使用多行连接符

# 不换行输出
def print1():
    x = "a"
    y = "b"
    # 换行输出
    print(x)
    print(y)

    print('---------')

    # 不换行输出
    print(x, y)

# print1()

# 数据类型
def data_type():
    # Python有五个标准的数据类型：

    # 1、Numbers（数字）
    # Python支持四种不同的数字类型：
    # int（有符号整型）`
    # long（长整型，也可以代表八进制和十六进制）（py3中已被移除
    # float（浮点型）
    # complex（复数）

    # 2、String（字符串）
    # 从左到右索引默认0开始的，最大范围是字符串长度少1
    # 从右到左索引默认-1开始的，最大范围是字符串开头

    # 如果你要实现从字符串中获取一段子字符串的话，可以使用[头下标:尾下标]
    # 来截取相应的字符串，其中下标是从0开始算起，可以是正数或负数，下标可以为空表示取到头或尾。
    # [头下标: 尾下标] 获取的子字符串包含头下标的字符，但不包含尾下标的字符。
    s = 'abcdefg'
    print(s[4])  # e
    print(s[1:3])  # bc
    print(s)  # abcdefg
    print(s[:])
    print(s[:4])  # abcd
    print(s[2:])  # cdefg
    # 加号（+）是字符串连接运算符，星号（*）是重复操作。
    print(s * 2)  # abcdefgabcdefg
    print(s + "hijk")  # abcdefghijk
    # Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 0 到索引 5 的位置并设置为步长为 2（间隔一个位置）来截取字符串：
    print(s[0:5:2])  # ace

    # 3、List（列表）
    # 它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
    list = ['runoob', 786, 2.23, 'john', 70.2]
    tinylist = [123, 'john']

    print(list)               # 输出完整列表
    print(list[0])            # 输出列表的第一个元素
    print(list[1:3])          # 输出第二个至第三个元素
    print(list[2:])           # 输出从第三个开始至列表末尾的所有元素
    print(tinylist * 2)       # 输出列表两次
    print(list + tinylist)    # 打印组合的列表

    # ['runoob', 786, 2.23, 'john', 70.2]
    # runoob
    # [786, 2.23]
    # [2.23, 'john', 70.2]
    # [123, 'john', 123, 'john']
    # ['runoob', 786, 2.23, 'john', 70.2, 123, 'john']

    # 4、Tuple（元组）
    # 元组是另一个数据类型，类似于List（列表）。
    # 元组用()标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表,不允许更新。

    # 5、Dictionary（字典）
    # 字典当中的元素是通过键来存取的，而不是通过偏移存取。
    # 字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
    dict = {}
    dict['one'] = "This is one"
    dict[2] = "This is two"

    tinydict = {'name': 'runoob', 'code': 6734, 'dept': 'sales'}

    print(dict['one'])       # 输出键为'one' 的值
    print(dict[2])              # 输出键为 2 的值
    print(tinydict)             # 输出完整的字典
    print(tinydict.keys())      # 输出所有键
    print(tinydict.values())    # 输出所有值

# data_type()

# 运算符
def operator():
    # 1、算术运算符
    # 幂运算： **
    print(10**2)  # 100
    # 除以并向下取整 //
    print(9//2)  # 4

    # 2、比较（关系）运算符
    # == != > < >= <=

    # 3、赋值运算符
    # = += -= *= %= **= //=

    # 4、逻辑运算符
    # and or not

    # 5、位运算符 将整数看做二进制数进行运算

    a = 60            # 60 = 0011 1100
    b = 13            # 13 = 0000 1101

    print("a & b的值为：", a & b)  # 12 = 0000 1100
    print("a | b的值为：", a | b)  # 61 = 0011 1101
    print("a ^ b的值为：", a ^ b)  # 49 = 0011 0001
    print("~a 的值为：", ~a)  # -61 = 1100 0011
    print("a << 2的值为：", a << 2)  # 240 = 1111 0000 左移两位等于×4
    print("a >> 2的值为：", a >> 2)  # 15 = 0000 1111 右移两位等于÷4

    # 6、成员运算符
    # in / not in 字符串、列表、元祖

    # 7、身份运算符
    # is / not is
    # is 用于判断两个变量引用对象是否为同一个(同一块内存空间)
    # == 用于判断引用变量的值是否相等。
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a[:]
    # print(a == b)
    print(a is c)

    # 8、运算符优先级

# operator()

# 条件语句 continue break pass
def condition():
    a = 1
    if a == 1:
        print(a)
    elif a != 1:
        print(a+1)

# for循环语句
def for_loop():
    # 逐个打印字符串中的元素
    for letter in "liuhaiqi":
        print(letter)

    # 逐个打印列表中的元素
    for fruit in ['apple', 'pear', 'bananas']:
        print(fruit)
    # 通过序列索引迭代
    fruits = ['banana', 'apple', 'mango']
    for index in range(len(fruits)):
        # print('当前水果：'+fruits[index])
        print('当前水果 : %s' % fruits[index])
    # for还可以和else搭配使用

# for_loop()

# while循环
def while_loop():
    # 可以搭配else使用
    count = 0
    while count < 5:
        print(count, " is  less than 5")
        count = count + 1
    else:
        print(count, " is not less than 5")

# while_loop()

# import math  # math 模块提供了许多对浮点数的数学运算函数
# import cmath  # cmath 模块包含了一些用于复数运算的函数。

def math_use():
    x = 8.1111
    y = 20
    # abs(x)  # 返回数字的绝对值，如abs(-10) 返回 10
    # math.ceil(x)	 # 返回数字的上入整数，如math.ceil(4.1) 返回 5
    # math.floor(x)  # 返回数字的下舍整数，如math.floor(4.9)返回 4
    # math.cmp(x, y)  # 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
    # math.exp(x)  # 返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
    # math.fabs(x)	 # 返回数字的绝对值，如math.fabs(-10) 返回10.0
    # math.log(x)  # 如math.log(math.e)返回1.0,math.log(100,10)返回2.0
    # math.log10(x)  # 返回以10为基数的x的对数，如math.log10(100)返回 2.0
    # max(x1, x2,...)  # 返回给定参数的最大值，参数可以为序列。
    # min(x1, x2,...)	 # 返回给定参数的最小值，参数可以为序列。
    # print(math.modf(x))  # 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
    # pow(x, y)  # x**y 运算后的值。
    # print(round(x, 2))  # 返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
    # math.sqrt(x)  # 返回数字x的平方根

# math_use()

import random
def function_random():
    seq = '123456789'
    # print(random.choice(seq))  # 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
    # start = 1; stop = 100; step = 5
    # start -- 指定范围内的开始值，包含在范围内。
    # stop -- 指定范围内的结束值，不包含在范围内。
    # step -- 指定递增基数。
    # print(random.randrange(([start,] stop [,step]))	 # 从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
    # random()  # 随机生成下一个实数，它在[0,1)范围内。
    # random.seed([1])  # 改变随机数生成器的种子seed。先调用它的情况下，使用 random() 生成的随机数将会是同一个。
    # l = [1, 2, 3, 4]
    # random.shuffle(l)  # 将序列的所有元素随机排序
    # print(l)
    # random.uniform(1, 5)  # 随机生成下一个实数，它在[x,y]范围内。

# function_random()

import string
# 字符串
def string1():
    # 字符串格式化
    print("My name is %s and weight is %d kg!" % ('lhq', 21))
    # 字符串格式化函数format
    print("{1} {0} {1}".format("hello", "world"))

    # 三引号
    s = '''lhq
wyx'''
    # print(s)
    # python的字符串内建函数
    x = 'lhq'
    # print(x.capitalize())  # 把字符串的第一个字符大写
    # print(x.center(2))  # 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
    # string.count(str, beg=0, end=len(string))  # 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
    # string.decode(encoding='UTF-8', errors='strict')  #  以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除非 errors 指 定 的 是 'ignore' 或 者'replace'
    # string.encode(encoding='UTF-8', errors='strict')  #  以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
    # string.endswith(obj, beg=0, end=len(string))  # 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
    # string.expandtabs(tabsize=8)  # 把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8。
    # string.find(str, beg=0, end=len(string))  # 检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
    # string.format()  # 格式化字符串
    # string.index(str, beg=0, end=len(string))  # 跟find()方法一样，只不过如果str不在 string中会报一个异常.
    # string.isalnum()  # 如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
    # string.isalpha()  # 如果 string 至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
    # string.isdecimal()  # 如果 string 只包含十进制数字则返回 True 否则返回 False.
    # string.isdigit()  # 如果 string 只包含数字则返回 True 否则返回 False.
    # string.islower()  # 如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
    # string.isnumeric()  # 如果 string 中只包含数字字符，则返回 True，否则返回 False
    # string.isspace()  # 如果 string 中只包含空格，则返回 True，否则返回 False.
    # string.istitle()  # 如果 string 是标题化的(见 title())则返回 True，否则返回 False
    # string.isupper()  # 如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
    # string.join(seq)  # 以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
    # string.ljust(width)  # 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
    # string.lower()  # 转换 string 中所有大写字符为小写.
    # string.lstrip() # 截掉 string 左边的空格
    # string.maketrans(intab, outtab)
    # maketrans()  # 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
    # max(str) # 返回字符串 str 中最大的字母。
    # min(str)  # 返回字符串 str 中最小的字母。
    # string.partition(str) # 有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string.
    # string.replace(str1, str2,  num=string.count(str1)) # 把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.
    # string.rfind(str, beg=0,end=len(string) )  # 类似于 find() 函数，返回字符串最后一次出现的位置，如果没有匹配项则返回 -1。
    # string.rindex( str, beg=0,end=len(string))  # 类似于 index()，不过是返回最后一个匹配到的子字符串的索引号。
    # string.rjust(width)  # 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
    # string.rpartition(str)  # 类似于 partition()函数,不过是从右边开始查找
    # string.rstrip()  # 删除 string 字符串末尾的空格.
    # string.split(str="", num=string.count(str))  # 以 str 为分隔符切片 string，如果 num 有指定值，则仅分隔 num+1 个子字符串
    # string.splitlines([keepends])  # 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
    # string.startswith(obj, beg=0,end=len(string))   # 检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.
    # string.strip([obj])  # 在 string 上执行 lstrip()和 rstrip()
    # string.swapcase()  # 翻转 string 中的大小写
    # string.title()  # 返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
    # string.translate(str, del="")  # 根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 del 参数中
    # string.upper()  # 转换 string 中的小写字母为大写
    # string.zfill(width)  # 返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0

# string1()

# 列表
def list1():
    # 更新列表
    l = []
    l.append('lhq')
    l.append('wyx')
    print(l)
    # 删除列表元素
    del l[1]
    print(l)
    print(l.count('lhq'))  # 统计某个元素在列表中出现的次数
    l.insert(2, 'love')  # 将对象插入列表
    print(l)
    l.reverse()  # 逆置
    l.sort()  # 排序

# list1()

# 元组
def tup():
    # 元组不可修改但是可以连接
    # 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
    pass

# 字典
def dictionary():
    # key一般是唯一的，如果重复最后的一个key-value会替换前面的，value不需要唯一。
    tinydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    del tinydict['Name']  # 删除键是'Name'的条目
    tinydict.clear()  # 清空字典所有条目
    del tinydict  # 删除字典
    # 键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行

# 日期和时间
import time
import calendar
def time_and_date():
    print(time.localtime(time.time()))  # 返回信息为元组
    # 格式化时间
    print(time.asctime(time.localtime(time.time())))
    # 格式化日期
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    # 获取某月日历
    print(calendar.month(2022, 3))

# time_and_date()

# 函数参数中 加了星号（*）的变量名会存放所有未命名的变量参数
def printinfo(*vartuple):
    "打印任何传入的参数"
    # print("输出:"+arg)
    for var in vartuple:
        print(var)

# 调用printinfo 函数
# printinfo(10)
# printinfo(70, 60, 50)


# 文件I/O
def fileIO():
    # str = input("请输入：")
    # print("你输入的内容是: ", str)

    # 文件读写
    fp = open(file="lhq.txt", mode="w", encoding="utf-8")
    print(fp.name+' '+fp.mode)
    fp.write("lhq")
    fp.close()
    fp = open("lhq.txt", mode="r")
    print(fp.read())
    fp.close()

    # 文件定位 fp.tell()
    # import os
    # 重命名文件 os.rename(current_file_name, new_file_name)
    # 删除文件 os.remove(file_name)

    # 创建目录test os.mkdir("test")
    # 更改工作目录 os.chdir("test")

    # os.getcwd()方法显示当前的工作目录
    # os.rmdir() 方法删除目录，目录名称以参数传递。

# fileIO()

# 异常处理
def exception():
    pass
    # try....except...else
    # try:
    #     fh = open("testfile", "w")
    #     fh.write("这是一个测试文件，用于测试异常!!")
    # except IOError:
    #     print("Error: 没有找到文件或读取文件失败")
    # else:
    #     print("内容写入文件成功")
    #     fh.close()

    # try-finally 语句 无论是否发生异常都将执行最后的代码。
    # try:
    #     < 语句 >
    # finally:
    #     < 语句 >  # 退出try时总会执行
    # raise

    # 用raise触发异常
    # def functionName(level):
    #     if level < 1:
    #         raise Exception("Invalid level!", level)
    # 触发异常后，后面的代码就不会再执行

