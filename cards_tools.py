# 记录所有的名片字典
card_list = []


def show_menu():
    '''显示菜单'''
    print("*" * 13)
    print("欢迎使用名片系统 V1.0")
    print(" ")
    print("1、新增名片")
    print("2、显示全部")
    print("3、搜索名片")
    print(" ")
    print("0、退出系统")
    print("*" * 13)


def new_card():
    print("新增名片")
    # 1、提示用户输入名片详细信息
    name = input("请输入名字信息:")
    phone = input("请输入电话:")

    # 2、使用用户输入的信息建立一个名片字典
    card_dict = {'name': name, 'phone': phone}
    # 3、将名片字典添加到列表中
    card_list.append(card_dict)
    # print(card_list)
    # 4、提示用户添加成功
    print("添加%s信息成功" % name)


def show_all():
    """
展示所有名片
    :return:
    """
    # print("展示所有名片")
    # for card_dict in card_list:
    #     print(card_dict)
    # 判断是否存在名片记录
    if len(card_list) == 0:
        print("当前没有记录，请添加")
        # return可以返回一个函数的执行结构
        # return下方的代码不会被执行
        # 如果return后面没有内容，表示返回调用函数的位置，并且不会返回任何结果
        return

    # 打印表头
    for name in ["姓名", "手机"]:
        print(name, end="\t\t")
    print(" ")
    print('=' * 13)
    for card_dict in card_list:
        print('%s\t\t %s\t\t' % (card_dict['name'],
                                 card_dict['phone']))


def search_card():
    """
搜索名片
    """
    # print("搜索名片")
    find_name = input("请输入名字")
    for card_dict in card_list:
        if card_dict['name'] == find_name:
            print('姓名\t\t电话')
            print('=' * 13)
            print("%s \t\t %s " % (card_dict['name'], card_dict['phone']))
            deal_card(card_dict)
            break
            # todo 针对找到的名片执行修改和删除的操作

    else:
        print('抱歉,没有找到%s' % find_name)


def deal_card(find_dict):
    """处理查找到的名片

    :param find_dict: 查找到的名片
    """
    # print(find_dict)
    # 修改数据
    action_num = input("请输入你想执行的操作:[1]修改数据[2]删除数据[3]返回主菜单")
    if action_num == '1':

        find_dict['name'] = input_card_info(find_dict['name'], "请输入要修改的姓名:")
        find_dict['phone'] = input_card_info(find_dict['phone'], "请输入要修改的手机号:")
        print("修改成功")

        # 删除数据
    elif action_num == '2':
        # print("删除数据")
        card_list.remove(find_dict)
        print("删除%s成功" % find_dict)


def input_card_info(dict_value, tip_message):
    """输入名片信息

    :param tip_message: 输入提示文字
    :param dict_value: 字典中原有的值
    :return:如果用户输入内容，则返回内容；如果没有输入则返回字典中原有的内容
    """
    result_str: str = input(tip_message)
    # 如果用户输入内容，则返回结果
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
# 如果用户没有输入内容，则返回字典中原有的值
# if __name__ == '__main__':
#     show_all()
