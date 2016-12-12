# -*- coding: utf-8 -*-
'''
列表支持所有类似string的序列操作
'''
test_list = [180, 'fanbo', 1.80]
print len(test_list)
print test_list[0] # 索引
print test_list[:-1] # 切片
print test_list + [158, 'cxm', 1.58] # 连接
print test_list * 3

#类型特定的方法
test_list.append('hehe')
print test_list
# 这里貌似append的返回值是NONE，所以直接printf会打印NONE
print test_list.pop(2)
test_list1 = ['aa', 'cc', 'bb']
test_list1.sort()
print test_list1
test_list1.reverse()
print test_list1
test_list.extend(['dd', 'ee'])
print test_list
print dir(test_list1)

# 嵌套
# python支持列表嵌套其他任意类型
M = [[1,2,3],
     [4,5,6],
     [7,8,9]]
# 列表嵌套列表可以表示矩阵或者二维数组
print M[1][0]

#列表解析
print M[0] # 可以简单地用index获取矩阵的行
# 我们现在需要用简单的方式来获取列，这里用到列表解析
print [row[0] for row in M]
# 这里row变量可以随便给，比如i也可以，列表解析即在列表中运行一个表达式创建一个新的列表
print [i[1] for i in M if i[1] % 2 == 0]
# 只能说这个特性太棒了！
print [M[i][i] for i in [0,1,2]]
print [c * 2 for c in 'spam']
