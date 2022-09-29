inFp = None
inStr = ""

inFp = open("C:/Users/cyci1234/Documents/pythonfile/data1.txt", "r", encoding="utf-8")
i=1
while True :
    inStr = inFp.readline()
    if inStr == "":
        break;
    print("%d: %s" %(i,inStr), end="")
    i = i + 1

inFp.close()