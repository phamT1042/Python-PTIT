class SV:
    __cnt = 1
    def __init__(self, name, diem1, diem2, diem3):
        self.__maSV = "SV{:02d}".format(SV.__cnt)
        SV.__cnt += 1

        chars = name.split()
        self.__name = ""
        for i in chars: self.__name += i.title() + " "
        self.__name = self.__name.rstrip()

        self.__score = (diem1 * 3 + diem2 * 3 + diem3 * 2) / 8

    def get_score(self):
        return self.__score

    def get_id(self):
        return self.__maSV

    def __lt__(self, other):
        return self.__score > other.__score if self.__score != other.__score else self.__maSV < other.__maSV

    def __str__(self):
        return self.__maSV + " " + self.__name + " " + '{:.2f}'.format(self.__score + 0.001)
    
n = int(input())
listSV = []
for i in range(n):
    listSV.append(SV(input(), float(input()), float(input()), float(input())))

listSV.sort()
start = 1
print(listSV[0], 1)
for i in range(1, n):
    print(listSV[i], end = ' ')
    if listSV[i].get_score() != listSV[i - 1].get_score():
        start = i + 1
    print(start)
