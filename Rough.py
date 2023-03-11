l=[{1,2},{2,4},{1,3},{3,6},{5,4},{3,5},{2,5},{6,7},{5,7}]
l1 = set()
x = 1
count = 0

def fun(x):
    for road in l:
        if x in road:
            y = road - {x}
            if max(y)!=2 and max(y) not in l1:
                l1.add(x)
                s2.add(max(y))
    return (s2-l1)

while (True):
    a = len(l1)
    y = fun(1)
    if (4 in y):
        count = count + 1
        break
    b = len(l1)
    if (a == b):
        break
print(y)
print(l1)

while (True):
    a = len(l1)
    y = fun(3)
    if (4 in s2):
        count = count + 1
        break
    b = len(l1)
    if (a == b):
        break
print(y)
print(l1)

while (True):
    a = len(l1)
    y = fun(6)
    if (4 in s2):
        count = count + 1
        break
    b = len(l1)
    if (a == b):
        break
print(y)
print(l1)

while (True):
    a = len(l1)
    y = fun(5)
    if (4 in s2):
        count = count + 1
        break
    b = len(l1)
    if (a == b):
        break
print(y)
print(l1)

