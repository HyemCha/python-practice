from tkinter import *
import sqlite3
def loadImage(fname):
    global inImage, XSIZE, YSIZE
    con, cur = None, None
    row, col, data, sql = 0,0,0,''
    con = sqlite3.connect('../pythonDB/rawDB')
    cur = con.cursor()
    fp = open(fname, 'rb')
    for row in range(0, XSIZE):
        for col in range(0, YSIZE):
            data = int(ord(fp.read(1)))
            sql = "INSERT INTO rawTable VALUES(" + str(row) + "," + str(col) + "," + str(data) + ")"
            cur.execute(sql)

    fp.close()
    con.commit()
    con.close()

def loadDatabase():
    global inImage, XSIZE, YSIZE
    con, cur = None, None
    row, col, data = 0, 0, 0
    record = None
    con = sqlite3.connect('../pythonDB/rawDB')
    cur = con.cursor()
    cur.execute('select * from rawTable')

    for i in range(0, XSIZE):
        tmpList = []
        for k in range(0, YSIZE):
            data = 0
            tmpList.append(data)
        inImage.append(tmpList)

    while(True):
        record = cur.fetchone()
        if record == None:
            break;
        row = record[0]
        col = record[1]
        data = record[2]
        inImage[row][col] = data

    con.close()

def displayImage(image):
    global XSIZE, YSIZE
    rgbString = ""
    for i in range(0, XSIZE):
        tmpString = ""
        for k in range(0, YSIZE):
            data = image[i][k]
            tmpString += "#%02x%02x%02x " % (data, data, data)
        rgbString += "{" + tmpString + "} "
    paper.put(rgbString)

# 전역변수
window, canvas, XSIZE, YSIZE = None, None, 256,256
inImage = []

if __name__ == '__main__':
    window = Tk()
    window.title("RAW-->DB")
    canvas = Canvas(window, height = XSIZE, width=YSIZE)
    paper = PhotoImage(width=XSIZE, height=YSIZE)
    canvas.create_image((XSIZE / 2, YSIZE / 2), image = paper, state = "normal")

    # 테이블 초기화
    con = sqlite3.connect('../pythonDB/rawDB')
    cur = con.cursor()
    cur.execute('drop table if exists rawTable')
    cur.execute('create table rawTable(row int, col int, data int)')
    con.commit()
    con.close()

    filename = '../image/RAW/lena.raw'
    loadImage(filename)
    loadDatabase()
    displayImage(inImage)

    canvas.pack()
    window.mainloop()