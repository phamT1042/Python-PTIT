import sys

save = []
for line in sys.stdin:
    for var in line.split():
        save.append(str(var).lower())

start, end = True, True
for string in save:
    if start: string = str(string).title()
    if string[-1] == '.' or string[-1] == '?' or string[-1] == '!':
        start, end = True, True
        string = string[:len(string) - 1]
    else:
        start, end = False, False
    print(string, end = ' ')
    if end: print()