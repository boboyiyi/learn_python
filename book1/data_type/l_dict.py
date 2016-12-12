# -*- coding: utf-8 -*-

# 映射操作，即字典构建和访问
test_dict = {'name':'cxm', 'height':158, 'marry':'no'}
print test_dict['name']
print test_dict['height'] + 1
# or如下创建
test_dict = {}
test_dict['name'] = 'cxm'
test_dict['height'] = 158
test_dict['marry'] = 'no'
del test_dict['marry'] # 删除键值，对列表del方法同样适用
print test_dict

# 重访嵌套
test_dict = {'name':{'first':'xiaomin', 'last':'chen'},
             'job':['HR','ENG']}
print test_dict['name']['first']
print test_dict['job'][0]
test_dict['job'].append('SALES')
print test_dict['job']
print test_dict.keys()
print test_dict.values()
print test_dict.items() # 转化为(key, value)元组组成的列表

# 键值排序
test_dict = {'a':1, 'b':2, 'c':3}
print test_dict
for key in sorted(test_dict):
    print key, '==>', test_dict[key]
# 这里注意print可以用','号隔开，打印不同的数据类型，不用str强制转换，然后用'+'号连接
# sorted方法用于对dict的key排序

# 查看键值是否存在
if not test_dict.has_key('hehe'):
    print 'missing'
# has_key测试是否存在键值

# 字典可以被用做表示稀疏矩阵
Matrix = {}
Matrix[(2, 3)] = 1
Matrix[(5 ,8)] = 1
print Matrix

# 避免键值不存在的几种方法
if Matrix.has_key((2, 4)):
    print 'hehe'
else:
    print 0

try:
    print Matrix[(2, 4)]
except KeyError:
    print 0

print Matrix.get((2, 4), 666) # get尝试找key(2, 4)存在与否，不存在则打印666，存在返回键值

