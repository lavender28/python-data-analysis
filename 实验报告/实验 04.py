# 判断回文数
# 回文数是指正着读和反着读都一样的数字。例如，121、12321、1234321 都是回文数。
def is_palindrome(s):
    # 去除字符串中的空格，并转换为小写
    normalized = "".join(ch.lower() for ch in s if ch != " ")
    # 检查 normalized 是否等于其反转版本
    return normalized == normalized[::-1]

input_str = "A man a plan a canal Panama"
print(is_palindrome(input_str))  # 输出: True

####################################################################################################
# 计算几何图形的面积
import math

def calc_circle_area(radius):
    """计算圆的面积：面积 = π * radius²"""
    if radius < 0:
        raise ValueError("半径不能为负数")
    return math.pi * radius ** 2

def calc_rectangle_area(length, width):
    """计算矩形的面积：面积 = 长 * 宽"""
    if length < 0 or width < 0:
        raise ValueError("长和宽不能为负数")
    return length * width

def calc_triangle_area(base, height):
    """计算三角形的面积：面积 = 0.5 * 底边 * 高"""
    if base < 0 or height < 0:
        raise ValueError("底边和高不能为负数")
    return 0.5 * base * height

def calc_area(shape, **kwargs):
    """
    根据图形类型计算面积
    参数:
      shape: 字符串，图形类型，可选 "circle", "rectangle", "triangle"
      **kwargs: 对应图形的参数：
          - circle: 需要 radius 参数
          - rectangle: 需要 length 和 width 参数
          - triangle: 需要 base 和 height 参数
    返回:
      对应图形的面积
    """
    shape = shape.lower()
    if shape == "circle":
        if "radius" not in kwargs:
            raise ValueError("计算圆面积需要提供 'radius'")
        return calc_circle_area(kwargs["radius"])
    elif shape == "rectangle":
        if "length" not in kwargs or "width" not in kwargs:
            raise ValueError("计算矩形面积需要提供 'length' 和 'width'")
        return calc_rectangle_area(kwargs["length"], kwargs["width"])
    elif shape == "triangle":
        if "base" not in kwargs or "height" not in kwargs:
            raise ValueError("计算三角形面积需要提供 'base' 和 'height'")
        return calc_triangle_area(kwargs["base"], kwargs["height"])
    else:
        raise ValueError("不支持的图形类型，请选择 circle, rectangle 或 triangle")

def main():
    while True:
        print("\n请选择要计算的图形面积：")
        print("1. 圆形")
        print("2. 矩形")
        print("3. 三角形")
        print("4. 退出")
        choice = input("请输入选项（1-4）：")

        if choice == "1":
            try:
                radius = float(input("请输入圆的半径："))
                area = calc_area("circle", radius=radius)
                print(f"圆的面积为：{area:.2f}")
            except ValueError as e:
                print("错误：", e)
        elif choice == "2":
            try:
                length = float(input("请输入矩形的长："))
                width = float(input("请输入矩形的宽："))
                area = calc_area("rectangle", length=length, width=width)
                print(f"矩形的面积为：{area:.2f}")
            except ValueError as e:
                print("错误：", e)
        elif choice == "3":
            try:
                base = float(input("请输入三角形的底边长度："))
                height = float(input("请输入三角形的高："))
                area = calc_area("triangle", base=base, height=height)
                print(f"三角形的面积为：{area:.2f}")
            except ValueError as e:
                print("错误：", e)
        elif choice == "4":
            print("退出程序，再见！")
            break
        else:
            print("无效的选项，请重新选择！")
main()

####################################################################################################
# 数据清洗与统计
# 输出说明
# 有效转换后的数值：[12.0, 5.0, 8.4, 0, 0, 7.0, 0]
# 过滤后保留的正数：[12.0, 5.0, 8.4, 7.0]
# 平均值：(12+5+8.4+7)/4 = 8.1
from functools import reduce

data = ["12", 5, "8.4", -3, "NaN", "7", None]
# 步骤1：转换为浮点数（无效值设为0）
cleaned = map(
    lambda x: float(x) if isinstance(x, (int, float)) else (float(x) if str(x).replace('.', '', 1).isdigit() else 0),
    data
)
# 步骤2：过滤非正数
filtered = filter(lambda x: x > 0, cleaned)
# 步骤3：计算平均值
sum_val, count = reduce(
    lambda acc, val: (acc[0] + val, acc[1] + 1),
    filtered,
    (0.0, 0)
)
average = sum_val / count if count > 0 else 0
print(f"平均值: {average:.2f}")  # 输出: 平均值: 8.10

####################################################################################################
# 文本分析与处理
# 拆分后的单词列表：["python", "is", "a", "powerful", ...]
# 过滤后的单词列表：["python", "powerful", "language", "easy", "learn", "python", ...]
# 词频统计结果：{"python": 3, "powerful": 1, "language": 1, ...}
# 最高频词：python（出现3次）
from functools import reduce

text = "Python is a powerful language. Python is easy to learn. Python is versatile."
stop_words = ["a", "to", "is"]
# 步骤1：拆分并转换为小写
words = text.lower().replace(".", "").split()
processed_words = map(lambda word: word.strip(), words)

# 步骤2：过滤停用词
filtered = filter(lambda word: word not in stop_words, processed_words)

# 步骤3：统计词频
word_counts = reduce(
    lambda counts, word: {**counts, word: counts.get(word, 0) + 1},
    filtered,
    {}
)

# 找出频率最高的单词
most_common = max(word_counts.items(), key=lambda x: x[1])
print(f"高频词: '{most_common[0]}' (出现次数: {most_common[1]})")

####################################################################################################
# 复杂数据转换
from functools import reduce

students = [
    {"name": "张三", "scores": [85, 90, 78]},
    {"name": "李四", "scores": [76, 88, 92]},
    {"name": "王五", "scores": [90, 95, 88]}
]
# 步骤1：计算平均分
averages = map(
    lambda student: {
        "name": student["name"],
        "scores": student["scores"],
        "average": round(sum(student["scores"]) / len(student["scores"]), 2)
    },
    students
)

# 步骤2：筛选平均分≥85的学生
filtered = filter(lambda student: student["average"] >= 85, averages)

# 步骤3：拼接名字
names_str = reduce(
    lambda acc, student: f"{acc}, {student['name']}" if acc else student["name"],
    filtered,
    ""
)
print(f"符合条件的学生: {names_str}")  # 输出: Alice, Charlie

####################################################################################################
# 银行账户管理系统设计
class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = 0.0    # 初始余额为0

    def deposit(self, amount):
        """
        存款操作
        :param amount: 存款金额，必须大于0
        """
        if amount <= 0:
            print("存款失败：金额必须为正数！")
            return
        self.__balance += amount
        print(f"存款成功：存入{amount}元，当前余额: {self.__balance:.2f}元")

    def withdraw(self, amount):
        """
        取款操作
        :param amount: 取款金额，必须大于0且不能超过余额
        """
        if amount <= 0:
            print("取款失败：金额必须大于零！")
            return
        if amount > self.__balance:
            print("取款失败：余额不足！")
            return
        self.__balance -= amount
        print(f"取款成功：取出{amount}元，当前余额: {self.__balance:.2f}元")

    def display_balance(self):
        """显示账户余额"""
        print(f"账户余额: {self.__balance:.2f}元")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate=0.03):
        """
        初始化储蓄账户
        :param account_number: 账号
        :param account_holder: 账户持有者
        :param interest_rate: 利率，默认3%
        """
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        """
        存款操作
        :param amount: 存款金额，必须大于0
        """
        if amount <= 0:
            print("存款失败：金额必须为正数！")
            return
        # 计算月利息并存入
        monthly_interest = self._BankAccount__balance * (self.interest_rate / 12)
        self._BankAccount__balance += (amount + monthly_interest)
        print(f"存款成功（含利息）:存入{amount}元，产生月利息{monthly_interest}元，当前余额: {self._BankAccount__balance:.2f}元")


# 测试代码
account1 = BankAccount("A001", "张三")
account1.deposit(1000)   # 存款成功，当前余额: 1000.00元
account1.withdraw(500)   # 取款成功，当前余额: 500.00元
account1.display_balance()  # 账户余额: 500.00元

sa = SavingsAccount("ABC12345", "李四", 0.05)
sa.deposit(1000)
sa.deposit(1000)
sa.deposit(1000)


##################################
