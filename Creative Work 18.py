l=[{1,2},{2,4},{1,3},{9,6},{5,8},{5,10},{3,5},{2,5},{3,6},{6,7},{8,4}]
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


def yoyo(ans):
    print(ans)
    for i in ans:
        a = len(l1)
        if(i==4):
            count=count+1
            break
        temp=fun(i)
        b = len(l1)
    print(temp)
    return temp
ans=yoyo({1})
while(True):
    temp=yoyo(ans)
    if(4 in temp):
        count=count+1
        break
    if(ans==temp):
        break
    ans=temp