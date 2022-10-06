from tkinter import *
from tkinter.filedialog import *

#함수 선언 부분
def func_open():
    global photo
    filename = askopenfilename(parent=window, filetypes=(("GIF 파일", "*.gif"),("모든 파일","*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo
    # for i in range(photo.height()):
    #     for j in range(photo.width()):
    #         r,g,b = photo.get(j,i)
    #         grey = int((r+g+b)/3)
    #         photo.put("#%02x%02x%02x" % (grey, grey, grey), (j,i))

def func_zoomIn(event):
    global photo, value
    value += 1
    photo = photo.zoom(value,value)
    pLabel.configure(image=photo)
    pLabel.image=photo

def func_zoomOut(e):
    global photo, value
    value -= 1
    photo = photo.subsample(value,value)
    pLabel.configure(image=photo)
    pLabel.image=photo

def func_exit():
    window.quit()
    window.destroy()

#메인
window = Tk()
window.geometry("500x500")
window.title("명화 감상하기")

#PhotoImage() : 이름을 가진 이미지 생성
photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand=1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)

#window.bind("<Key>", keyEvent)
value=0
window.bind("<Up>", func_zoomIn)
window.bind("<Down>", func_zoomOut)

window.mainloop()