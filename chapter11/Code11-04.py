inFp = None
inList, inStr = [], ""

inFp = open("C:/Users/cyci1234/Documents/pythonfile/data1.txt", "r", encoding="utf-8")

inList = inFp.readlines()
for inStr in inList :
    print(inStr, end="")

inFp.close()