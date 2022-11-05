def Log(newLog):
    f=open("./log.txt", "a")
    f.write(newLog)
    f.close()
    
def errorLog(newLog):
    f=open("./errorLog.txt", "a")
    f.write(newLog)
    f.close()