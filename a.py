# import sys
# def stdin_gen():
#     for x in sys.stdin.read().split():
#         yield int(x)
# cin = stdin_gen()

# import sys
# i = 0
# t = int(input())
# for line in sys.stdin:
#     n = int(line)
#     i += 1
#     if i == t: break

#for _ in range(int(sys.stdin.readline())):

#memory with array < memory with list

a = [2, 6, 28]
for i in range(3, 1000): a.append(6 * a[i - 1] - 4 * a[i - 2])
save = []
for i in range(0, 203):
    save.append(int(str(a[i])[-3:]))
for x in save:
    print(x)


        



