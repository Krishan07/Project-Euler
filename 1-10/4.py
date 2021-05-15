def ispal(n):
    return str(n) == str(n)[::-1]

list = []
for first in range(100, 1000):
    for second in range(100, 1000):
        i = first * second
        if ispal(i):
            list.append(i)
print(max(list))
