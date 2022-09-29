inFp, outFp = None, None
inStr = ""

inFp = open("C:/Windows/win.ini", "r", encoding="utf-8")
outFp = open("C:/Users/cyci1234/Documents/pythonfile/data3.txt", "w")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("--- 파일이 정상적으로 복사됨 ---")