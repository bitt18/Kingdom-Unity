l=[{1,2},{2,4},{1,3},{3,6},{6,5},{5,4},{3,5},{2,5}]
def shieldcity(x,y,z):
    l1 = set()
    x = 1
    count = 0

    def fun(x):
        for road in l:
            if x in road:
                y = road - {x}
                if max(y) not in l1:
                    l1.add(x)
                    break
        return y

    a = len(l1)
    while (True):
        a = len(l1)
        y = fun(x)
        x = max(y)
        if (x == z):
            break
        if (x == y):
            count = count + 1
            break
        b = len(l1)
        if (a == b):
            break
    print(x, a)
    print(l1)
    print(count)
shieldcity(1,3,6)
