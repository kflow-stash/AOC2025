input_ = open("data/day2.txt", "r").read().split(",")

id_sum = 0
for ix, ids in enumerate(input_):
    print(ix)
    id1, id2 = ids.split("-")
    for x in range(int(id1), int(id2) + 1):
        id = str(x)
        split = 1
        while split <= len(id) // 2:
            if len(id) // split == len(id) / split:
                n_splits = len(id) // split
                parts = [id[iy * split : (iy + 1) * split] for iy in range(n_splits)]
                if len(set(parts)) == 1:
                    id_sum += x

                    break
            split += 1


print(id_sum)
