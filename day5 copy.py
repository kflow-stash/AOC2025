fresh, avail = open("data/day5.txt","r").read().split("\n\n")


fresh_rngs = []
for rng in fresh.split("\n"):
    fresh_rngs.append([int(x) for x in rng.split("-")])
    
fresh_orig = fresh_rngs.copy()    

combined_count = 1
it = 0
while combined_count >0:
    it+=1
    print(it, len(fresh_rngs))
    known_ranges = [fresh_rngs[0]]
    combined_count = 0
    for ix, rng in enumerate(fresh_rngs):
        added = False
        
        if ix >0:
            for iy in range(len(known_ranges)):
                rng2 = known_ranges[iy]
                overlap_start = max(min(rng),min(rng2))
                overlap_end = min(max(rng),max(rng2))
                if overlap_end >= overlap_start:
                    rng2 = [min(rng[0],rng2[0]),max(rng[1],rng2[1])]
                    known_ranges[iy]=rng2
                    added = True
                    combined_count += 1


            if not added:
                known_ranges.append(rng)
                
    fresh_rngs = known_ranges.copy()

print(sum([x[1]-x[0]+1 for x in fresh_rngs]))
                

        
    