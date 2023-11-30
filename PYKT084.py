from collections import OrderedDict

myDict, start, saveStr = OrderedDict(), 1, None
for _ in range(int(input())):
    if start:
        start, saveStr = 0, input()
        myDict[saveStr] = 0
    else:
        if not len(input()):
            start = 1
        else:
            myDict[saveStr] += 1
for key in myDict:
    print("{}: {}".format(key, myDict[key]))