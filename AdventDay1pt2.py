with open('input') as f:
    lines = f.readlines()

nums = [int(line.strip()) for line in lines]

for i in range(len(nums)-2):
    for j in range(i + 1, len(nums)-1):
        for k in range(j + 1, len(nums)):
            num1 = nums[i]
            num2 = nums[j]
            num3 = nums[k]

            if num1 + num2 + num3 == 2020:
                total = num1 * num2 * num3

print(total)

