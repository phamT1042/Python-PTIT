class Student:
    def __init__(self, ma, ten, lop):
        self.__ma = ma
        self.__ten = ten
        self.__lop = lop
        self.__diemCC = 10

    def getMa(self):
        return self.__ma

    def tinhDiem(self, dd):
        for i in dd:
            if i == 'm': self.__diemCC -= 1
            elif i == 'v': self.__diemCC -= 2

        if self.__diemCC < 0: self.__diemCC = 0

    def __str__(self):
        res = self.__ma + ' ' + self.__ten + ' ' + self.__lop + ' ' + str(self.__diemCC)
        if self.__diemCC == 0: 
            res += ' ' + "KDDK"
        return res

if __name__ == "__main__":
    t = int(input())
    student_list = []

    for i in range(t):
        student_list.append(Student(input(), input(), input()))
    
    for i in range(t):
        s = input().split()
        for j in student_list:
            if s[0] == j.getMa(): j.tinhDiem(s[1])
        
    for i in student_list: print(i)



