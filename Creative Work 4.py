s=input()
pattern = input()
count = 0
for i in range(len(pattern)):
    for j in range(i,len(s)):
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
            while(True):
                if(s[j]==pattern[i]):
                    i = i + 1
                    j = j + 1
                    continue
                else:
                    break
        else:
            continue
if (count == 0):
    print("Complete Match")
else:
    print("Not a match")