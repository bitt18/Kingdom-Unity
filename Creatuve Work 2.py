n=int(input())
print("Enter whether the reply specifies the team (1 if it does, 2 if it does not)")
scorefor=0
scoreagainst=0
for i in range(n):
    anstype=int(input())
    print("Enter the score")
    if(anstype==1):
        scorefor, scoreagainst = map(int,input().split())
        print("YES")
        print("Chef's Team", scorefor, "Opponent Team", scoreagainst)
    elif(anstype==2):
        score1, score2 = map(int,input().split())
        if (scorefor > scoreagainst):
            max1 = scorefor
            min1 = scoreagainst
            case=1
        else:
            max1 = scoreagainst
            min1 = scorefor
            case=2
        max2 = max(score1, score2)
        min2 = min(score1, score2)
        if(min2<max1):
            if(case==1):
                scorefor=max2
                scoreagainst=min2
            else:
                scorefor=min2
                scoreagainst=max2
        elif(score1==score2):
            scorefor=score1
            scoreagainst=score1
        else:
            print("NO")
            continue
        print("YES")
        print("Chef's team", scorefor, "Opponent's team", scoreagainst)