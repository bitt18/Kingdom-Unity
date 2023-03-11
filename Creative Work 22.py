noofroads=8
l=[{1,2},{2,4},{1,6},{2,3},{0,6},{4,5},{0,7},{5,6}]

shieldcity=set()

def fun(x,c2,l1,s2):
    for road in l:
        if x in road:
            y = road - {x}
            if max(y)!=c2 and max(y) not in l1:
                l1.add(x)
                s2.add(max(y))
    return (s2-l1)


def yoyo(ans,c1,l1,s2):
    l1=l1
    s2=s2
    c2=c1
    for i in ans:
        temp=fun(i,c2,l1,s2)
    return temp
def big(a,b,c):
    l1 = set()
    s2 = set()
    count=0
    ans={a}
    c1=c
    while(True):
        temp=yoyo(ans,c1,l1,s2)
        if(b in temp):
            count=count+1
            print(a,b,c1)
            break
        if(ans==temp or temp==set()):
            break
        ans=temp
    return(count)

for p in range(noofroads):
    check = set()
    for q in l:
        if(p in q):
            r=q-{p}
            check.add(max(r))
    check1=[]
    for i in check:
        for j in check:
            if({i,j} not in check1) and (i!=j):
                ct=big(i,j,p)
                if(ct==0):
                    shieldcity.add(p)
                check1.append({i,j})
print(shieldcity)