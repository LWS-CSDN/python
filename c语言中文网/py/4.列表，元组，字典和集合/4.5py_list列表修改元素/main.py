#1.修改单个元素
nums=[40,36,89,2,36,100,7]
nums[2]=-26
nums[-3]=-66.2
print(nums)

#2.修改一组元素
nums = [40, 36, 89, 2, 36, 100, 7]
#修改第 1~4 个元素的值（不包括第4个元素）
nums[1: 4] = [45.25, -77, -52.5]
print(nums)

nums = [40, 36, 89, 2, 36, 100, 7]
#在4个位置插入元素
nums = [40, 36, 89, 2, 36, 100, 7]
nums[4:4] = [-77, -52.5, 999]
print(nums)

s = list("Hello")
s[2:4] = "XYZ"
print(s)

nums = [40, 36, 89, 2, 36, 100, 7]
#步长为2，为第1、3.虚拟DOM的两种创建方式、5个元素赋值
nums[1: 6: 2] = [0.025, -99, 20.5]
print(nums)