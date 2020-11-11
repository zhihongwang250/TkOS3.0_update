# coding:utf-8

import os
print('你确定要卸载吗？y/n')
yn = input()
if yn == 'y':
    os.rmdir('d:/TkOS')
    print('卸载成功。')
else:
    pass
input('press enter to quit')
