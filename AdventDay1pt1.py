with open('input') as f:
    lines = f.readlines()

nums = [int(line.strip()) for line in lines]

for i in range(len(nums)-1):
    for j in range(i + 1, len(nums)):
        num1 = nums[i]
        num2 = nums[j]

        if num1 + num2 == 2020:
            totals = num1 * num2

print(totals)