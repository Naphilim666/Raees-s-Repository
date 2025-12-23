lst = [1, [2, [3, 4], 5], 6]
sum = 0
for i in lst:
    if type(i) is int:
        sum += i
    else:
        for a in i:
            if type(a) is int:
                sum += a
            else:
                for b in a:
                    if type(b) is int:
                        sum += b
print(sum)