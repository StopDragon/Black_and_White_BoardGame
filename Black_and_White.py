import time

black_and_white():
    split()
    username, tries, wins, chips, members = login(load_members())
    play_more = True
    while play_more == True:
        tries += 1
        score_player = 0
        score_com = 0
        print('-----')

        list_com = make_list_com()
        list_com_color = []
        list_com_number = []
        list_player = [0,1,2,3,4,5,6,7,8,9]
        list_player_sug = []
        for x in list_com:
            list_com_color.append(list_com[x][1])

        for round in range(1,10):
            list_com_number.append(list_com[round-1][0])
            print('----------Round:', round,'----------')
            print('현재 점수 현황')
            print('당신점수 - ',score_player ,' : 컴퓨터 점수 - ', score_com)
            print('--------------------')
            print(list_com_color)
            print(list_com_number)
            print(list_player_sug)
            p = input('보유한 타일 중 제시할 타일을 입력해주세요 (0~9까지만 입력가능)')
            print('남은 타일:', list_player)
            while not(p.isdigit) or not(0=<int(p)=<9) or p in list_player:
                p = input('다시 입력해주세요')
                print('남은 타일:', list_player)
            list_player.remove(p)
            list_player_sug.append(p)
            print('당신은 ', p,'를 제시하셨습니다')
            print('결과는...')
            for x in range(3,0,-1):
                print(x)
                time.sleep(1)
            print('컴퓨터 타일:', list_com_color)
            print('컴퓨터 타일:', list_com_number)
            print('당신의 타일:', list_player_sug)

            time.sleep(1)

            if list_player_sug[round-1] < list_com_number[round-1]:
                if list_player_sug[round-1] % 2 = list_com[round-1][1]:
                    print('당신이 2점을 획득하셨습니다!')
                    score_player +=2
                else:
                    print('당신이 1점을 획득하셨습니다!')
                    score_player +=1

            if list_player_sug[round-1] < list_com_number[round-1]:
                if list_player_sug[round-1] % 2 = list_com[round-1][1]:
                    print('컴퓨터가 2점을 획득하였습니다!')
                    score_com += 2
                else:
                    print('컴퓨터가 1점을 획득하였습니다!')
                    score_com += 1

            else:
                print('무승부하였습니다.')

            time.sleep(1)

            if round <9:
                print('다음 라운드로 넘어가겠습니다.')
                time.sleep(1)

        print('#최종결과#')
        if score_player < score_com:
            print('당신점수 - ',score_player ,' : 컴퓨터 점수 - ', score_com,' 으로 당신이 패배하였습니다!')
            chips -= abs(score_player - score_com)
        if score_com < score_player:
            print('당신점수 - ',score_player ,' : 컴퓨터 점수 - ', score_com,' 으로 당신이 승리하셨습니다!')
            chips += abs(score_player - score_com)
        else:
            print('당신점수 - ',score_player ,' : 컴퓨터 점수 - ', score_com,' 으로 무승부하셨습니다!')

        members[username] = (members[username][0],tries, wins, chips)
        show_top5(members)

        more('계속해서 플레이 하시겠습니까?')

    store_members(members)
    print('다음에 또 찾아주세요!')
