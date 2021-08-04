with open('adtest') as f:
    lines = f.readlines()

nums = [(line.strip()) for line in lines]
validpw = 0


for i in range(len(nums)):

    lister = nums[i]
    numlist = lister.split()
    numrange = numlist[0].split('-')
    lower = int(numrange[0])
    upper = int(numrange[1])
    character = numlist[1][0]
    numcount = numlist[2].count(character)

    if character[0] in numlist[2]:
        if (numcount >= lower) and (numcount <= upper):
            validpw += 1



print(validpw)