# -*- coding: utf-8 -*-
# 元组就像一个不可变的列表
test_tuple = (1,2,3,4)
# test_tuple[0] = 2是错误的

# 元组用于传参中的数据不变形约束，感觉像c语言中的const一样

test_tuple = ('fanbo', 185, 'cm', 65, 'kg')
print test_tuple
tmp = list(test_tuple)
print tmp
tmp.sort()
T = tuple(tmp)
print T
T1 = (1,2,3,4)
print [i + 5 for i in T1] # 列表解析
