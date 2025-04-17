import cv2
import pygetwindow as gw
import time
import ctypes
from pynput import keyboard


def is_locked():
    """检查 Windows 是否处于锁屏状态"""
    user32 = ctypes.windll.User32
    return user32.GetForegroundWindow() == 0  # 如果前台窗口句柄为 0，则说明锁屏

def capture_image():
    """拍照并保存"""
    cap = cv2.VideoCapture(0)  # 打开摄像头
    if not cap.isOpened():
        print("无法打开摄像头")
        return

    # time.sleep(2)  # 等待摄像头稳定

    ret, frame = cap.read()  # 读取画面
    if ret:
        cv2.imwrite("py_captured_image.jpg", frame)  # 保存照片
        print("照片已保存为 py_captured_image.jpg")

    cap.release()  # 释放摄像头资源

def on_press(key):
    """监听键盘事件"""
    if not is_locked():  # 只有在锁屏状态下才拍照s
        capture_image()
        exit()

# 启动键盘监听
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()  # 保持监听状态 keep

    # waitkey只能监听gui有窗口事件 所以不显示窗口还是使用监听器 
    # with 语句的目的是确保监听器的生命周期在代码块内自动管理，也就是在代码块执行完毕后，自动停止监听并释放相关资源。
    # listener.join() 使得程序保持运行，直到键盘监听器的任务完成（例如，当你按下某个键来停止监听）。

