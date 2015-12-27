#! /usr/bin/env python
# coding=utf-8

class updataFile:
    def __init__(self, fileName):
        self.fileName = fileName

    def clearSplaceLine(self):
        with open(self.fileName, 'r') as fr:
            outFile = fr.readlines()
        with open(self.fileName, 'w') as fw:
            for line in outFile:
                if line != "\n":
                    fw.write(line)

        fr.close()
        fw.close()


if __name__ == "__main__":
    import os
    files = []
    for f in os.listdir("."):  # 当前目录下
        if os.path.isfile(f):
            files.append(f)
    for file in files:
        if ".htm" == os.path.splitext(file)[1]:
            old = file
            updataFile(old).clearSplaceLine()
