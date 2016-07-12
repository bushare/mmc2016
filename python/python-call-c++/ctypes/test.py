# -*- coding: utf-8 -*-
from ctypes import *
import os.path

#必须写绝对路径
s=CDLL(path.join(path.dirname(path.abspath(__file__)), "test.so"))

#c的int数组
a=(c_int*10)()

def opt(a):
  for i in range(len(a)):
    print a[i]

for i in range(len(a)):
  a[i]=i

opt(a)
print
print s.foo(a,len(a))
opt(a)
