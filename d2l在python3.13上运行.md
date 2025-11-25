首先你要先访问华为云Python镜像源：Simple Index滑动至页面底部，下载最新版本的.tar.gz源码包（如d2l-1.0.3.tar.gz）
https://repo.huaweicloud.com/repository/pypi/simple/d2l/  
下载好后，打开该文件所在位置。随后打开Anaconda Prompt，先激活自己的环境后，再使用cd:命令符来到你下载好的文件地址处  
随后，输入解压缩的命令符tar -zxvf，再复制你下载的文件名(例如：(ml_env) D:\Micsoft下载的文件>tar -zxvf d2l-1.0.3.tar.gz) 下载完成后进入文件目录中
(以spyder为例)  
1.打开你的python编辑器
2.打开文件
3.选择文件夹中的setup.py的文件并打开
4.将requirements里面的等式全部改成>=样式
5.随后在Anaconda Prompt上输入命令`pip install .`
