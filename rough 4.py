noofroads=6
l=[{0,1},{1,2},{3,4},{2,4},{2,6},{5,2}]
for p in range(noofroads):
    check = set()
    for q in l:
        if(p in q):
            r=q-{p}
            check.add(max(r))
    print(p, check)