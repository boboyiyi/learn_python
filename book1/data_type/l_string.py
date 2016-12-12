# -*- coding: utf-8 -*-
test_str = 'boboyiyi'
# 字符串序列操作
print 'The length of ' + test_str + ' is ' + str(len(test_str)) + '.'
'''
int2str: str(int_value)
字符串长度: len(test_str)
字符串连接: + 号
单行注释: #
多行注释: '''       '''
程序中包含中文定义coding scheme # -*- coding: utf-8 -*-
'''

print test_str[0] + ' ' + test_str[1] + ' ' + test_str[-2] + ' ' +  test_str[-1]
print test_str[-1] + ' = ' + test_str[len(test_str) - 1]
'''
0为第一个字符，-1为最后一个
-2为倒数第二个
-1和长度 -1的字符是一样的
'''

print test_str[0:3] # 0 1 2三个元素
print test_str[1:] # 1 2 ...所有
print test_str[:3] # 0 1 2
print test_str[:-1] # 最后一个字符不输出
print test_str[:] # equal to test_str
print test_str[1:-1:2] # 第三个参数表示每隔两个字符索引一次
print test_str[5:1:-1] # 步长为负数情况
'''
slice 分片
'''

print test_str * 2 # 字符串两次打印

# test_str[0] = 'h' 错误，字符串不可变性
test_str = 'h' + test_str[1:] # 新的赋值，python清除旧对象，创建新对象test_str
print test_str

print dir(test_str) # dir(test_str)可以显示test_str类型特定的方法

print test_str.find('oy')
print test_str.replace('oy','ooyy')
print test_str.upper() # lower
print (test_str.upper()).lower()
print test_str.isalpha() # also isdigit
line = 'aaa,bbb,ccc,dd\n'
print line.split(',')
print line.rstrip() # 去除右侧的空格，换行等
'''
string的一些方法示例
'''

msg = '''wo jiao
fan bo
ni jiao
sha?'''
print msg
# 多行文本示例，也是注释方法的由来

# raw string的用处
file1 = open(r'C:\new\text.data','w')
# 如果不使用r，则\n和\t都会被当成转义字符，也就是说raw string强制关闭转义字符

# 查询字符的ASCII码，反之
print ord('S')
print chr(115)

# 字符串格式化
print 'The test string is %s' % test_str 
print 'My name is %s, I am %d years old.' % ('fanbo', 26)
print '%s --- %s --- %s' % (4, 3.14, ['hehe', 1, 3.14])

tmp = list(test_str) # 将字符串转化为字符的列表‘’
tmp[0] = 'x' # 可以进行修改了
print tmp
print ''.join(tmp) # 将列表合并成字符串

