# https://www.youtube.com/watch?v=xZFoZvhnVTU&t=621

# ---------specification-----------
# given nums = [2,7,11,15], target = 9
# because nums[0] + nums[1]=2+7 = 9
# return [0,1]

# Notes
# python dict can be seen as a set
# use "if key in dict" to see if a key is in a dictionary
# use a seen dict to avoid traverse two times of a list
# it only available when the elements have arithmatic relations or similarity

target1 = 9
nums1 = [4, 22, 32, 42, 5]


def two_sum(target, nums):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            print([seen[target - num], i])
            return [seen[target - num], i]
        elif num not in seen:
            seen[num] = i


two_sum(target1, nums1)
