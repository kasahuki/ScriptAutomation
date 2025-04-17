1. 基本语法

AHK2使用 `:=` 进行变量赋值:

```autohotkey
myVar := "Hello World"
```

使用 `#` 定义热键:

```autohotkey
#z:: Run "notepad.exe"  ; Win+Z 打开记事本
```

2. 发送按键和文本

```autohotkey
Send "Hello World"  ; 发送文本
Send "{Enter}"     ; 发送回车键
SendInput "{LWin down}r{LWin up}"  ; 按下Win键,按R,松开Win键
```

3. 运行程序和命令

```autohotkey
Run "notepad.exe"  ; 运行记事本
Run "explorer.exe C:\Users"  ; 打开用户文件夹
RunWait "cmd.exe /c ping www.google.com"  ; 运行命令并等待完成
```

4. 窗口操作

```autohotkey
WinActivate "Untitled - Notepad"  ; 激活记事本窗口
WinMaximize "A"  ; 最大化当前活动窗口
WinMinimize "Calculator"  ; 最小化计算器窗口
```

5. 鼠标操作

```autohotkey
Click 100, 200  ; 在坐标(100, 200)处点击
MouseMove 500, 500  ; 移动鼠标到坐标(500, 500)
MouseClickDrag "Left", 0, 0, 200, 200  ; 从(0,0)拖拽到(200,200)
```

6. 剪贴板操作

```autohotkey
A_Clipboard := "Text to clipboard"  ; 设置剪贴板内容
clipText := A_Clipboard  ; 获取剪贴板内容
```

7. 文件操作

```autohotkey
FileAppend "Log entry`n", "C:\log.txt"  ; 追加内容到文件
FileRead content, "C:\data.txt"  ; 读取文件内容
```

8. 字符串操作

```autohotkey
str := "Hello, World!"
SubStr(str, 1, 5)  ; 返回 "Hello"
StrReplace(str, "World", "AutoHotkey")  ; 替换字符串
```

9. 数组和对象

```autohotkey
myArray := [1, 2, 3, 4, 5]
myArray.Push(6)  ; 添加元素

myObject := {name: "John", age: 30}
myObject.job := "Developer"  ; 添加属性
```

10. 函数定义和调用

```autohotkey
MyFunction(param1, param2) {
    result := param1 + param2
    return result
}

x := MyFunction(5, 3)  ; 调用函数
```

11. 条件语句

```autohotkey
if (x > 0) {
    MsgBox "x is positive"
} else if (x < 0) {
    MsgBox "x is negative"
} else {
    MsgBox "x is zero"
}
```

12. 循环

```autohotkey
; For 循环
for i in [1, 2, 3, 4, 5] {
    MsgBox i
}

; While 循环
count := 0
while (count < 5) {
    count++
    MsgBox count
}
```

13. 定时器

```autohotkey
SetTimer TimerFunc, 1000  ; 每1000毫秒执行一次

TimerFunc() {
    ToolTip "Timer tick"
}
```

14. 热字符串

```autohotkey
::btw::by the way
::omw::on my way
```

15. GUI创建

```autohotkey
MyGui := Gui()
MyGui.Add("Text", "x10 y10 w200", "Hello, World!")
MyGui.Add("Button", "x10 y40 w100", "Click Me").OnEvent("Click", ButtonClicked)
MyGui.Show()

ButtonClicked(*)
{
    MsgBox "Button was clicked!"
}
```

