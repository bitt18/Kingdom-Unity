s=input()
pattern = input()
count = 0
i=0
while(i<len(pattern)):
    for j in range(i,len(s)):
        if(i<len(pattern)):
            if (pattern[i] == s[i]):
                break
            elif (pattern[i] == "?"):
                break
            elif (pattern[i] == "*"):
                for k in range(i + 1, len(pattern)):
                    if (pattern[k] == "*"):
                        i = i + 1
                        continue
                    else:
                        i = i + 1
                        break
            if (s[j] == pattern[i]):
                while(i<len(pattern) and j<len(s)):
                    if(s[j]==pattern[i]):
                        i = i + 1
                        j = j + 1
                        continue
                    else:
                        break
            else:
                continue
    i=i+1
if (count == 0):
    print("Complete Match")
else:
    print("Not a match")