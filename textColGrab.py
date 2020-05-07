# Python first col python grabber


def func():
    colGrab = 0
    f = open("palomarMap.txt", "r")
    fW = open("nCol.txt", "w")
    colGrab = int(input("ColGrab: "))

    for line in f:
        temp = line
        splittemp = temp.split(",")
        fW.write(splittemp[colGrab] + "\n")

    f.close()
    fW.close()
    print("Done")

func()

