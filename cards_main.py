import cards_tools
while True:
    cards_tools.show_menu()
    action = input("请输入:")

    if action in ['1','2','3']:
        # print("您输入的是[%s]" % action)
        # 1、新增名片
        if action == '1':
            cards_tools.new_card()

        # 2、显示全部
        elif action == '2':
            cards_tools.show_all()

        # 3、搜索名片
        elif action == '3':
            cards_tools.search_card()

    elif action == '0':
    #     输入0则退出程序
        print("欢迎再次使用系统")
        break
    else:
        print("输入错误，请重新输入")
