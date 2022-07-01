import time

a = 100
list = [i for i in range(1,a)]+[-int(j) for j in range(-a, 1)]

while True:
    list.append(list.pop(0))
    print(((list[0])*"~").center(a), end = "\r")
    time.sleep(0.01)