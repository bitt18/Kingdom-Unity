l=[{1,4},{1,2},{2,4},{1,3},{3,6},{6,5},{5,4},{3,5},{2,5}]
s={1,4}
l1={1}
a=s-{4}
x=max(a)
print(x)
def way(x):
    s1=set()
    for road in l:
        if x in road:
            l1.add(x)
            y=road-{x}
            s1.update(y)
            print(s1)
    return(s1)
s=way(x)
print(l1)


