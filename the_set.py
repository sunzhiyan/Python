# -*- encoding: utf-8 -*-
'''
@File : the_set.py
@Time : 2020/03/07 10:21:42
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
set1 = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(set1)
print('orange' in set1)
set2 = set('sdhfjskxmdvnjdg')
set3 = set('dnvbmxbcdbvnxzmvn')
print(set2-set3)
print(set2|set3)
print(set2&set3)
print(set2^set3)