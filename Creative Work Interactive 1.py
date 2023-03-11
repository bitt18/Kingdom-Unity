listofcities=[{0,2},{1,3},{0,1},{1,5},{4,5},{2,6},{3,6},{4,7},{5,7}]
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
            break
        if(citiesconsidered==temp or temp==set()):
            break
        citiesconsidered=temp
    return(count)
print(alternatepath(1,6,5))