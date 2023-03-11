cities,noofroads,cost=map(int,input().split())
roadlist=[]
shieldcity=set()
for i in range(noofroads):
    roadindex=a=list(map(int,input().split()))
    roadlist.append(roadindex)
print(roadlist)
roadlist1=roadlist
for i in range(cities):
    count=0
    for road in roadlist:
        for city in road:
            if(i==city):
                count=count+1
                roadlist1.remove(road)
    if(count>1):
        shieldcity.add(i)
print(shieldcity)


