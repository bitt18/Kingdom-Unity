l=[{1,2},{2,4},{1,3},{4,6},{5,4},{3,5},{2,5},{3,6}]
l1 = set()
x = 1
count = 0
s2=set()

def fun(x):
    for road in l:
        if x in road:
            y = road - {x}
            if max(y)!=2 and max(y) not in l1:
                l1.add(x)
                s2.add(max(y))
    return (s2-l1)

def shieldcity(x):
    count=0
    y = fun(x)
    if (4 in y):
        count = count + 1
    return y

ans=shieldcity(1)
print(ans)
for i in ans:
    a = len(l1)
    if(i==4):
        break
    temp=shieldcity(i)
    b = len(l1)
print(temp)

ans=temp
for i in ans:
    a = len(l1)
    if (i == 4):
        break
    temp = shieldcity(i)
    b = len(l1)
print(temp)