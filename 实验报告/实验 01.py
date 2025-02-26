# 计算矩形的面积和周长
length = float(input("请输入矩形的长度："))
width = float(input("请输入矩形的宽度："))
area = length * width
perimeter = 2 * (length + width)
print(f"矩形的面积为：{area:.2f}, 周长为：{perimeter:.2f}")

# 计算输入数值的平方根
num = float(input("请输入一个数值："))
sqrt_result = num ** 0.5
print(f"{num} 的平方根是：{sqrt_result:.2f}")