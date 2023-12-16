# import sys
# def stdin_gen():
#     for x in sys.stdin.read().split():
#         yield int(x)
# cin = stdin_gen()
# t = next(cin)

# import sys
# i = 0
# t = int(input())
# for line in sys.stdin:
#     n = int(line)
#     i += 1
#     if i == t: break

#memory with array < memory with list:
#a = array.array('i', [0] * n)

#input = open("ten file", "r")
#read all lines in file: for line in input:
#output = open("ten file", "w")

#from sys import setrecursionlimit
#setrecursionlimit(10 ** 6)

#Đổi số cơ số 2 sang 10: num_oct = int(num_bin, 2)
#Đổi số sang kí tự chữ cái: char = chr(num + 65) (0 -> 'A') | char = chr(num + 97) (0 -> 'a')
#Đổi kí tự sang mã ASCII: ord()

#from bisect
#lower_bound: bisect_left | upper_bound: bisect_right

#use stack or queue with deque:
#from collections import deque
#add: q.append() | pop_top (stack): q.pop() | pop_queue (queue): q.popleft()
