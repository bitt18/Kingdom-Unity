l=[{1,2},{2,4},{1,6},{2,3},{2,6},{4,5},{4,7},{5,6}]
l1 = set()
s2=set()

def fun(x,c2):
    for road in l:
        if x in road:
            y = road - {x}
            if max(y)!=c2 and max(y) not in l1:
                l1.add(x)
                s2.add(max(y))
    return (s2-l1)


def yoyo(ans,c1):
    print(ans)
    c2=c1
    for i in ans:
        temp=fun(i,c2)
    print(temp)
    return temp
def big(a,b,c):
    count=0
    ans={a}
    c1=c
    while(True):
        temp=yoyo(ans,c1)
        if(b in temp):
            count=count+1
            break
        if(ans==temp):
            break
        ans=temp
    return(count)


temp2=big(1,4,2)
print(temp2)