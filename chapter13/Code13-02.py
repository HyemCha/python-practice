import sqlite3

con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
row = None

con = sqlite3.connect("../pythonDB/maverDB.db")
cur = con.cursor()

cur.execute("SELECT * FROM userTable")

print("사용자ID    사용자이름        이메일                        출생연도")
print("-"*62)

while(True):
    row = cur.fetchone()
    if(row == None):
        break;
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%-11s  %-10s    %-25s    %d" % (data1, data2, data3, data4))

con.close()