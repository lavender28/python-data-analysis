temp = float(input("请输入温度值: "))   # 输入温度值
unit = input("请输入单位（C/F）: ").upper()   # 输入单位并转换为大写字母
# 判断单位并进行温度转换
if unit == "C":
    f = temp * 1.8 + 32
    print(f"{temp:.2f}℃ = {f:.2f}℉")   # 输出转换后的温度
elif unit == "F":
    c = (temp - 32) / 1.8
    print(f"{temp:.2f}℉ = {c:.2f}℃")
else:
    print("输入错误，请输入 C 或 F")