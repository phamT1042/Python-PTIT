class caThi:
    ma = 1
    def __init__(self, ngay, gio, phong):
        self.ngay = ngay
        self.gio = gio
        self.phong = phong
        self.ma = "C" + ("0" * (3 - len(str(caThi.ma)))) + str(caThi.ma)
        caThi.ma += 1

    def __str__(self):
        return self.ma + " " + self.ngay + " " + self.gio + " " + self.phong

f = open("CATHI.in", "r")
save = f.readlines()
dsCaThi = []
for i in range(1, len(save), 3):
    dsCaThi.append(caThi(save[i].rstrip('\n'), save[i + 1].rstrip('\n'), save[i + 2].rstrip('\n')))

dsCaThi = sorted(dsCaThi, key = lambda x: (x.ngay, x.gio, x.ma))

for i in dsCaThi: print(i)