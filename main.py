###solution to exercise 84 from ben stephenson's "the python workbook".

nums = input('Enter three numbers: ').split(',')
nums = [float(i) for i in nums]
nums = sorted(nums)

print(nums[1])
