from tkinter import *
from tkinter.ttk import *
import macro

def confirm():
    in_text = input2_1.get()
    lab.configure(text=in_text)



root = Tk()
root.title("urmall Macro")
root.geometry("700x600")
root.resizable(False, False)

frame = Frame(root)
frame.pack()

input0_0 = Label(frame, text="근무자", width=20)
input0_0.grid(row=0,column=0)

input0_1 = Entry(frame, width=30)
input0_1.grid(row=0,column=1)

input1_0 = Label(frame, text="인원", width=20)
input1_0.grid(row=1,column=0)

input1_1 = Entry(frame, width=30)
input1_1.grid(row=1,column=1)

input2_0 = Label(frame, text="특이사항", width=20)
input2_0.grid(row=2,column=0)

default = '특이사항 없음'
input2_1 = Entry(frame, width=30, textvariable=default)
input2_1.grid(row=2,column=1)

combo = Combobox(root)
combo['values'] = ('A조', 'B조','C조','D조','수동')
combo.current(0)
combo.pack()

lab = Label(root, text=default, width=20)
lab.pack()

confirm = Button(root, text="확인", command=confirm)
confirm.pack()

root.mainloop()