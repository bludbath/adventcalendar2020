with open('Day3input.txt') as f:
    map = f.readlines()
    map = [ line.strip() for line in map]


treecounter = 0
hill, slope = 0,0


while hill +1 < len(map):
    hill += 1
    slope += 3

    mountain = map[hill][slope % len(map[hill])]
    if mountain == '#':
            treecounter += 1

print(treecounter)
