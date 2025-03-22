#  SCRIPT & DOC?EXCEL? の AUTOMATIC、

## bat(powershell) 

**==bat（cmd/powershell）用于系统级别的自动化脚本==**

### WSL powershell/cmd 混用 

前面的是powershell 语法 后面 加个wsl 即可用bash语法

![image-20241230215631002](https://cdn.jsdelivr.net/gh/kasahuki/os_test@main/img/image-20241230215631002.png)

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







# Autohotkey 

==主要用途 ：快捷键自定义 屏幕监控位置 模拟鼠标键盘处理简单任务==

## why ahk or Python

Python 和 AutoHotkey 都是常用的编程语言，但它们的设计目标、用途和功能有所不同。下面是它们之间的一些主要区别：

### 1. **用途和目标**
   - **Python**: 是一种通用编程语言，广泛用于科学计算、Web 开发、自动化脚本、人工智能、数据分析等各种领域。它非常强大且灵活，支持面向对象编程、函数式编程等多种编程范式。
   - **AutoHotkey (AHK)**: 是一种专门用于 Windows 平台的脚本语言，主要用于键盘、鼠标自动化以及图形界面自动化任务。它的核心功能是自动化重复的工作任务，特别是在 Windows 环境中。

### 2. **功能特点**
   - **Python**:
     - 丰富的标准库，支持各种操作（如文件操作、网络编程、数据库操作等）。
     - 强大的第三方库和框架，可以扩展到各个领域。
     - 跨平台支持（Windows、Linux、macOS 等）。
     - 语法简洁，易于学习和使用。
   - **AutoHotkey**:
     - 主要用于键盘和鼠标事件的自动化脚本编写，例如键盘快捷键、鼠标点击、窗口控制等。
     - 非常适合做自动化任务、宏录制、图像识别等与 Windows 操作系统相关的操作。
     - 语法较为简单，容易上手，但功能上不如 Python 那么强大和通用。

### 3. **执行效率和适用场景**
   - **Python**: 
     - 执行效率相对较低，但它更适用于复杂的应用程序开发，能够处理更广泛的任务。
     - 可以通过安装不同的第三方库来实现自动化（例如 `pyautogui` 用于鼠标和键盘自动化，`selenium` 用于网页自动化等）。
   - **AutoHotkey**:
     - 执行效率较高，特别是在简单的鼠标键盘自动化任务中，响应速度较快。
     - 主要用于快速编写一些自动化脚本、快捷键和小工具。

### 4. **跨平台支持**
   - **Python**: 支持跨平台，可以在不同的操作系统上运行同一份代码。
   - **AutoHotkey**: 主要设计为 Windows 平台上的自动化工具，虽然有一些第三方项目支持在其他平台上运行，但本质上是为 Windows 环境优化的。

### 5. **社区和生态系统**
   - **Python**: 拥有一个庞大且多样化的开发者社区，拥有海量的第三方库和资源，适合任何规模的项目。
   - **AutoHotkey**: 主要面向 Windows 用户，社区也很活跃，专注于桌面自动化和快捷键等任务。

### 6. **学习曲线**
   - **Python**: 语法简洁易学，但由于其通用性和广泛应用，可能需要学习更多的编程概念和技术，特别是在做复杂应用时。
   - **AutoHotkey**: 语法简单，学习曲线较低，适合快速上手并编写自动化脚本。



# Python 第三方库

### **Python 是否可以替代 AutoHotkey?**
- **可以**，但取决于具体需求：
  - 如果你只是需要做简单的键盘、鼠标自动化或窗口操作，Python 可以通过 `pyautogui`、`pynput`、`keyboard` 等库来实现相同的功能，甚至可以进行更多的操作。
  - 如果你需要做更复杂的跨平台自动化任务或开发其他类型的应用程序，Python 会更适合。
  - 如果你只是需要在 Windows 环境下做一些简单的快捷键和自动化任务，AutoHotkey 是一个快速且高效的选择。

总结来说，**Python** 是一个功能强大且灵活的编程语言，适合各种任务，而 **AutoHotkey** 则是一个专注于 Windows 平台自动化的脚本语言。在需要跨平台支持或更复杂任务时，Python 是更好的选择；而在进行 Windows 专属的简单自动化时，AutoHotkey 更为方便和高效。

Python 拥有丰富的第三方库，几乎覆盖了所有应用领域。以下是一些常见的 Python 库及其用途，按照功能类别进行分类：

### 1. **数据科学与机器学习**
   - **NumPy**: 提供支持多维数组和矩阵运算的功能，及对线性代数、随机数生成等的支持，是进行数值计算的基础库。
   - **Pandas**: 提供高效的数据处理和分析工具，尤其是数据框（DataFrame）结构，非常适合处理表格数据。
   - **Matplotlib**: 用于绘制静态图表、线图、柱状图等，适合数据可视化。
   - **Seaborn**: 基于 Matplotlib 的高级数据可视化库，提供更易用和美观的图形。
   - **SciPy**: 基于 NumPy 的科学计算库，提供更高级的数学、科学和工程计算功能，如积分、优化、信号处理等。
   - **Scikit-learn**: 机器学习库，提供各种机器学习算法的实现，适用于分类、回归、聚类、降维等任务。
   - **TensorFlow / Keras**: 用于构建和训练深度学习模型，TensorFlow 是一个强大的开源深度学习框架，Keras 是它的高级接口，简化了神经网络的构建。
   - **PyTorch**: 另一个流行的深度学习框架，强调动态图和灵活性，适用于研究和生产环境。

### 2. **Web 开发**
   - **Flask**: 一个轻量级的 Web 框架，适合快速开发小型 Web 应用，支持扩展。
   - **Django**: 功能强大的 Web 框架，适合开发大型和复杂的 Web 应用，内置 ORM、认证、路由等功能。
   - **FastAPI**: 用于构建 API 的现代 Web 框架，速度快，支持异步编程和自动生成 OpenAPI 文档。
   - **Requests**: 用于发送 HTTP 请求，简化了 GET、POST 等请求的使用，支持 API 调用等功能。
   - **BeautifulSoup**: 用于解析和抓取网页内容，广泛用于网页数据的提取（网页爬虫）。
   - **Selenium**: 自动化 Web 浏览器操作，支持网页的自动化测试和爬虫。

### 3. **数据库**
   - **SQLAlchemy**: 强大的 ORM 库，用于与关系型数据库（如 MySQL、PostgreSQL）进行交互，支持 SQL 查询生成和对象关系映射。
   - **SQLite**: 内置的轻量级数据库库，适合小型项目和嵌入式应用。
   - **Peewee**: 另一个轻量级 ORM，用于与 SQLite、MySQL 和 PostgreSQL 等数据库交互。

### 4. **自动化和系统管理**
   - **Celery**: 一个异步任务队列系统，用于分布式任务处理和后台任务调度。
   - **PyAutoGUI**: 用于自动化图形界面操作（例如鼠标移动、点击、键盘输入等）。
   - **paramiko**: 提供 SSH 协议的支持，适用于远程服务器的自动化操作。
   - **Fabric**: 用于自动化远程服务器管理和部署的工具，通常用于 DevOps 场景。
   - **os / sys**: 内置库，提供与操作系统交互的功能，如文件操作、路径管理、环境变量等。

### 5. **图形用户界面（GUI）**
   - **Tkinter**: Python 内置的 GUI 库，用于开发简单的桌面应用程序。
   - **PyQt / PySide**: 基于 Qt 的跨平台 GUI 框架，适用于开发复杂的桌面应用程序。
   - **Kivy**: 开源的 Python 框架，适用于开发跨平台（Windows、Linux、iOS、Android）的应用。

### 6. **网络编程**
   - **socket**: Python 内置的库，用于网络通信，支持客户端和服务器模型。
   - **Twisted**: 异步网络框架，用于构建高性能的网络应用，如 HTTP 服务器、聊天室等。
   - **asyncio**: Python 3.4+ 的标准库，用于编写异步 I/O 代码，支持协程和事件循环。
   - **websockets**: 用于实现 WebSocket 协议的库，支持实时、双向通信。

### 7. **文件操作和处理**
   - **os**: Python 内置库，用于与操作系统进行交互，如文件路径操作、文件删除、目录创建等。
   - **shutil**: 提供文件和文件夹的高级操作，如复制、移动、压缩等。
   - **pathlib**: Python 3.4+ 提供的面向对象的文件路径操作库，比 os.path 更为简洁。
   - **csv**: 处理 CSV 文件的内置库，提供读写操作。
   - **json**: 用于处理 JSON 格式数据的内置库，支持数据解析和生成。

### 8. **测试和调试**
   - **unittest**: Python 内置的单元测试框架，支持测试用例的组织和执行。
   - **pytest**: 一个非常流行的测试框架，比 `unittest` 更简洁，支持更丰富的功能。
   - **mock**: 用于在测试中模拟对象或函数，常用于单元测试中的依赖注入。

### 9. **图像处理**
   - **Pillow**: 图像处理库，支持各种图像格式的打开、编辑、保存等操作。
   - **OpenCV**: 强大的计算机视觉库，支持图像和视频的处理，应用广泛于人脸识别、目标检测等领域。
   - **matplotlib**: 虽然是一个数据可视化库，但也可以用于图像显示和一些简单的图像处理任务。

### 10. **安全性与加密**
   - **cryptography**: 提供对称加密、非对称加密、数字签名等加密功能。
   - **PyCryptodome**: 提供加密、解密、消息认证等功能，支持常见的加密算法。
   - **hashlib**: 用于生成哈希值的库，支持多种哈希算法，如 SHA-256、MD5 等。

### 11. **其他常用库**
   - **regex (re)**: Python 内置的正则表达式库，用于字符串匹配和处理。
   - **time / datetime**: 提供时间和日期处理功能。
   - **logging**: 用于记录日志的标准库，支持不同级别的日志输出。
   - **pytest**: 用于测试代码的框架，支持并行测试和丰富的插件。



# Python工具箱

## FAKER

~~~python
# 用处：爬虫请求头…… （需要表单数据时）
from faker import Faker
fake = Faker('zh-CN') # 指定地区语言 组成：语言代码-国家（地区）代码

student = []


for i in range(5):
  student.append({"name":fake.name(),"address":fake.address(), "phone":fake.phone_number()})

# for i in range(len(student)):
#   print(student[i])
for i in student:
  print(i)
~~~



## pyautogui

**模态窗口（Modal Window）** 是一种 **必须处理后才能继续操作的窗口**。

对话框是 **模态窗口**，意味着必须先关闭它，Python 脚本才会继续运行。

~~~python

import pyautogui as pg
# print(pg.size())

# for i in range(10):
#   print(pg.position())
# pg.alert("hello!", "msg",)
# pg.confirm("Are you sure")
# pg.prompt('What is your name?')
# pg.password()
# pg.alert(
#   text='hello',
#   title='msg',
#   button='continue'
# )
# response = pg.confirm(
#   text='点击数字',
#   title='选择',
#   buttons=['1','2','3']
# )
# if response == '1':
#   pg.alert('first')
# pg.alert(response)

# img1 = pg.screenshot()
# img1.save("test1.png")

# location = pg.locateCenterOnScreen('image.png')
# pg.click(location)

# for i in range(10):
#   pg.click()
#   pg.press('shift')
#   pg.move(15,0)

# x, y = pg.size()
# pg.moveTo(x/2,y/2)


# pg.write('hello')


# pg.mouseDown()
pg.keyDown('shift')

# for i in range(5):
#   pg.move(10,0)

# pg.keyUp('shift')
# pg.mouseUp()
# 一定要解除


# 监听行为呢
# 可以结合opencv 和 


~~~

### **⚠ 为什么执行结束后 Shift 仍然保持按下？**





1. `pg.keyDown('shift')` 只是**模拟按键按下**，但不会**自动执行 keyUp()**。
2. **Python 脚本运行结束，并不会自动释放按键**，所以 Shift **一直保持按住状态**。
3. 如果你执行了 `pg.keyDown("shift")`，但**没有运行 `pg.keyUp("shift")`**，你的系统会一直保持 Shift 被按住的状态，可能导致输入异常（如全大写、快捷键误触发等）。





## Opencv



## python-docx --- office 自动化的入门



![image-20250205145203478](https://cdn.jsdelivr.net/gh/kasahuki/os_test@main/img/image-20250205145203478.png)

~~~python
from docx import Document
# 库只支持docx 文档

dx = Document()

# 添加文本本质是依靠操作段落做到的
# p1 = dx.add_paragraph('senjay')
# print(type(p1))
# print(dx.paragraphs)
# print(len(dx.paragraphs))
# print(p1.text)
# p1.clear() # 清除这个段落
# print(p1.text)

# p1 = dx.add_paragraph("第一段")
# p2 = dx.add_heading("第二章")
# p1.insert_paragraph_before("第0章")
# dx.add_page_break() # 注意分页符也是段落
# p3 = dx.add_heading("第三章")
# p = p2._element # 先获取标签
# p.getparent().remove(p) # clear方法 也只是删除文本 并没有删除段落也没有删除段落符 
# p._p = p._element = None # 释放内存

p1 = dx.add_paragraph("senjay")
p2 = dx.add_paragraph("senjay")
p3 = dx.add_paragraph("senjay")
p4 = dx.add_paragraph("senjay")
p5 = dx.add_paragraph("senjay")

# p1.alignment = ''   左/右/居中对齐  -- 段落样式
# p1.style = '' 打印这个段落样式
# p1.style.delete() 删除样式 恢复成默认的样子也就是正文样式
# dx.add_paragraph("text", style = "")
# for paragraph in dx.paragraphs: 遍历所有段落
dx.save('./office/word/test.docx')  # ./ 表示当前目录通常指的是你当前操作的工作目录或者文件所在的目录

~~~

![image-20250205155921566](https://cdn.jsdelivr.net/gh/kasahuki/os_test@main/img/image-20250205155921566.png)



段前/段后 （这两个是不同段落间的）/行间距（这个是一个段落文字间的）

**在当前段落添加文本直接添加run就行**

run是相对于一个段落的 p.runs

**同理也有run的样式**



如果要根据一个模板制作上百个文件 直接根据数据excel 表格结合word 写一个函数封装逻辑 获取excel数据 用数据结构存储

然后分别根据word样式特征==装填文字==

也可以用变量包装重要信息 使用{}使用变量

~~~python
from docx import Document
from docx.enum.text import WD_UNDERLINE

# 打开文档
doc = Document('./office/word/produ1.docx')  # 替换为你的文档路径

# 遍历文档中所有的段落
for paragraph in doc.paragraphs:
    # 遍历段落中的每一个run
    runs = paragraph.runs
    i = 0
    while i < len(runs):
        if runs[i].underline and runs[i].text.startswith(" "):
           run = runs[i]
           while i + 1 < len(runs) and runs[i].underline and runs[i].text.startswith(" "):
               run.text += runs[i+1].text
               i+=1
           run.text="5245"
        i+=1

        

        
# 保存修改后的文档
doc.save('./office/word/produ1.docx')

~~~







## openpyxl & pandas



---



# 网络爬虫库相关



**`requests`**:

- 通过直接发送 HTTP 请求与服务器交互，模拟浏览器发送 GET、POST 等请求，并获取响应。
- 主要用于与服务器进行数据交互，**不模拟浏览器的用户行为**，因此不处理 JavaScript 动态渲染内容。
- 更适合用于 **抓取静态网页** 或者通过 API 获取数据。

**`selenium`**:

- 通过控制真实浏览器（如 Chrome、Firefox）来模拟用户的操作（点击、输入、滚动等），可以执行 JavaScript 并加载网页的完整内容。
- **适用于动态网页**，即页面内容由 JavaScript 渲染生成的情况。
- 在执行操作时，会打开一个图形化的浏览器界面或者以无头模式运行（没有 GUI 界面的浏览器）。
