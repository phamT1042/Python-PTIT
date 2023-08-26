import sys

def bandScore(n):
    if 0 < n < 3: return 1
    if 2 < n < 5: return 2.5
    if n < 7: return 3
    if n < 10: return 3.5
    if n < 13: return 4
    if n < 16: return 4.5
    if n < 20: return 5
    if n < 23: return 5.5
    if n < 27: return 6
    if n < 30: return 6.5
    if n < 33: return 7
    if n < 35: return 7.5
    if n < 37: return 8
    if n < 39: return 8.5
    return 9

for _ in range(int(sys.stdin.readline())):
    n = sys.stdin.readline().split()
    res = (bandScore(int(n[0])) + bandScore(int(n[1])) + float(n[2]) + float(n[3])) / 4
    if res % 1 >= 0.75:
        res = int(res) + 1
    elif res % 1 >= 0.25:
        res = int(res) + 0.5
    else:
        res = int(res)
    print(f"{res:.1f}")