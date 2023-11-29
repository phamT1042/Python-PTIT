t = int(input())
while t > 0:
    t -= 1
    a = input().split(".")
    if len(a) != 4:
        print("NO")
    else:
        try:
            if 0 <= int(a[0]) < 256 and 0 <= int(a[1]) < 256 and 0 <= int(a[2]) < 256 and 0 <= int(a[3]) < 256:
                print("YES")
            else:
                print("NO")
        except:
            print("NO")