# Nếu như tồn tại số 0, với mọi số x ta có thể tạo được mọi
# bội số (âm và dương) của x.
# VD: (0, x) => -x, 2x. (-x, x) => -3x, 3x....

# Nếu ta trừ tất cả các số trong mảng và k cho cùng 1 giá trị, kết quả không thay đổi
# VD: Ta có x0, x1, x2 và k. Giả sử 2x1 - x2 = k
# Khi đó: 2(x1 - x0) - (x2 - x0) = 2x1 - x2 = k - x0

# Ta có thể làm cho mảng tồn tại số 0 bằng cách trừ tất cả các số trong mảng đi x0. Và 
# khi đó, ta có thể tạo được bội số của tất cả các số còn lại trong mảng, hay nói cách khác
# các số có thể được tạo ra sẽ có dạng: u(xi - x0) + v(xj - x0) (1)

# Theo bổ đề Bezout: Nếu như d = gcd(a, b) với a, b là 2 số nguyên không âm
# => Luôn tồn tại 2 số nguyên x, y sao cho ax + by = d (2)

# (1)(2) => Các số có thể được tạo ra sẽ là bội số của gcd(x1 - x0, x2 - x0, ...)
# Vậy ta chỉ cần kiểm tra k - x0 có chia hết cho gcd(x1 - x0, x2 - x0, ...)
import math

for i in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    g = a[1] - a[0]
    for i in range(2, n):
        g = math.gcd(g, a[i] - a[0])

    print("NO") if (k - a[0]) % g else print("YES")