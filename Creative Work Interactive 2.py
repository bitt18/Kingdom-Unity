cities=8
listofcities=[{1,2},{2,4},{1,6},{2,3},{0,6},{4,5},{0,7},{5,6}]
for p in range(cities):
    complement = set()
    for q in listofcities:
        if(p in q):
            r=q-{p}
            complement.add(max(r))
    print(p, complement)