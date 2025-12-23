lst = [1, [2, [3, 2, 4], 5, 1], 6]
dic={1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
for i in lst:
    if type(i) is int:
        dic[i]=dic[i]+1
    else:
        for a in i:
            if type(a) is int:
               dic[a]=dic[a]+1
            else:
                for b in a:
                    if type(b) is int:
                       dic[b]=dic[b]+1
print(dic)