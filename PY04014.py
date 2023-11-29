class HocSinh:
    cnt = 1
    def __init__(self, name, diem):
        self.ma = "HS{:02}".format(HocSinh.cnt)
        self.name = name
        self.diemTB = sum(diem) + diem[0] + diem[1]
        self.diemTB = round(((self.diemTB / 12.0) * 10) / 10.0, 1)

        if self.diemTB >= 9:
            self.xepLoai = "XUAT SAC"
        elif self.diemTB >= 8:
            self.xepLoai = "GIOI"
        elif self.diemTB >= 7:
            self.xepLoai = "KHA"
        elif self.diemTB >= 5:
            self.xepLoai = "TB"
        else:
            self.xepLoai = "YEU"
        HocSinh.cnt += 1
    
    def __str__(self):
        return self.ma + " " + self.name + " " + str(self.diemTB) + " " + self.xepLoai
    
    def __lt__(self, other):
        if self.diemTB == other.diemTB: return self.ma < other.ma
        return self.diemTB > other.diemTB

n = int(input())
a = []
for i in range(n):
    name = input()
    score = list(map(float, input().split()))
    a.append(HocSinh(name, score))

print(*sorted(a), sep = '\n')