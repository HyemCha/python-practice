from tkinter import *
from tkinter import messagebox

window = Tk()

def custom():
    messagebox.showinfo("title", '내용')
def custom2():
    if chk.get()==0:
        messagebox.showinfo("", "체크버튼이 꺼졌요요"+str(chk.get()))
    else:
        messagebox.showinfo("", "체크박스가 켜쳤어요"+str(chk.get()))

img = PhotoImage(file="img/qenguin.gif")
btn1 = Button(window, image=img, command=custom)

chk = IntVar()
cb1 = Checkbutton(window, text='체크버튼', variable=chk, command=custom2)

label1 = Label(window, text="text", font=("궁서체"), fg='red')

btn1.pack()
cb1.pack()
label1.pack()



window.mainloop()