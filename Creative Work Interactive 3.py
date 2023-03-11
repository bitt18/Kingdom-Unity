cities,noofroads,cost=map(int,input().split())
listofcities=[]

for i in range(noofroads):
    roadindex=a=set(map(int,input().split()))
    listofcities.append(roadindex)

shieldcity=set()

def connectedcities(startcity,c,s1,s2):
    for road in listofcities:
        if startcity in road:
            complementcity = road - {startcity}
            if max(complementcity)!=c and max(complementcity) not in s1:
                s1.add(startcity)
                s2.add(max(complementcity))
    return (s2-s1)

def alternatepath(a,b,c):
    s1 = set()
    s2 = set()
    count=0
    citiesconsidered={a}
    while(True):
        for i in citiesconsidered:
            temp = connectedcities(i, c, s1, s2)
        if(b in temp):
            count=count+1
            print("Alternate path found",a,b,c)
            break
        if(citiesconsidered==temp or temp==set()):
            break
        citiesconsidered=temp
    return(count)

for p in range(cities):
    complement = set()
    for q in listofcities:
        if(p in q):
            r=q-{p}
            complement.add(max(r))
    avoidrepitition=[]
    for i in complement:
        for j in complement:
            if({i,j} not in avoidrepitition) and (i!=j):
                count=alternatepath(i,j,p)
                if(count==0):
                    shieldcity.add(p)
                avoidrepitition.append({i,j})
print("Cities to be shielded", shieldcity)
print("Cost",len(shieldcity)*cost)