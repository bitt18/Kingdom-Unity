cities,noofroads,cost=map(int,input().split())
roadlist=[]
shieldcity=set()
for i in range(cities):
    roadindex=a=set(map(int,input().split()))
    roadlist.append(roadindex)
for i in range(cities):
    count=0
    for road in roadlist:
        for city in road:
            if(i==city):
                count=count+1
    if(count>1):
        shieldcity.add(i)
print(shieldcity)
print(len(shieldcity)*cost)


