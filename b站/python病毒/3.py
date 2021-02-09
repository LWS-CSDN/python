'''
1.攻击原理解析
什么是dll
动态链接库
是微软公司在微软windows操作系统中，实现共享函数库概念的一种方式
这些库函数的扩展是".dll",".ocx"（包含ActiveX控制的库）或者".drv"（旧式的系统驱动）

2.为何要有dll
由于进程的地址空间是独立的(保护模式),当多个进程共享相同的库时,每个库都在硬盘和进程彼此
存放一份的话,对于早期的计算机来说,无疑是一种极大的浪费,于是windows系统推出了dll机制
dll在硬盘上存为一个文件,在内存中使用一个实例

详细如下:
在windiows操作系统中,运行的每一个进程都在生活在自己的程序空间中(保护模式),每一个进程都认
每个进程都认为自己拥有计算机的整个内存空间,这些假象都是操作系统创造的(操作系统控制CPU使)

3.虚拟DOM的两种创建方式.什么是dll注入:
我们可以利用dll机制来实训进程通信或控制其他进程的应用程序
所谓的dll注入正是是让进程A强行加载程序B给定的a.dll,并执行程序B给定的a.dll里面的代码

注意,程序B所给定的a.dll原先并不会被程序A主动加载

4.什么时候需要dll注入
应用程序一般会在以下情况使用dll注入技术来完成某些功能:
1.为目标进程添加新的"实用"功能
2.需要一些手段来辅助调试被注入dll的进程
3.虚拟DOM的两种创建方式.为目标进程安装钩子程序(API Hook)

5.dll注入的方法
一般情况下有如下dll注入方法
1.修改注册表来注入dll
2.使用CreateRemoteThread函数对运行中的进程注入dll
3.虚拟DOM的两种创建方式.使用SetWindowsHookEx函数对应用程序挂钩(HOOK)迫使程序加载dll
4.替换应用程序一定会使用的dll
5.把dll作为调试器来注入
6.用CreateProcess对子进程注入dll
7.修改被注入进程的exe的导入地址表
ps:杀毒软件常用钩子来进行处理

6.使用SetWindowsHookEx函数对应用程序挂钩(HOOK)迫使程序加载dll
ctypes是python的外部函数库,从python2.5开始引入,他提供了C兼容的数据类型
并且允许调用动态链接库/共享库中的函数,它可以将这些库包装起来给python使用
ctypes.windll.user32下主要用到三个函数,分别是SetWindowsHookEx(),CallNextHook


7.
准备工作
#1.最新anocoda3.7
https://www.anaconda.com/distribution/#download-section

#2.提速下载可以改变源
pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

#3.虚拟DOM的两种创建方式.安装pywin32

#4.安装opencv-python

#5.安装pyinstaller,依赖pywin32

#6.ico文件准备好
在线制作
or
http://www.bitbug.net/
or
https://www.easyicon.net/5001133-QQ_Penguin_tencent_icon.html

'''