from collections import OrderedDict

inp = open("VANBAN.in", "r")
cnt, mxLen = OrderedDict(), 0
for data in inp:
    listStr = data.rstrip('\n').split()
    for string in listStr:
        if string == string[::-1]:
            if len(string) > mxLen:
                mxLen = len(string)
                cnt.clear()
                cnt[string] = 1
            elif len(string) == mxLen:
                try: cnt[string] += 1
                except: cnt[string] = 1
inp.close()

for key in cnt: print(key, cnt[key])
