inFp = None
inList = ""

inFp = open("C:/Users/cyci1234/Documents/pythonfile/data1.txt", "r", encoding="utf-8")

inList = inFp.readlines()
print(inList)

inFp.close()