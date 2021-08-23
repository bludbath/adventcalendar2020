with open('Day3input.txt') as f:
    map = f.readlines()
    map = [ line.strip() for line in map]

treecounter = 0
hill, slope = 0,0

while hill < len(map):

    mountain = map[hill][slope % len(map[hill])]
    if mountain == '#':
            treecounter += 1

    hill += 1
    slope += 3
    
print(treecounter)
