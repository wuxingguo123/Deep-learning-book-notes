首先你要先访问华为云Python镜像源：[Simple Index](https://repo.huaweicloud.com/repository/pypi/simple/d2l/)，滑动至页面底部，下载最新版本的.tar.gz源码包（如d2l-1.0.3.tar.gz）。滑动至页面底部，下载最新版本的.tar.gz源码包（如d2l-1.0.3.tar.gz）。下载好后，打开该文件所在位置。

随后打开Anaconda Prompt，先激活自己的环境：
`conda activate [你的环境名]`

然后使用 `cd` 命令来到你下载好的文件地址处。

随后，输入解压缩的命令符：
`tar -zxvf [你的文件名].tar.gz`

下载完成后，进入文件目录中：
`cd d2l-1.0.3`

**(以spyder为例)**
1.  打开你的 python 编辑器，选择文件夹中的 **`setup.py`** 文件并打开。
2.  将 `requirements` 里面的所有等式 (`==`) **全部**改成 `>=` 样式。
3.  随后在 Anaconda Prompt 上输入命令：
    `pip install .`

下载完成后，打开 spyder 点：**控制台 -> 重启 ipython 内核**。

验证下载是否成功：
```python
import d2l
print(d2l.__version__)
