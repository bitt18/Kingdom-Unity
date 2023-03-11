#startswith
#endswith
import math
recipe=input()
question=recipe.count("?")
ans=="YES"
for i in range(len(recipe)):
    if(recipe[i]=="?"):
        continue
    elif (recipe[i] == recipe[len(recipe) - i - 1]):
        continue
    elif(recipe[len(recipe)-i-1]=="?"):
        question=question-1
    else:
        ans="NO"
        count=0
        break
if(ans=="YES"):
    count=math.ceil(question/2)
    count=26**(count)
print(count)