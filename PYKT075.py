input = open("SOTAY.txt", "r")
output = open("DIENTHOAI.txt", "w")

string = input.readlines()
input.close()

listDB, i, day = [], 0, ""

while i < len(string):
    pt = string[i].rstrip("\n")
    if (len(pt) == 15 and pt[7] == '/'): day = pt
    else:
        listDB.append((pt, string[i + 1].rstrip("\n"), day))
        i += 1
    i += 1

listDB.sort(key = lambda x: (x[0].split()[2], x[0].split()[0], x[0].split()[1]))

for x in listDB:
    output.write(x[0] + ": " + x[1] + " " + x[2].split()[1] + "\n")

output.close()