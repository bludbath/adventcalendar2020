with open('Day3input.txt') as f:
    lines = f.readlines()
    mountain = [line.strip() for line in lines]

treecount = 0
ride = 0
drop = 0

for i in range(len(mountain) - 1):
    ride += 1
    drop += 3
    tree = mountain[ride][drop % len(mountain[ride])]

    if tree == '#':
        treecount += 1

print('treecount', treecount)
