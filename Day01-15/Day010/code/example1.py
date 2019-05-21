"""
nonlocal: it works in exactly the same way as the global statement, except that it is used to refer to variables that are neither global nor local to the function.
@Author:jyang
@Date:5/17/2019
"""

import tkinter
import tkinter.messagebox

def main():
    flag = True

    #修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, World!') if flag else ('blue', 'Goodbye, World!')
        label.config(text=msg, fg=color)

    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('900x160')
    # 设置窗口标题
    top.title('Life limited')
    # 创建标签对象并添加到顶层窗口
    content = 'Life is life, life is an interesting journey of ups and downs.'
    label = tkinter.Label(top, text=content, font='Arial -32', fg='green')
    label.pack(expand=1)

    # 创建一个放按钮的容器
    panel = tkinter.Frame(top)
    panel.pack(side='bottom')
    # 创建按钮对象，指定添加到哪个容器，通过command参数绑定事件回调函数
    # 注意回调函数不需要()
    btn1 = tkinter.Button(panel, text='Modify', command=change_label_text)
    btn1.pack(side='left')
    btn2 = tkinter.Button(panel, text='Out', command=confirm_to_quit)
    btn2.pack(side='right')

    tkinter.mainloop()


if __name__ == '__main__':
    main()
