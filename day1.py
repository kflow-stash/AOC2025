import os

input_ = open("data/day1_pt1.txt","r").read().split("\n")

last_direct = "R"
last_loc = 0
loc = 50
zeros=0
skip = False
for x in input_:
    direct_ = x[0]
    steps_ = int(x[1:])
    
    if direct_ == "L" and loc == 0:
        stop_here = 1
        zeros-=1
    
    
    steps_ = steps_ if direct_ == "R" else -steps_
    loc += steps_
    passes = loc // 100
    
    if loc == 0:
        zeros+=1
        
    # account for passing and landing on 0 when going left
    if loc % 100 ==0 and loc < 0:
        zeros+=1
    
    loc = loc - (100*passes)
    
    zeros += abs(passes)




print(zeros)
    
    

