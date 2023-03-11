noofroads=8
l=[{1,2},{2,4},{1,6},{2,3},{0,6},{4,5},{0,7},{5,6}]
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
                print(i,j,p)
                check1.append({i,j})


