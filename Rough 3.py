cities,noofroads,cost=map(int,input().split())
l=[]
inputroad=set()
for i in range(noofroads):
    roadindex=a=set(map(int,input().split()))
    l.append(roadindex)
print(l)