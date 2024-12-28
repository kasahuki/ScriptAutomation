# SCRIPT & DOC?EXCEL? の AUTOMATIC

## bat(powershell) & Autohotkey

### BAT（批处理）文件的主要用途：

1. 系统自动化
- 批量执行命令
- 自动化系统维护
- 简化重复性任务

2. 系统管理
- 启动/关闭服务
- 文件备份
- 系统清理
- 网络配置

3. 程序管理
- 快速启动程序
- 设置运行环境
- 程序部署
- 自动更新

4. 文件操作
- 文件复制
- 文件移动
- 文件重命名
- 批量文件处理

5. 系统信息
- 系统诊断
- 硬件信息收集
- 网络状态检查

6. 开发辅助
- 编译脚本
- 测试环境配置
- 项目构建

7. 日常事务
- 定时任务
- 系统监控
- 性能优化

8. 远程管理
- 远程执行命令
- 服务器维护

简单、轻量、直接调用系统命令是其最大优势。

### Bat应用场景

**适合简单场景：**

启动程序
执行基本命令
文件操作
简单的系统交互
**局限性：**

交互复杂度有限
无法精确模拟鼠标键盘
缺乏高级控制流
**更好的替代方案：**

AutoHotkey（Windows）
Python + PyAutoGUI
Selenium（Web应用）
AutoIt
Robot Framework
**BAT 适合**：

简单启动流程
基础命令执行
系统级操作
**不适合：**

复杂交互
精确控制
高级自动化
建议根据具体需

---







## Autohotkey















---



## Python-basic_syntax



~~~python
"""
注释变色
"""
# 输入都是读到回车为止
# 对于空格的处理
# 如果用户输入多个值，默认会将所有内容作为一个字符串
# a = input() # 返回str
# print("hello world")

a = 1
if a == 1:
    print(a)
    print("缩进数量代表代码块部分" , end="不换行")
else:
    print("a+2") # print 输出默认换行
print("--->end="" 表示不换行")
# 数据类型无需声明 但是必须要有赋值 （和js类似）
floatNum = 100.0
stringVar = "hello world!"
isEmpty = False

#数据类型转换
# 隐式转化 整型和字符串 --> 字符串
# 布尔和整型 -->整型
print(type(isEmpty))
print(type(a))
print(type(stringVar))

print(stringVar + " cat " + str(floatNum))
# 字符串是str 不是string

# --------------------------------

# 字符串知识点

# 字符串索引
# 切片操作 也是前闭后开的
print(stringVar[1:5])
print(int(5/2))
a = 1/3
print(int(a))
# 向下取整
print(3/2) # 输出1
print(2.5//2)  # 输出 1.0
# 对于整数和浮点谁的向下取整输出不一样

print(2**10) # 次幂

if a==1 or a==1/3:
    print("HAHA")
elif a == 2:
    print(False)
else:
    print(True)
# || && 用 or and 代替

str1 = "scarletkasa0@gmail.com"
str2 = "scarlet"
str3 = "gmail.net"
print(str2 in str1)
print(str3 in str1)

# ——————————————————————————————————————————————————
# 复合数据类型
# ——————————————————————————————————————————————————
## <列表>（python最常用的数据类型）

"""
列表是一种可变（Mutable）的有序序列，可以包含任意类型的元素。
使用方括号 [ ] 来表示，元素之间用逗号 , 分隔。
可以通过索引访问和修改列表中的元素。
示例：my_list = [1, 2, 3, 'hello']
与其他语言的比较：

类似于 C++ 中的 std::vector 或 Java 中的 ArrayList，但 Python 中的列表更灵活，因为它可以包含不同类型的元素。
"""
# a = [1,5,8,9,3,555.8,"sfsdf"]
# 列表函数


# ——————————————————————————————————————————————————
## <元组> Tuple

"""
组是一种不可变（Immutable）的有序序列，一旦创建后不能修改。
使用圆括号 ( ) 来表示，元素之间用逗号 , 分隔。
可以通过索引访问元组中的元素，但不能修改。
示例：my_tuple = (1, 2, 'hello')
与其他语言的比较：

与 C++ 的 std::tuple 相似，但在 C++ 中，元组通常用于固定长度的异构数据结构。
"""
ta = (1,2, 8, 7, 7, 8, 75, 23, 65, 23, 56, 89, 63, 45, 35, 56 )
print("Tuple_ta:",ta)
# 和list的区别在于不可改变性
# 可以作为字典的键
#  发法稀缺： count() 和 index(值) -->返回i第一个查找到的值的下标
#——————————————————————————————————————————————————
## <字典> dictionary
# 字典索引必须要是不可变类型 （如 字符串 和 元组）
# 字典的键必须是唯一的
"""
Python中的字典：

字典是一种无序的键值对（Key-Value）集合。
使用花括号 { } 来表示，每个键值对之间用逗号 , 分隔，键和值之间用冒号 : 分隔。
键必须是不可变的类型（通常是字符串或整数），值可以是任意类型。
示例：my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
与其他语言的比较：

类似于 C++ 中的 std::map 或 Java 中的 HashMap，但 Python 中的字典更加灵活，键和值的类型可以是任意的。
"""
a = {"senjay": 999, "kasa": 253, "Guanhui": 456, 520:"Keiko Takahashi"}
# print(a[520],a["senjay"])
print(a)
print(a.get(52)) # 和索引的区别就是不会空指针异常
print(a.keys(),"---",a.values())
# 可以修改

a = {"senjay":"a", "kasa":"b", "gaunhui":"c"}
for i in a:
    print(i)
 # 遍历是遍历键key



# 合并两个不冲突的字典

dict1 = {1: "senjay", 2: "kasa", 3: "kasahuki", 4: "guanhui", 5: "attavoy " }

dict2 = {1: "senjay", 2: "kasa", 3: "kasahuki", 4: "guanhui", 5: "attavoy "}

dict4 = {1: "spenjay"}

dict1.update(dict4)  # 如果key 冲突了就会用和第二个字典覆盖
print(dict1)
# update(self, __m, kwargs) 参数是什么意思

d = {**dict1,**dict4} # 同理
print("d:",d)
# 总之就是注意有些函数是没有返回值的！！！


# ——————————————————————————————————————————————————
# 面向 ** 的思想
"""
Python
主要是面向对象编程（OOP）
也支持面向过程编程
支持函数式编程特性
C++
面向对象编程（OOP）
面向过程编程
支持泛型编程
C语言
主要是面向过程编程
不支持面向对象编程
Java
纯面向对象编程（OOP）
一切皆对象的设计理念
JavaScript
基于原型的面向对象编程
支持函数式编程
支持面向过程编程
主要编程范式说明：

面向对象编程：以对象为核心，将数据和操作数据的方法封装在对象中
面向过程编程：以过程（函数）为中心，强调步骤和顺序
函数式编程：以函数为主要编程元素，强调数据处理的纯粹性
泛型编程：编写适用于多种数据类型的代码
"""
# 循环

for i in range(4): # (0 1 2 3)
    print(i)
for i in "hello world!":
    print(ord(i),end=" ")
print('')
for i in ["red",str1,str2,str3]:
    print(i)
n = 5
# python 不支持 n-- 自增自减
while n:  # 和if一样  if n 不为0就一直做
    print(n)
    n -=1

# range(起始值,终止值,步进)
# 就是for循环自己确定始末 和 ?++而已
for i in range(1,8,2):
    print(i)

print("-----")
demo = [1, 5, 8, 9, 7, 6]
for i in range(len(demo)):
    print(demo[i],end=" ")

# 格式化输出
c = "senjay"
print("")
print(f"My name is {c}")
# 字典循环的技巧



~~~



## ListFunc

~~~python
# 函数最重要的就是 返回类型确定 函数名 传参数 逻辑体 返回值（NULL）

arr1 = [2,5,8,9,5,3,6]
print("len:",len(arr1))
print("5 の count = ",arr1.count(5))
print(arr1.pop()) # 返回结尾元素并弹出
print(arr1.pop(2)) # 也可删除指定位置的东西
arr1.append("end") # 对应pop
# arr1.insert(1,4)
# arr1.remove(4)
print("len:",len(arr1))
# 删除第一个value=4 的item（项）

# del(arr1[1:3]) 删除列表切片
# arr1.reverse()  无返回值会直接修改原表

print("arr1:",end="")
for i in arr1:
    print(i,end=" ")
print("")
# arr1.clear()
arr1.pop()
arr1.sort() # 原地排序没有返回值
arr1.sort(reverse=True)
print("sortedArr1:",end=" ")
for i in arr1:
    print(i,end=" ")
print("")
arr2 = sorted(arr1,reverse=True)
print("arr2:",end="")
for i in arr2:
    print(i,end=" ")
# 注意XX.func() or func(XX)
print("")
print("Final",arr2[2],arr1[1],arr2[4],"end") # 自动空格！！！




~~~



## addition1

~~~python
a = "hello world!"
print(a[-5]) # 支持从右边开始计数
# float 精度更高
b = "haha" * 2 + "lala" *3
# 使用 + 进行拼接，* 进行重复
print(b)
# 反斜杠都是表示转移 '\'
print('scarletkasa0@gmail.com')
print('\'') # 打印单引号

# 字符串不可修改 immutable
"""
a[0] = '5' 
print(a)
 
不支持 item assignment(赋值)
"""
print(a[-1:-3:-1]) #str[起始位:终止位:步长]
# 步长的方向要和 始末为止走向一样！！

print(len(a))
print(a.title())
print(a.upper())
print(a.lower())
print(a.lstrip())
print(a.rstrip())
print(a.strip())

# 注释英文：comment
~~~

## FUNCTION

### ==参数部分==

#### 示例：有多个参数，带默认值

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")  # 使用默认值 "Hello"
greet("Bob", "Good morning")  # 使用自定义的问候语 "Good morning"
```

#### 示例：可变数量的位置参数（`*args`）

```python
def sumargs(*args):
    temp = 1
    for i in args:
        temp *=i
    return temp


print(sumargs(1,5,8,9,6))
```

#### 示例：可变数量的关键字参数（`**kwargs`）

```python
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30)
# 输出:
# name: Alice
# age: 30
```

### ==返回值==

#### 示例：返回多个值（作为元组）

```python
def swap(a, b):
    return b, a

x, y = swap(3, 4)
print(x, y)  # 输出 4 3
```

#### 示例：返回列表或字典

```python
def create_dict(a, b):
    return {"first": a, "second": b}

result = create_dict("Alice", "Bob")
print(result)  # 输出 {'first': 'Alice', 'second': 'Bob'}
```

## 解包实参列表 （类比js解构）

对于==列表==或是==元组==

~~~python
stu1 = ["senjay",19,180,62]
stu2 = ["senjay",20]
def solve(name = None,age = None,height = None,weight = None):
    print(name,age,height,weight)

# 模拟函数重载
solve(*stu1)
solve(*stu2)

~~~

对于==字典== 或者是那种涉及了kwargs 也就是关键字键值对这样的，都是有两个*（就比如==上面传参数那里==）

**！！！在Python中，当使用 kwargs 时，键必须是字符串类型。****

~~~python
dict = {'1':"a",'2':"b",'3':"c",'4':"d",'5':"e",'6':"f"}  # 键改为字符串

def catLetter(**kwargs):
    ans  = ""
    for i in kwargs:
        ans+=kwargs.get(i)
    return ans
ans = catLetter(**dict)
print(ans)

~~~

缩进问题：注意不要有多余的==前空格==

## 变量作用域

------

函数内部只作引用的 `Python` 变量隐式视为全局变量。如果在函数内部任何位置为变量赋值，则除非明确声明为全局变量，否则均将其视为局部变量：

```python
a = 1
 
def use():
    print(f"use: {a}")
 
def change():
    a = 114514
 
use()
change()  # 调用函数
 
print(a)  # a 的值不发生改变
```

可以看到，`use()` 函数在只做引用的情况下将 `a` 视为了全局变量，而在 `change()` 函数中对 `a` 做修改，则将 `a` 视为了局部变量，并没有改变其值。

使用关键词 [`global`](https://docs.python.org/zh-cn/3.9/reference/simple_stmts.html#global) 声明变量，将被视为全局变量，在函数对象中更改不再视为局部变量：

```python
a = 1
 
def use():
    print(f"use: {a}")
 
def change():
    global a
    a = 114514
 
use()
change()  # 调用函数
 
print(a)  # a 的值不发生改变
```



## 模块导入



模块是包含 `Python` 定义和语句的文件。其文件名是模块名加后缀名 `.py` 。在模块内部，通过全局变量 `__name__` 可以获取模块名（即字符串）。

模块包含可执行语句及函数定义。这些语句用于初始化模块，且仅在 `import` 语句第一次遇到模块名时执行。

首先创建一个名为 `solve.py` 的文件：

```python
def Sum(n):
    """Calculate the sum of list and return the result"""
    t = 0;
    for i in range(len(n)):
        t += n[i]
    return t
 
def Fib(n):
    """Create a list which is the first n terms of the Fibonacci series"""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib
```

在该文件中，我们定义了 `Sum` 和 `fib` 函数，接下来在另一个 `.py` 文件里导入并使用：



```python
from solve import Sum
from solve import Fib
a = [1, 2, 3, 4]
print(Fib(Sum(a)))
```

也可以一次性导入该模块中所有的函数定义：

```python
from solve import *
a = [1, 2, 3, 4]
print(Fib(Sum(a)))
```

### pip Python 导入库

~~~python
import numpy as np

from numpy import add 
~~~



![image-20241226213320148](https://cdn.jsdelivr.net/gh/kasahuki/os_test@main/img/image-20241226213320148.png)

#### 包管理工具



~~~
1. Docker

    - 包管理：Docker Hub, Docker Registry
2. Node.js

    - npm (Node Package Manager)
    - Yarn
3. Linux 发行版

    - Debian/Ubuntu: apt, dpkg
    - Red Hat/CentOS: yum, dnf (较新版本)
    - Arch Linux: pacman
    - Fedora: dnf
    - openSUSE: zypper
4. Python

    - pip
    - conda (用于Anaconda发行版)
5. Java

    - Maven
    - Gradle
    - Apache Ivy
~~~



# 大数据分析部分



## FILE_PROCESS

~~~python
# 文件操作

## 文件读取和写入

## 文件对象及方法




~~~



## DATA_PROCESSOR

**lower_bower : 下界**

**upper_bower : 上界**

~~~python
# 数据处理和可视化
# numpy(数组计算) pandas（表格） Matplotlib(绘图)
# 脚本自动化 联系js shell脚本呢？

~~~

~~~ceylon
CSV (Comma-Separated Values) 和 Excel 文件是两种常用的数据存储格式，它们有以下主要区别：

1. 文件格式：
   - CSV 是纯文本文件，通常使用逗号（或其他分隔符）分隔数据。
   - Excel 文件是二进制格式，可以包含多个工作表、格式化、公式等。

2. 复杂性：
   - CSV 格式简单，易于读写和处理。
   - Excel 格式更复杂，支持更多功能，如多个工作表、图表、宏等。

3. 数据类型：
   - CSV 只存储原始数据，不保留数据类型信息。
   - Excel 可以保存和识别不同的数据类型（如日期、数字、文本）。

4. 文件大小：
   - CSV 文件通常比等效的 Excel 文件小。
   - Excel 文件因包含额外信息和功能，通常更大。

5. 兼容性：
   - CSV 几乎可以被所有数据处理软件读取。
   - Excel 文件主要用于 Microsoft Excel，虽然其他软件也可以读取，但可能会丢失一些高级功能。

6. 格式化和样式：
   - CSV 不支持任何格式化或样式。
   - Excel 支持丰富的格式化选项，如字体、颜色、边框等。

7. 计算能力：
   - CSV 仅存储数据，不支持公式或计算。
   - Excel 支持复杂的公式和计算功能。

8. 多表支持：
   - CSV 通常只包含单个数据表。
   - Excel 文件可以包含多个工作表。

9. 编辑难度：
   - CSV 可以用任何文本编辑器编辑。
   - Excel 文件通常需要专门的软件（如 Microsoft Excel）来编辑。

10. 数据分析：
    - CSV 适合简单的数据存储和传输。
    - Excel 更适合进行数据分析、可视化和报告生成。


~~~



