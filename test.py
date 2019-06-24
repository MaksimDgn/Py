#!coding=utf-8

import os
from sys import argv

script, arg, arg2 = argv[0:]
#t = argv[1:]
dash = '-'*20

fname = 'fin.txt'
f = open(fname, 'r')
print(f.read())
f.close()

print(dash)

str = 'hello world'
print(str)
path = "pytestdir 2"
try:
    os.mkdir(path)
except OSError:
    print("Не удалось создать дерикторию {}".format(path))
else:
    print("Дериктория {} успешно создана".format(path))

print(dash)
print("Script: {} \n argv 1: {} \n arg 2: {}".format(script, arg, arg2))
