import os

input_ = open("data/day3.txt","r").read().split("\n")


total_ = 0
for row in input_:
    nums = [int(x) for x in row]
    mx1 = max(nums[:-1])
    ix1 = nums.index(mx1)
    nums = nums[ix1+1:]
    mx2 = max(nums)

    total_ += int(str(mx1) + str(mx2))
    print(ix1,int(str(mx1) + str(mx2)))
    
print(total_)
    