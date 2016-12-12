# -*- coding: utf-8 -*-
choice = 'hehe'
if choice == 'fb':
    print 'Yes!'
elif choice == 'cxm':
    print 'No!'
else:
    print 'hehe'
# python中没有switch语句，我们可以使用if语句或者字典实现
# 字典中也可以使用函数，所以复杂性这里不用担心
D = {'fb':'Yes!',
        'cxm':'No!'
        }
print D.get(choice, 'hehe') # 这一句增加了switch的default
