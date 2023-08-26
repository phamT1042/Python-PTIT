n = input()

def check(n):
    i = 0
    while i < len(n):
        if n[i] == '6':
            if i + 1 == len(n): return "YES"
            if n[i + 1] == '6': i += 1
            elif n[i + 1] == '8':
                if i + 2 == len(n): return "YES"
                if n[i + 2] == '8': i += 3
                else: i += 2
            else: return "NO"
        else: return "NO"

    return "YES"

print(check(n))