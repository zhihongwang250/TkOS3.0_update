# coding:utf-8
import os
import shutil
# 安装程序

def setup():
    input('注意：安装之前您必须有一个d:\的系统分区，如果没有，请划分这个系统分区。\n\
如果您不同意，无法安装，同意请按回车。')
    try:
        print('开始安装')
        os.mkdir('d:\TkOS')
        shutil.copy(' {}\code'.format(os.getcwd()))
        print('安装结束。')
    except FileExistsError:
        print('对不起，您已经在指定的文件目录下安装或手动创建了TkOS的系统文件夹。')
    except OSError:
        print('对不起，您没有创建系统分区。')
    finally:
        print('setup was over.')
        input('press enter to quit:')

if __name__ == '__main__':
    setup()