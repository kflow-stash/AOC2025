input_ = open("data/day6.txt","r").read().split("\n")

operations = input_[-1].split()
data = input_[:-1]

data_grid = [[x for x in row.split()] for row in data]
row_lengths = [[len(x) for x in row] for row in data_grid]
col_lengths = [max(row[i] for row in row_lengths) for i in range(len(data_grid[0]))]

last_cl = 0
total_= 0
for ix, cl in enumerate(col_lengths):
    operation = operations[ix]
    col = [data[y][last_cl:cl+last_cl] for y in range(len(data))]
    
    nums = [int("".join([col[y][x] for y in range(len(col))])) for x in range(cl-1,-1,-1)]
    
    val = nums[0]
    for iy in range(1,len(nums)):
        if operation == "*":
            val*=nums[iy]
        else:
            val+=nums[iy]
    total_ += val

    last_cl = cl+last_cl + 1


print(total_)
