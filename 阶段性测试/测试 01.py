class Listinfo(object):
    def __init__(self, list_val):
        self.varList = list_val

    def add_key(self, key_name):
        if isinstance(key_name, (str, int)):
            self.varList.append(key_name)
            return self.varList
        else:
            return 'error'

    def get_key(self, num):
        if num >= 0 and num < len(self.varList):
            return self.varList[num]
        else:
            return 'error'

    def update_list(self, list_et):
        self.varList.extend(list_et)
        return self.varList

    def del_key(self):
        if len(self.varList) >= 0:
            return self.varList.pop(-1)
        else:
            return 'error'


list_info = Listinfo([222, 111, 'sss', '333'])
print(list_info.add_key('1111'))
print(list_info.get_key(4))
print(list_info.update_list(['1', '2', '3']))
print(list_info.del_ksey())


#####################################################################


dic = {
    "杭州市": {
        "上城区":["清波街道", "南山街道"],
        "西湖区":["灵隐街道", "湖滨街道"]},
    "温州市":{
        "鹿城区":["五马街道","滨江街道"],
        "瓯海区":["茶山街道","高教园区"]}}
a = 0
for i in dic:
    print(i)
for three in range(3):
    pn = input("请输入城市：")
    if pn in dic:
        p = dic[pn]
        c = p.keys()
        while True:
            for k in c:
                print(k)
            cn = input("请输入街区：")
            if cn in c:
                jn = dic[pn][cn]
                for l in jn:
                    print(l)
            else:
                print("城区名不存在，请重新输入：")
                continue
            qu = input("离开输入q：")
            if qu == "q":
                print("退出程序")
                break
    else:
        a = a + 1
        print("三次输入错误将退出程序，目前错误{}次！".format(a))
    continue

#####################################################################

    def input_student():
        """
        提示用户输入一个学生记录，如果用户输入 'exit' 则返回 None。
        返回值是一个字典，包含 'name', 'age', 'grade' 三个键。
        """
        name = input("请输入学生姓名（或输入 'exit' 结束录入）：")
        if name.lower() == "exit":
            return None
        try:
            age = int(input("请输入学生年龄："))
            grade = float(input("请输入学生成绩（0-100）："))
        except ValueError:
            print("输入错误：年龄必须为整数，成绩必须为数字。请重新输入该学生记录。")
            # 重新录入当前学生记录
            return input_student()

        return {"name": name, "age": age, "grade": grade}


    def calculate_average(students):
        """
        计算并返回所有学生成绩的平均值。
        """
        total = sum(student["grade"] for student in students)
        return total / len(students) if students else 0


    def get_above_average(students, average):
        """
        返回成绩高于平均成绩的学生记录列表。
        """
        return [student for student in students if student["grade"] > average]


    def print_students(students):
        """
        打印学生记录列表，每条记录包含姓名、年龄和成绩。
        """
        for student in students:
            print(f"姓名：{student['name']}, 年龄：{student['age']}, 成绩：{student['grade']:.2f}")


    def main():
        # 存储所有学生记录的列表
        students = []

        # 循环录入学生记录
        while True:
            student = input_student()
            if student is None:
                break
            students.append(student)

        # 检查是否有学生记录
        if not students:
            print("未录入任何学生记录。")
            return

        # 计算平均成绩并输出
        average = calculate_average(students)
        print("\n所有学生的平均成绩为：{:.2f}".format(average))

        # 筛选并输出成绩高于平均成绩的学生
        above_avg_students = get_above_average(students, average)
        print("\n成绩高于平均成绩的学生：")
        print_students(above_avg_students)

        # 将所有学生按成绩从高到低排序，并输出排序结果
        sorted_students = sorted(students, key=lambda x: x["grade"], reverse=True)
        print("\n按成绩从高到低排序后的学生记录：")
        print_students(sorted_students)


    main()
