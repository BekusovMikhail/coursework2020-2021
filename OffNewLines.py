import sys


def NoNewLines(path):
    filein = open(path, "r")
    fileout = open(path + "NoNL", "w")
    for i in filein:
        if i != "\n":
            print(i, file=fileout, end="")


NoNewLines("")
