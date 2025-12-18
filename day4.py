import os

input_ = open("data/day4.txt","r").read().split("\n")

grid = []
for iy, row in enumerate(input_):
    row_list = []
    for ix,x in enumerate(row):
        row_list.append(x)
    grid.append(row_list)
        
print(grid)
vecs = [(0,1),(0,-1),(1,1),(1,-1),(1,0),(-1,1),(-1,-1),(-1,0)]

def count_adj(iy,ix):
    count_ = 0
    for vec in vecs:
        if iy + vec[0] >=0 and ix+vec[1] >=0 and iy + vec[0] < len(grid) and ix + vec[1] < len(grid[0]):
            

            if grid[iy + vec[0]][ix+vec[1]] == "@":
                count_+=1
        
    return count_
  
total_count= 0  
while True:
    remove_ = []
    for iy, row in enumerate(grid):
        for ix,elem in enumerate(row):
            if elem == "@":
                if count_adj(iy,ix)< 4:
                    print(iy,ix)
                    remove_.append((iy,ix))
                    total_count+=1
                    
    if len(remove_) > 0:
        for iy,ix in remove_:
            grid[iy][ix]="."
    else:
        break
                
                
print(total_count)
                
        