# 1. 输入购买金额（原价）
price = float(input("请输入购买金额（原价）："))

# 5. 若金额 <= 0，输出 输入错误 提示
if price <= 0:
    print("购买金额输入错误")

# 2. 输入会员等级
level = int(input("请输入会员等级（0=非会员 / 1=普通会员 / 2=VIP）："))

description = ""
final_price = 0.0

# 3. 结合嵌套判断计算折扣
if level == 0:  # 非会员
    # 非会员：满300减30 / 满500减80 / 满1000减200
    if price >= 1000:
        final_price = price - 200
        description = "非会员满1000减200"
    elif price >= 500:
        final_price = price - 80
        description = "非会员满500减80"
    elif price >= 300:
        final_price = price - 30
        description = "非会员满300减30"
    else:
        final_price = price
        description = "非会员不满300无优惠"

elif level == 1:  # 普通会员
    # 普通会员：享受 9 折
    final_price = price * 0.9
    description = "普通会员享受 9 折"
    
elif level == 2:  # VIP会员
    # VIP会员：享受 8 折，另满500额外减50
    # 这里的满500通常指原价
    base_discounted = price * 0.8
    if price >= 500:
        final_price = base_discounted - 50
        description = "VIP会员享受 8 折，满500额外减50"
    else:
        final_price = base_discounted
        description = "VIP会员享受 8 折"

else:
    print("会员等级输入错误") # 等级无效

# 4. 输出原价、折扣方案说明、实付金额
print(f"原价：{price:.2f}")
print(f"折扣方案说明：{description}")
print(f"实付金额：{final_price:.2f}")
