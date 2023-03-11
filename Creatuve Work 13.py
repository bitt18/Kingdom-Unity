l=[{1,2},{2,4},{1,3},{3,6},{6,5},{5,4},{3,5},{2,5}]
s={1,4}
count=0
l1={}
a=s-{4}
x=max(a)
print(x)
def way(x):
    s1=set()
    for road in l:
        if x in road:
            y=road-{x}
            if max(y) not in l1:
                l1.add(x)
                s1.update(y)
                print(s1)
    return(s1)
s=way(x)
print(l1)
while(s!=set()):
    for i in s:
        s=way(i)
        print(s)
        if(4 in s):
            count=count+1
print("Count=", count)



