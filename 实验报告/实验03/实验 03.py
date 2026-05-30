# 条件控制
# 温度单位转化工具
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
    print("单位输入错误！")


# 电商促销策略
# 案例：根据用户等级和购物金额制定折扣策略
user_level = input("请输入用户等级：")   # 输入用户等级"VIP"、"普通会员"、"非会员"
order_amount = float(input("请输入购物金额："))   # 输入购物金额
# 判断用户等级和购物金额，制定折扣策略
if user_level == "VIP":
    if order_amount > 1000:
        discount = 0.8
    else:
        discount = 0.85
elif user_level == "普通会员":
    discount = 0.9
else:
    discount = 0.95
# 输出用户的折扣和折扣后的金额
print(f"用户的折扣是：{discount * 10} 折，折扣后的金额是：{order_amount * discount:.2f} 元")

# 用户行为分析
active_days = [3, 5, 7, 2, 6, 4, 1]

# 1. 计算平均活跃天数
average_days = sum(active_days) / len(active_days)
print("平均活跃天数：", average_days)

# 2. 找出连续活跃超过5天的用户
# 假设列表中每个数对应一个用户（用户编号从1开始）
print("\n连续活跃超过5天的用户：")
for index, days in enumerate(active_days):
    if days >= 5:
        print(f"用户 {index + 1}：连续活跃 {days} 天")

# 3. 统计不同活跃等级用户数量
inactive_count = 0  # 活跃天数 < 3 天
normal_count = 0    # 3 <= 活跃天数 <= 5
active_count = 0    # 活跃天数 > 5

for days in active_days:
    if days < 3:
        inactive_count += 1
    elif 3 <= days <= 5:
        normal_count += 1
    else:  # days > 5
        active_count += 1

print("\n活跃等级统计：")
print(f"不活跃（<3天）： {inactive_count} 人")
print(f"一般（3-5天）： {normal_count} 人")
print(f"活跃（>5天）： {active_count} 人")

# 股票价格波动监控
import random

# 初始股票价格
price = 50.0
# 统计天数
days = 0

print("股票价格波动监控开始...")
print(f"初始价格：{price}元")

# 使用无限循环，每天更新股票价格
while True:
    days += 1
    # 计算每天的波动比例，范围在 -3% 到 +5% 之间
    percent_change = random.uniform(-0.03, 0.05)
    # 更新股票价格
    price = price * (1 + percent_change)

    # 输出当天的波动情况
    print(f"第{days}天: 变化率: {percent_change:.2%}, 当前价格: {price:.2f}元")

    # 检查是否触发预警或卖出条件
    if price < 40:
        print(f"警告：股票价格跌破40元！达到条件所需天数：{days}")
        break
    elif price > 60:
        print(f"提示：股票价格超过60元，建议卖出！达到条件所需天数：{days}")
        break

# 异常处理
# 用户输入验证
import math

class NegativeInputError(Exception):
    pass

while True:
    try:
        num = float(input("请输入一个非负数: "))
        if num < 0:
            raise NegativeInputError("输入错误：请输入非负数！")
        print(f"{num} 的平方根是 {math.sqrt(num):.2f}")
        break
    except ValueError:
        print("输入错误：请输入数字！")
    except NegativeInputError as e:
        print(e)


# 简易 ATM 机模拟
balance = 1000
while True:
    print("\n1. 存款 | 2. 取款 | 3. 查询余额 | 4. 退出")
    choice = input("请选择操作: ")
    if choice == "1":
        # 存款操作
        try:
            amount = float(input("请输入存款金额: "))
            if amount < 0:
                print("存款金额不能为负数！")
                continue
        except ValueError:
            print("输入错误，请输入一个有效的数字！")
            continue
        balance += amount
        print(f"存款成功，当前余额: {balance:.2f}元")
    elif choice == "2":
        # 取款操作
        try:
            amount = float(input("请输入取款金额: "))
            if amount < 0:
                print("取款金额不能为负数！")
                continue
        except ValueError:
            print("输入错误，请输入一个有效的数字！")
            continue
        if amount > balance:
            print("余额不足，无法取款！")
            continue
        balance -= amount
        print(f"取款成功，当前余额: {balance:.2f}元")
    elif choice == "3":
        # 查询余额
        print(f"当前余额: {balance:.2f}元")
    elif choice == "4":
        # 退出程序
        print("感谢使用，再见！")
        break
    else:
        print("无效输入，请重新选择！")
