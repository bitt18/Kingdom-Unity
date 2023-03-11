l=[{1,2},{2,4},{1,3},{3,6},{6,5},{5,4},{3,5},{2,5}]
l1=set()
x=1
for road in l:
    if x in road:
        y = road - {x}
        if max(y) not in l1:
            l1.add(x)
            break
x=2
for road in l:
    if x in road:
        y = road - {x}
        if max(y) not in l1:
            l1.add(x)
            break
x=4
for road in l:
    if x in road:
        y = road - {x}
        if max(y) not in l1:
            l1.add(x)
            break
x=5
for road in l:
    if x in road:
        y = road - {x}
        if max(y) not in l1:
            l1.add(x)
            break
x=6
for road in l:
    if x in road:
        y = road - {x}
        if max(y) not in l1:
            l1.add(x)
            break
x=3
for road in l:
    if x in road:
        y = road - {x}
        if max(y) not in l1:
            l1.add(x)
            break
