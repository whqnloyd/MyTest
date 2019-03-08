def twoSum(self, nums, target):
    loc1 = 0
    loc2 = 0
    for i in nums:
        try:
            # loc2 = nums[loc1+1:].index(target-i)+loc1+1

            # loc2 = nums.index(target - i)
            # if loc1 == loc2:
            #     loc1 = loc1 + 1
            #     continue

            return loc1, loc2
        except:
            loc1 = loc1 + 1
            continue

print(twoSum(None,[3,2,4,6,9,11],15))