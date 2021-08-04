with open('AD2') as f:
    lines = f.readlines()

nums = [(line.strip()) for line in lines]
validpw = 0

for i in range(len(nums)):

    lister = nums[i]
    numlist = lister.split()
    numrange = numlist[0].split('-')
    character = numlist[1][0]
    lowcount = int(numrange[0])
    uppercount = int(numrange[1])
    charlist = numlist[2]

    if character[0] in numlist[2]:
        if character == charlist[lowcount - 1] and character != charlist[uppercount - 1]:
            validpw += 1
        elif character != charlist[lowcount - 1] and character == charlist[uppercount - 1]:
            validpw += 1


print("valid", validpw)
