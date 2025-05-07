nums=input("请输入整数(用空格分开)：").split()
nums.sort()
print(f"最大值：{max(nums)}")
print(f"最小值：{min(nums)}")
print(f"求和：{sum(nums)}") #错误未修改
print(f"排序结果：{nums}")