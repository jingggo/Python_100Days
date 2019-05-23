# Python_100Days
A project to record the process of learning Python  
And this project following [Python-100-Days](https://github.com/jackfrued/Python-100-Days)

**Useful Information**:
- [Python 简史](http://www.cnblogs.com/vamei/archive/2013/02/06/2892628.html)  
- [Anaconda安装](https://www.jianshu.com/p/62f155eb6ac5)  

#### Day001
Python 简介，优缺点及其安装
#### Day002
语言元素
#### [Day003 If语句](https://github.com/jingggo/Python_100Days/tree/master/Day01-15/Day003)
#### [Day004 for and while loop](https://github.com/jingggo/Python_100Days/tree/master/Day01-15/Day004)
#### [Day005 练习](https://github.com/jingggo/Python_100Days/tree/master/Day01-15/Day005)
For practice
1. Lily
1. Perfect num 
1. Chicken
1. Fibonacci
1. Craps
1. 
#### [Day006 函数](https://github.com/jingggo/Python_100Days/tree/master/Day01-15/Day006)
函数的模块和使用  
函数的作用：
防止冗余代码  
def 定义  
```
buildoutcfg
    def foo():
        pass
```
用模块管理函数：  
同一个.py文件中定义了两个同名函数，由于Python没有函数重载的概念，那么后面的定义会覆盖之前的定义，也就意味着两个同名函数实际上只有一个是存在的。  
```
def foo():
    print("Hello")


def foo():
    print("World")


foo()

Output: World
```
如何避免同名函数的情况：  
答案其实很简单，Python中每个文件就代表了一个模块（module），我们在不同的模块中可以有同名的函数，在使用函数的时候我们通过import关键字导入指定的模块就可以区分到底要使用的是哪个模块中的foo函数。  
补充说明：  
如果我们导入的模块除了定义函数之外还中有可以执行代码，那么Python解释器在导入这个模块时就会执行这些代码，
事实上我们可能并不希望如此，因此如果我们在模块中编写了执行代码，最好是将这些执行代码放入如下所示的条件中，
这样的话除非直接运行该模块，if条件下的这些代码是不会执行的，因为只有直接执行的模块的名字才是"__main__"。

#### [Day007 数据结构](https://github.com/jingggo/Python_100Days/blob/master/Day01-15/Day007/CommonDataStructure.md)(str, list, tuple, list, dic, set)
#### [Day008 面向对象编程](https://github.com/jingggo/Python_100Days/tree/master/Day01-15/Day008/面向对象编程基础.ipynb)
#### [Day009 面向对象进阶](https://github.com/jingggo/Python_100Days/tree/master/Day01-15/Day009)
#### [Day010 图形界面编程tkinter](./Day01-15/Day010)
#### [Day011 文件操作](./Day01-15/Day011)
#### [Day012 正则表达式](./Day01-15/Day012)
#### [Day013 进程和线程](./Day01-15/Day013)
#### [Day014 网络协议](./Day01-15/Day014)
#### [Day015 图像和办公文档处理](./Day01-15/Day015)
[Python实现十大经典排序算法](https://cloud.tencent.com/developer/article/1108770)
