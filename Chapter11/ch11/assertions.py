mylist = [1, 2, 3]  # this ideally comes from some place

assert 4 == len(mylist)  # this will break

for position in range(4):
    print(mylist[position])
