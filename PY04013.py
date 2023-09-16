def convert(time):
    hours, minutes = int(time[:2]), int(time[3:])
    return hours * 60 + minutes

class TramDo:
    ma = 1
    def __init__(self, name, sumTime, sumMua):
        self.__ma = "T0" + str(TramDo.ma)
        self.__name = name
        self.__sumTime = sumTime
        self.__sumMua = sumMua
        TramDo.ma += 1
    
    def __str__(self):
        return ("%s %s %.2f" % (self.__ma, self.__name, (self.__sumMua * 60 / self.__sumTime)))
    
    def addTime(self, bd, kt):
        self.__sumTime += convert(kt) - convert(bd)
    
    def addMua(self, mua):
        self.__sumMua += mua

    def getName(self):
        return self.__name

if __name__ == '__main__':
    saveTram = []
    for _ in range(int(input())):
        name = input()
        check = 0
        for tram in saveTram:
            if tram.getName() == name:
                tram.addTime(input(), input())
                tram.addMua(int(input()))
                check = 1
                break
        
        if not check:
            saveTram.append(TramDo(name, abs(convert(input()) - convert(input())), int(input())))
    
    for i in saveTram: print(i)