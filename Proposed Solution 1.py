#Try to copy, paste and run this code on Google Colaboratory. You can use any Gmail or Google account you have :)

print("Enter cities, number of roads and cost to build one shield with spaces in between")
cities,noofroads,cost=map(int,input().split())
roadlist=[]
shieldcity=set()
print("Enter the two cities connected by a road, with a space in between. Press enter, then enter two cities connected by another road and so on") 
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
print("Cities shielded are",shieldcity)
print("Cost of shielding the cities is",len(shieldcity)*cost)


