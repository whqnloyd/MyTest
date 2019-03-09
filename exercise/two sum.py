def twoSum(self, nums, target):
    dic = {}
    for i, num in enumerate(nums):
        if num not in dic:
            dic[target - num] = i
        else:
            return dic[num], i
    # loc1 = 0
    # loc2 = 0
    # for i in nums:
    #     loc2 = nums[loc1+1:].index(target-i)+loc1+1
    #
    #     # loc2 = nums.index(target - i)
    #     # if loc1 == loc2:
    #     #     loc1 = loc1 + 1
    #     #     continue
    #
    #         return loc1, loc2
    #     except:
    #         loc1 = loc1 + 1
    #         continue

print(twoSum(None,[3,3,3,6,9,11],15))