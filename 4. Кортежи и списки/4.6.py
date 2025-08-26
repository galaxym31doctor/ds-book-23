mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range (0, 3):
    summ = sum(mylist[i])
    prois = mylist[i][0]*mylist[i][1]*mylist[i][2]
    mylist[i].append(summ)
    mylist[i].append(prois)

print(mylist)
