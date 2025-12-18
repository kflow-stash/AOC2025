fresh, avail = open("data/day5.txt","r").read().split("\n\n")



fresh_rngs = []
for rng in fresh.split("\n"):
    fresh_rngs.append([int(x) for x in rng.split("-")])
    
print(fresh_rngs)
    
fresh_cnt = 0
for item in [int(x) for x in avail.split("\n")]:
    for rng_ in fresh_rngs:
        if item >= rng_[0] and item <= rng_[1]:
            fresh_cnt+=1
            break
            
print(fresh_cnt)