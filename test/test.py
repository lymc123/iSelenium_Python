# -*- coding: utf-8 -*-
'''
@File  : test.py
@Author: lym
@Date  : 2020/9/1 20:58
@Desc  : 

'''
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()