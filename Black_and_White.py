black_and_white():
    username, tries, wins, chips, members = login(load_members())
    play_more = True
    while play_more == True:
        tries += 1
        round = 0
        print('-----')
        for _ in range(9):
            round +=1
            list_com_color = []
            list_com = make_list_com()
            list_com_number = []
            list_player = [0,1,2,3,4,5,6,7,8,9]
            for x in list_com:
                if list_com[x][1] % 2 = 1:
                    list_com_color.append(■)
                else:
                    list_com_color.append(□)
            list_com_number.append(list_com[round-1])
            print(list_com_color)
            print(list_com_number)
