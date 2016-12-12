# -*- coding: utf-8 -*-
file1 = open('test.txt', 'w')
file1.write('Hello, World!\n')
file1.write('My name is Fanbo.\n')
file1.close()
# file write

file2 = open('test.txt', 'r')
all_contents = file2.read()
print all_contents
# 或者直接 print open('test.txt','r').read()
file2.close()
file2 = open('test.txt', 'r')
print file2.readline().rstrip()
print file2.readline().rstrip()
print file2.readline()
print file2.readline()

# 将对象（比如dict直接写入文件并load）
import pickle
fo = open('fo_type', 'w')
D = {'name':'fanbo', 'height':180}
print D
pickle.dump(D, fo)
fo.close()
D = {}
fi = open('fo_type')
D = pickle.load(fi)
print D

