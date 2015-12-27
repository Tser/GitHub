#! /usr/bin/env python
# coding=utf-8
import os, fileinput


class updateFile:
    def __init__(self, pathName):
        self.pathName = pathName
        self.curFile = []
        self.curDir = []
        try:
            files = os.listdir(self.pathName)
        except Exception, e:
            print e.message
        for f in files:
            if os.path.isfile(f):
                self.curFile.append(f)
            elif os.path.isdir(f):  # 此语句，可由于扩展
                self.curDir.append(f)
            else:
                pass

    def updateFileLastName(self, sName, dName):
        if "." == sName[:1]:
            self.sName = sName
        elif "." != sName[:1]:
            self.sName = "." + sName
        else:
            pass
        if "." == dName[:1]:
            self.dName = dName
        elif "." != dName[:1]:
            self.dName = "." + dName
        else:
            pass
        # 获取到当前目录(".")下的文件文件名
        for file in self.curFile:
            if self.sName == os.path.splitext(file)[1]:
                try:
                    # 获取文件的名字：os.path.splitext(fName)[0]
                    newFile = os.path.splitext(file)[0] + self.dName
                    os.rename(file, newFile)
                    print file, "--->", newFile
                except Exception, e:
                    print e.message
            else:
                pass

    def updateFileCurrent(self):
        try:
            with open("PayLoad.csv", 'r') as f:
                lines = f.readlines()
                for line in lines:
                    oldData = line.split(",")[0]
                    newData = line.split(",")[1]
                    # print oldData, "-->", newData
                    for f in self.curFile:
                        if ".htm" == os.path.splitext(f)[1]:
                            print f, "updated"
                            for line in fileinput.input(f, inplace=True):
                                print line.rsplit().replace(oldData, newData)
                        else:
                            pass
        except Exception, e:
            print e.message

if __name__ == "__main__":
    print "Run Python2.7.10,test success"
    pathName = raw_input("curPathName:")
    updateFile(pathName).updateFileCurrent()
    os.system("color a")
    print "update over!"
