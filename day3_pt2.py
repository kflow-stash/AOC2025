import os

input_ = open("data/day3.txt","r").read().split("\n")


total_ = 0
for row in input_:
    nums = [int(x) for x in row]
    jult = []
    ix1 = -1
    for ix in range(11,-1,-1):
        stop_idx = -ix if ix > 0 else None
        mx1 = max(nums[ix1+1:stop_idx])
        print(ix, mx1)
        ix1 = nums.index(mx1,ix1+1)

        jult.append(str(mx1))
    

    total_ += int("".join(jult))

    
print(total_)
    