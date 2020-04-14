import re,os
filename = "student.txt"


def main():
    """主函数:主要用于实现系统的主页面"""
    ctrl = True       # 标记是否退出系统
    while(ctrl):
        menu()         # 显示菜单
        option = input("请选择：")   # 选择菜单项
        option_str = re.sub("\D", "", option)   # 提取数字   re.sub()函数可以匹配任意的数字，并将数字替换
        if option_str in ['0','1','2','3','4','5','6','7']:
            option_int = int(option_str)
            if option_int == 0:    # 退出系统
                print("您已退出学生信息管理系统!")
                ctrl = False
            elif option_int == 1:
                # 录入学生成绩信息
                insert()

            elif option_int == 2:
                # 查找学生成绩信息
                search()

            elif option_int == 3:
                # 删除学生成绩信息
                delete()

            elif option_int == 4:
                # 修改学生成绩信息
                modify()

            elif option_int == 5:
                # 排序
                sort()

            elif option_int == 6:
                # 统计学习总数
                total()

            elif option_int == 7:
                # 显示所有学生信息
                show()


def menu():
    # 输出菜单
    print('''
     ---------------学生信息管理系统------------
     ==================功能菜单================
                    1 录入学生信息
                    2 查找学生信息
                    3 删除学生信息
                    4 修改学生信息
                    5 排序
                    6 统计学生总人数
                    7 显示所有学生信息
                    0 退出系统
     =======================================    
                  说明:通过数字选择菜单
     =======================================
    ''')

def save(student):
    """将学生信息保存到文件"""
    try:
        student_txt = open(filename, "a")   # 以追加模式打开
    except Exception as e:
        student_txt = open(filename, "w")   # 文件不存在，创建文件并打开
    for info in student:
        student_txt.write(str(info) + "\n") # 按行存储，添加换行符
    student_txt.close()                     # 关闭文件

# 以上代码中，将以追加的模式打开一个文件，并且应用try。。。except语句捕获异常。如果出现异常，则说明没有要打开的文件，这时再以写的模式创建并打开文件，接下来通过for语句将列表中的元素一行一行写入文件中，每行结束添加换行符


def insert():
    """录入学生信息"""
    # 定义一个空列表，保存学生信息
    stdentList = []
    mark = True   # 用来判断是否继续添加
    while mark:
        id = input("请输入ID（如1001）：")
        if not id:
            break   # ID为空，跳出循环

        name = input("请输入名字：")
        if not name:
            break   # 名字为空，跳出循环

        try:
            english = int(input("请输入英语成绩："))
            python = int(input("请输入Python成绩："))
            c = int(input("请输入C语言成绩："))
        except:
            print("输入无效，不是整数值。。。请重新录入信息")
            continue

        # 将输入的学生信息保存到字典
        stdent = {"id":id, "name":name, "english":english, "python":python, "c":c}

        # 将学生信息字典添加到列表中
        stdentList.append(stdent)

        inputMark = input("是否继续添加？（y/n）:")
        if inputMark == "y":
            # 继续添加
            mark = True
        else:
            # 不继续添加
            mark = False
    save(stdentList)
    print("学生信息录入完毕")

def delete():
    """删除学生信息"""
    mark = True    # 标记是否循环
    while mark:
        studentId = input("请输入要删除的学生ID：")

        # 判断是否输入要删除的学生
        if studentId is not "":
            # 判断文件是否存在
            if os.path.exists(filename):
                # 打开文件
                with open(filename, "r") as rfile:
                    # 读取全部内容
                    student_old = rfile.readlines()
            else:
                student_old = []

            # 标记是否删除
            ifdel = False
            # 如果存在学生信息
            if student_old:
                # 以写的方式打开文件
                with open(filename, "w") as wfile:
                    d = {}
                    for list in student_old:
                        # 字符串转换字典
                        d = dict(eval(list))
                        if d['id'] != studentId:
                            # 将一条学生信息写入文件
                            wfile.write(str(d) + "\n")
                        else:
                            # 标记已删除
                            ifdel = True

                        if ifdel:
                            print("ID为 %s 的学生信息已经被删除..." % studentId)
                        else:
                            print("没有找到ID为 %s 的学生信息..." % studentId)
            else:
                # 不存在学生信息
                print("无学生信息...")
                # 退出循环
                break
            # 显示全部学生信息
            show()
            inputMark = input("是否继续删除？（y/n）:")
            if inputMark == "y":
                # 继续删除
                mark = True
            else:
                # 退出删除
                mark = False


def modify():
    """修改学生信息"""
    show() # 显示全部学生信息

    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, "r") as rfile:  # 打开文件
            student_old = rfile.readlines()  # 读取全部内容
    else:
        return
    studentid = input("请输入要修改的学生ID：")
    with open(filename, "w") as wfile: # 以只写模式打开文件
        for student in student_old:
            d = dict(eval(student))  # 字符串转字典
            if d['id'] == studentid :  # 判断是否为要修改的学生
                print("找到了这名学生的信息，可以修改他的信息")
                while True:  # 输入要修改的信息
                    try:
                        d['name'] = input("请输入姓名：")
                        d['english'] = int(input("请输入英语成绩："))
                        d['python'] = int(input("请输入Python成绩："))
                        d['c'] = int(input("请输入c语言成绩："))
                    except:
                        print("您的输入有误，请重新输入。")
                    else:
                        break  # 跳出循环
                student = str(d) # 将字典转换为字符串
                wfile.write(student + "\n") # 将修改的信息写入文件
                print("修改成功!")
            else:
                # 将未修改的信息写入到文件
                wfile.write(student)
        mark = input("是否继续修改其他学生的信息？（y/n）：")
        if mark == "y":
            modify()  # 重新执行修改操作

def search():
    """查找学生信息"""
    mark = True
    # 保存查询结果的学生列表
    student_query = []
    while mark:
        id = ""
        name = ""
        # 判断文件是否存在
        if os.path.exists(filename):
            mode = input("按ID查输入1；按姓名查输入2：")

            if mode == "1":
                # 按学生ID查询
                id = input("请输入学生ID：")
            elif mode == "2":
                # 按学生姓名查询
                name = input("请输入学生姓名：")
            else:
                print("您的输入有误，请重新输入：")
                search()
            # 打开文件
            with open(filename, "r") as file:
                # 读取全部内容
                student = file.readlines()
                for list in student:
                    # 将字符串转字典
                    d = dict(eval(list))
                    # 判断是否按id查询
                    if id is not "":
                        if d['id'] == id:
                            # 将找到的学生信息保存到列表中
                            student_query.append(d)
                    # 判断是否按姓名查找
                    elif name is not "":
                        if d['name'] == name:
                            # 将找到的学生信息保存到列表中
                            student_query.append(d)
                # 显示查询结果
                show_student(student_query)
                # 清空列表
                student_query.clear()
                inputMark = input("是否继续查询？（y/n）：")
                if inputMark == "y":
                    mark = True
                else:
                    mark = False
        else:
            print("暂未保存数据信息...")
            return

def show_student(studentList):
    """将保存在列表中的学生信息显示出来"""
    # 如果没有要显示的数据
    if not studentList:
        print("(o@.@o)无数据信息(o@.@o) \n")
        return

    # 定义标题显示格式
    format_title = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    print(format_title.format("ID","名字","英语成绩","Python成绩","C语言成绩","总成绩"))  # 按指定格式显示标题
    # 定义具体内容显示格式
    format_data = "{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
    # 通过for循环将列表中的数据全部显示出来
    for info in studentList:
        print(format_data.format(info.get("id"),
                                 info.get("name"),
                                 str(info.get("english")),
                                 str(info.get("python")),
                                 str(info.get("C")),
                                 str(info.get("english"))+str(info.get("python"))+str(info.get("C")).center(12)

                                 ))




def total():
    """统计学生总人数"""
    # 判断文件是否存在
    if os.path.exists(filename):
        # 打开文件
        with open(filename, "r") as rfile:
            # 读取全部内容
            student_old = rfile.readlines()
            if student_old:
                # 打印出统计的学生人数
                print("一共有 %d 名学生！" % len(student_old))
            else:
                print("还没有录入学生信息！")

    else:
        print("暂未保存数据信息...")


def show():
    """显示所有学生信息功能"""
    student_new  = []
    # 判断文件是否存在
    if os.path.exists(filename):
        # 打开文件
        with open(filename, "r") as rfile:
            # 读取全部内容
            student_old = rfile.readlines()
        for list in student_old:
            # 将找到的学生信息保存到列表中
            student_new.append(eval(list))
        if student_new:
            # 调用show_student()函数将学生信息显示到控制台上
            show_student(student_new)
    else:
        print("暂未保存数据信息...")



def sort():
    """按学生成绩排序"""
    # 展示全部学生信息
    show()
    # 判断文件是否存在
    if os.path.exists(filename):
        # 以只读模式打开文件
        with open(filename, "r") as file:
            # 读取全部内容
            student_old = file.readlines()
            student_new = []
        for list in student_old:
            # 字符串转字典
            d = dict(eval(list))
            # 将转换后的字典添加到李表中
            student_new.append(d)
    else:
        return
    ascORdesc = input("请选择（0升序；1降序）：")
    if ascORdesc == "0":
        # 按升序排列
        ascORdescBool = False
    elif ascORdesc == "1":
        # 按降序排序
        ascORdescBool = True
    else:
        print("您的输入有误，请重新输入！")
        sort()
    mode = input("请选择排序方式（1按英语成绩排序；2按Python成绩排序；3按C语言成绩排序；0按总成绩排序）：")
    if mode == "1":
        # 按英语成绩排序
        student_new.sort(key=lambda x: x["english"], reverse=ascORdescBool)
    elif mode == "2":
        # 按Python成绩排序
        student_new.sort(key=lambda x: x["python"], reverse=ascORdescBool)
    elif mode == "3":
        # 按C语言成绩排序
        student_new.sort(key=lambda x: x["C"], reverse=ascORdescBool)
    elif mode == "0":
        # 按总成绩排序
        student_new.sort(key=lambda x: x["english"] + x["python"] + x["C"], reverse=ascORdescBool)
    else:
        print("您的输入有误，请重新输入！")
        sort()
    # 显示排序结果
    show_student(student_new)


if __name__ == '__main__':
    main()




