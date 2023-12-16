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
#đọc dòng trong file chú ý rstrip('\n')
#output = open("ten file", "w")

#from sys import setrecursionlimit
#setrecursionlimit(10 ** 6)

#Đổi số cơ số 2 sang 10: num_oct = int(num_bin, 2)
#Đổi cơ số 10 sang 2: num_bir (str[2:]) = bin(num_oct)
#Đổi số sang kí tự chữ cái: char = chr(num + 65) (0 -> 'A') | char = chr(num + 97) (0 -> 'a')
#Đổi kí tự sang mã ASCII: ord()

#from bisect
#lower_bound: bisect_left | upper_bound: bisect_right
#Hàm tính biểu thức dạng string: eval(s)

#use stack or queue with deque:
#from collections import deque
#add: q.append() | pop_top (stack): q.pop() | pop_queue (queue): q.popleft()
#OrderedDict giữ thứ tự phần tử thêm vào
#from queue import PriorityQueue
# q.put() | q.queue[0]: ptu đầu priorityqueue | q.get(): pop ra ptu đầu

#format 2 số phần thập phân: "{0:.2f}".format(n) | ("%.2f" % n)
#format mã: "MS{:02}".format(ma)
#Trung bình tổng dãy số n phần tử, làm tròn 1 số phần thập phân: round(((sum / n.0) * 10) / 10.0, 1)
#trick làm tròn với 2 số phần thập phân: '{:.2f}'.format(n + 0.001)

#diff date: 
#from datetime import datetime
#(datetime.strptime(end, "%d/%m/%Y") - datetime.strptime(start, "%d/%m/%Y")).days + 1