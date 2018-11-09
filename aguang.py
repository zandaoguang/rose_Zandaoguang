from tkinter import *
from PIL import Image,ImageTk
import tkinter
import tkinter.messagebox


root  = Tk()
root.title('我要向你表白')
root.geometry("600x500+300+100")
cv= Canvas(root, width = 600, height =500, bg = "white")
cv.pack()
frame = Frame(root)
frame.pack()
image = Image.open("aguang.jpg")
im = ImageTk.PhotoImage(image)
cv.create_image(300,200,image = im)

def showDialogNO():
    tkinter.messagebox.showinfo(title='伤心了', message='再考虑考虑吧，不要急着回答')

def showDialogOK():
    tkinter.messagebox.showinfo( title="欧耶", message="确认过眼神，余生都是你")
    tkinter.messagebox.showinfo( title="欧耶", message="爱你,么么么么么么么哒～～～")
    root.destroy()

def showDialogEE():
    tkinter.messagebox.showinfo(title='别纠结了', message='你完了，你妈让你嫁给我')
    tkinter.messagebox.showinfo(title='别纠结了', message='你爸也是这么说的')
    tkinter.messagebox.showinfo(title='别纠结了', message='你奶奶也让你嫁给我')
    tkinter.messagebox.showinfo(title='别纠结了', message='你哥哥也同意了，你全家都同意')
    tkinter.messagebox.showinfo(title='别纠结了', message='你闺蜜说嫁给我没错')
    tkinter.messagebox.showinfo(title='别纠结了', message='你爸说不同意就打你')
    tkinter.messagebox.showinfo(title='别纠结了', message='接受现实吧，我会对你好的')
    tkinter.messagebox.showinfo(title='别纠结了', message='你都是我的人了')

def closeWindow():
    tkinter.messagebox.showerror(title='未作回应',message='小姐姐,请不要逃避!')
    return

root.protocol('WM_DELETE_WINDOW', closeWindow)
output_label0 = Label(root,text ="实话告诉你吧", font =("仿宋", 18,"bold"))
cv.create_window(20, 20, anchor=NW, window= output_label0)
output_label1 = Label(root,text ="我喜欢你很久了", font =("仿宋", 18,"bold"))
cv.create_window(30, 60, anchor=NW, window= output_label1)
output_label2 = Label(root,text ="你看着办吧", font =("仿宋", 18,"bold"))
cv.create_window(40, 100, anchor=NW, window= output_label2)
Button1 = Button(root, text="同意", font =("仿宋", 18,"bold"),width=10,height=1,command = showDialogOK)
cv.create_window(100, 420, anchor=NW, window=Button1)
Button2 = Button(root,text='考虑一下', font =("仿宋", 18,"bold"),width=10,height=1,command = showDialogEE)
cv.create_window(270, 420, anchor=NW, window=Button2)
Button3 = Button(root,text='不同意', font =("仿宋", 18,"bold"),width=10,height=1,command = showDialogNO)
cv.create_window(440, 420, anchor=NW, window=Button3)
root.mainloop()