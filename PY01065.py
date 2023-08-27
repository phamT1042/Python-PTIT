from sys import stdin, stdout

add = []
minus = []
pos_not_fill = []
math = ""

def sinh():
    global add, minus
    for i in range(10, 90):
        for j in range(10, 100 - i):
            add.append(f"{i} + {j} = {i + j}")
    for i in range(20, 100):
        for j in range(10, i - 10 + 1):
            minus.append(f"{i} - {j} = {i - j}")

def check(ex):
    global math, pos_not_fill
    for x in pos_not_fill:
        if math[x] != ex[x]:
            return False
    return True

def main():
    global add, minus, pos_not_fill, math
    sinh()
    t = int(stdin.readline())
    for _ in range(t):
        math = input()
        sign = math[3]
        if sign == '/' or sign == '*':
            print("WRONG PROBLEM!")
        else:
            pos_not_fill = [i for i in range(12) if math[i] != '?']
            flag = 0
            if sign == '+':
                for x in add:
                    if check(x):
                        print(x)
                        flag = 1
                        break
            elif sign == '-':
                for x in minus:
                    if check(x):
                        print(x)
                        flag = 1
                        break
            else:
                for x in add:
                    if check(x):
                        print(x)
                        flag = 1
                        break
                if flag == 0:
                    for x in minus:
                        if check(x):
                            print(x)
                            flag = 1
                            break
            if flag == 0:
                print("WRONG PROBLEM!")

    add.clear()
    minus.clear()
    pos_not_fill.clear()

if __name__ == "__main__":
    main()
