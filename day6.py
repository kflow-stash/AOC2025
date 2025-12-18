input_ = open("data/day6.txt","r").read().split("\n")

operations = input_[-1].split()
data = input_[:-1]

data_grid = [[int(x) for x in row.split()] for row in data]
print(len(data_grid),len(data_grid[0]))

total_val = 0
for ix in range(len(data_grid[0])):
    col_val = data_grid[0][ix]
    operation = operations[ix]
    for iy in range(1,len(data_grid)):
        if operation == "*":
            col_val *= data_grid[iy][ix]
        else:
            col_val += data_grid[iy][ix]
            
    total_val += col_val

print(total_val)
            
    
            
        
    