# -*- coding: utf-8 -*-
name = 'fanbo'
height = 180
N, H = name, height # 元组tuple赋值
[N1, H1] = [name, height] # 列表赋值
# 混用也是可以的，只要保证左右数目相同，例如
[A, B, C] = (1, 2, 3)
[a, b, c] = 'SHE'
red, blue, green = range(3) # 整数赋给元组


L = [1, 2, 3]
L += [5, 6] # +=合并自动调用的是速度较快的extend方法，而不是真正的L = L + [5, 6]

print 'hehe', 'fanbo', # print最后加一个','号，是说不要换行
print 'ku'
# 逗号隔开是默认加空格的，而不要空格，必须用字符串连接或者格式化输出
print 'hehe' + 'fanbo'
print '%s ... %s' % ('hehe', 'fanbo')

# stdout重定向
log = open('log.txt', 'w')
print >> log, 1, 2, 3
print >> log, 4, 5, 6,
log.close()
print open('log.txt', 'r').read()
