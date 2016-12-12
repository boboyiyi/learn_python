# -*- coding: utf-8 -*-
# while
L = [i + 1 for i in range(10)]
i = 0
while i < len(L):
    if L[i] == 3:
        i += 1
        continue 
    elif L[i] % 2 == 0: print L[i]
    elif L[i] == 8: break
    else: pass # pass means do nothing
    i += 1
# while else是python特有的结构，可以让代码简洁一些，我觉得没多大用

# for
sum = 0
for i in range(10):
    sum += i
print sum

for i in "boboyiyi":
    print i,
# 加,号不换行，只加一个空格

T = [(1,2), (3,4), (5,6)]
for (a,b) in T:
    print a, b,

str1 = "abc"
str2 = "adc"
str3 = ""
for i in str1:
    for j in str2:
        if i == j:
            str3 += i
            break
print str3
# 多重循环

for line in open("test.txt"):
    print line.upper()

test = list(open("test.txt"))
print test

print range(5), range(2, 5), range(0, 10, 2)

test_str = "boboyiyi"
for i in range(0, len(test_str), 2): print test_str[i],

L1 = [1,2,3,4]
L2 = [5,6,7,8]
print zip(L1, L2)
for (x,y) in zip(L1, L2):
    print x, y, "---", x + y

l1 = (1,2,3)
l2 = (4,5,6)
l3 = (7,8,9)
t1 = zip(l1,l2,l3)
# 只要长度一样，列表还是tuple都可以用zip
print t1

s1 = 'abc'
s2 = 'hgilq'
print zip(s1,s2)
# 长度不一样，会截断

# zip创建字典的示例
L1 = ['name', 'height']
L2 = ['fanbo', 180]
D = dict(zip(L1, L2))
print D

lines = [line.rstrip() for line in open('test.txt')]
print lines

print [x + y for x in 'abc' for y in 'efg']
