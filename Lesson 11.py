# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
# d = int(input("d = "))
# res = 0
# num = [a,b,c,d]
# print(num[1])
#
# # for el in num:
# #     if el > 0:
# #         res += 1
# #
# # # for i in range(4):
# # #     if num[i] > 0:
# # #         res += 1
# #
# # print(res)

# nums = [0, 0, 0, 1, 1, 0, 1, 0, 1, 1]
# count0 = 0
# for el in nums:
#     if el == 0:
#         count0 += 1
#
# i = 0
# count01 = 0
# while nums[i] == 0:
#     count01 += 0
#     i += 1

import random
# print(random.randint(0, 10))

# l = 10 # int(input("l = "))
# nums = [random.randint(10, 100) for i in range(l)]
# # for i in range(l):
# #     nums.append(random.randint(0, 10))
# print(nums)
# maxValue = nums[0]
# for el in nums:
#     if el > maxValue:
#         maxValue = el
# print(maxValue)
#
# maxValue = nums[0]
# maxI = 0
# for i in range(len(nums)):
#     if nums[i] > maxValue:
#         maxValue = nums[i]
#         maxI = i
# print(maxI)
#
# print(max(nums))
# print(nums.index(max(nums)))



# nums[1] = 999
# print(nums)
# print(len(nums))



# s = "mama"
# for i in s:
#     print(i)


# print(nums)
# print(nums.index(7))
# print(nums.count(7))
# nums.append(100)
# print(nums)
# nums.remove(1)
# print(nums)
# nums.reverse()
# print(nums)
# nums.insert(4, 999)
# print(nums)
# nums.pop(1)
# print(nums)


l = 10 # int(input("l = "))
nums = [random.randint(1, 10) for i in range(l)]
print(nums)
# imax = 0
# imin = 0
# for i in range(len(nums)):
#     if nums[i] > nums[imax]:
#         imax = i
#     if nums[i] < nums[imin]:
#         imin = i
#
# s = 0
# a = imin if imax > imin else imax
# b = imax if imax > imin else imin
#
# for i in range(a+1, b):
#     s += nums[i]
# print(s)

# t = nums[0]
# nums[0] = nums[len(nums) - 1]
# nums[len(nums) - 1] = t
# print(nums)
#
# print(sum(nums[1:4]))

even = [el for el in nums if el % 2 == 0]
# for el in nums:
#     if el % 2 == 0:
#         even.append(el)
print(even)