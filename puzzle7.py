def test(nums):
    return all([sum(nums[:i])==i for i in range (len(nums))])
nums=[1,1,1,1,1]
print(nums)
print(test(nums))