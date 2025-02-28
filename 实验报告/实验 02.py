# 字符串操作
# 任务1：拼接并修改字符串
str1 = "I am learning"
str2 = "Python"
result = (str1 + " " + str2).upper()   # 拼接并转换为大写
print(result)

# 任务2：字符串切片
str3 = "Data Analysis"
part1 = str3[:4]   # 提取"Data"
part2 = str3[5:]   # 提取"Analysis"
print(part1, part2)

# 任务3：字符串查找与替换
# text = input("请输入一段文本：")   # 输入文本：Python是一门很棒的编程语言，Python简单易学。
# sensitive_word = input("请输入需要替换的敏感词: ")   # 输入敏感词：Python
# index = text.find(sensitive_word)
# print(f"Position of sensitive_word: {index}")
# new_str = text.replace(sensitive_word, "***")
# print(f"替换后的文本:{new_str}")

# 列表操作
# 任务1：学生成绩管理
# 学生成绩列表
grades = [95, 88, 76, 84, 92, 89, 100, 65]

# 计算总分
total_score = sum(grades)
print(f"总分：{total_score}")

# 计算平均分
average_score = total_score / len(grades)
print(f"平均分：{average_score:.2f}")

# 找出最高分和最低分
highest_score = max(grades)
lowest_score = min(grades)
print(f"最高分：{highest_score}")
print(f"最低分：{lowest_score}")

# 任务2：筛选偶数
# 数值列表
numbers = [10, 15, 20, 25, 30]
# 筛选偶数
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # 输出: [10, 20, 30]

# 任务3：商品库存管理系统
# 创建两个仓库的商品列表并合并
# 创建仓库1的商品列表（电子产品）
warehouse1 = ["iPhone 16", "iPad Pro", "MacBook Air"]
# 创建仓库2的商品列表（配件）
warehouse2 = ["AirPods", "Magic Mouse", "Apple Pencil", "AirPods", "AirPods"]

# 合并两个仓库的商品列表
all_products = warehouse1 + warehouse2
print("合并后的库存列表:", all_products)
print("库存总数:", len(all_products))

# 新增商品到库存末尾
all_products.append("Apple Watch")
print("添加新商品后的列表:", all_products)

# 删除索引为2的过时商品（MacBook Air）
del all_products[2]
print("删除过时商品后的列表:", all_products)

# 统计"AirPods"的数量
airpods_count = all_products.count("AirPods")
print("AirPods的库存数量:", airpods_count)

# 查找"iPad Pro"首次出现的位置
ipad_index = all_products.index("iPad Pro")
print("iPad Pro的首次位置索引:", ipad_index)

# 元祖操作
# 任务1：日期处理
date = ()

# 输入日期
# year = int(input("请输入年份："))   # 输入年份：2025
# month = int(input("请输入月份："))   # 输入月份：3
# day = int(input("请输入日期："))   # 输入日期：1

# date = (year, month, day)  # 存储为元组

# 输出日期
# print(f"日期：{date[0]}年{date[1]}月{date[2]}日")

# 字典操作
# 任务1：书籍信息管理
# 创建书籍信息字典
book = {
    "title": "Python数据分析基础",
    "author": "余本国",
    "price": 39.00,
    "publisher": "人民邮电出版社"
}
# 输出书名和作者
print("书名:", book["title"])
print("作者:", book["author"])
pages = book.get("pages", "未知")   # 若键不存在，返回默认值
print("页数:", pages)

# 添加页数信息
book["pages"] = 180
print("添加页数后：", book)
# 出版社信息修改
book["publisher"] = "清华大学出版社"

# 集合操作
# 任务1：朋友关系分析
# 两个朋友圈
friends_a = {"张三", "李四", "王五"}
friends_b = {"李四", "王五", "找六", "孙七"}

# 共同好友
common_friends = friends_a & friends_b
print("共同好友:", common_friends)  # 输出: {'李四', '王五'}
# 独自好友
unique_friends_a = friends_a - friends_b
unique_friends_b = friends_b - friends_a
print("A独有好友:", unique_friends_a)  # 输出: {'张三'}
print("B独有好友:", unique_friends_b)  # 输出: {'找六', '孙七'}
