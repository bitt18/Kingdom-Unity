s=input()
pattern=input()
count=0
for i in range(len(pattern)):
    if(pattern[i]==s[i]):
        continue
    elif(pattern[i]=="?"):
        continue
    elif(pattern[i]=="*"):
        for j in range(i+1,len(pattern)):
            if(pattern[j]==*):
                i=i+1
                continue
            else:
                i=i+1
                break
    else:
        count=count+1
if(count==0):
    print("Complete Match")
else:
    print("Not a match")