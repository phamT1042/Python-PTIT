import sys

res, save, sign = [], [], ['.', '?', '!']
for line in sys.stdin:
    for var in line.split():
        save.append(var)
add = ""
for string in save:
    if string[-1] != '.' and string[-1] != '?' and string[-1] != '!':
        if len(add) == 0: string = str(string).title()
        else: string = str(string).lower()
        add += string + " "
    else:
        add += str(string)[:len(string) - 1].lower()
        res.append(add)
        add = ""
for x in res: print(x)