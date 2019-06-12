#-*- coding: utf-8 -*-
import time
import random

def clear():
    print("\n" * 100)

def loading():
    for _ in range(1):
        print('\r    절 대 로 딩 해   @(^ O^)@  ', end='')
        time.sleep(0.15)
        print('\r    절 대 로 딩 해  @=(^O ^)@  ', end='')
        time.sleep(0.15)
        print('\r    절 대 로 딩 해 @==(^O ^)@  ', end='')
        time.sleep(0.15)
        print('\r    절 대 로 딩 해   @(^O ^)@  ', end='')
        time.sleep(0.15)
        print('\r    절 대 로 딩 해   @(^ O^)=@ ', end='')
        time.sleep(0.15)
        print('\r    절 대 로 딩 해   @(^ O^)==@', end='')
        time.sleep(0.15)

def split():
    print('\n\n')
    print('______  _               _                        _   _    _  _      _  _         ')
    print('| ___ \| |             | |                      | | | |  | || |    (_)| |        ')
    print('| |_/ /| |  __ _   ___ | | __   __ _  _ __    __| | | |  | || |__   _ | |_   ___ ')
    print("| ___ \| | / _` | / __|| |/ /  / _` || '_ \  / _` | | |/\| || '_ \ | || __| / _ |")
    print('| |_/ /| || (_| || (__ |   <  | (_| || | | || (_| | \  /\  /| | | || || |_ |  __/')
    print('\____/ |_| \__,_| \___||_|\_\  \__,_||_| |_| \__,_|  \/  \/ |_| |_||_| \__| \___|\n\n')
    print('    [---]                                                              [---]')
    print('    [---]                     HANYANG UNIV. (ERICA)                    [---]')
    print('    [---]            Jung_Ji_Yong, Han_Seung_Woo, Ko_Dong_Woo          [---]')
    print('    [---]                    Last Update: 2019.05.31                   [---]')
    print('    [---]                                                              [---]\n')
    print('                                 0. 게임 방법 보기')
    print('                                 1. 게임 시작하기')
    print('                                 2. TOP5 랭킹 보기')
    print('                                 3. 종료\n')
    splitanswer = input('번호를 입력하세요:')
    while not (splitanswer == '1' or splitanswer == '2' or splitanswer == '3' or splitanswer == '0'):
        splitanswer = input('번호를 입력하세요:')
    if splitanswer == '0':
        gamerulse()
    elif splitanswer == '2':
        show_top5(members)
    elif splitanswer == '3':
        raise SystemExit

def gamerulse():
    clear()
    print('1. `player`는 `COM`와 게임을 진행합니다.')
    print('2. 각자에게 0 ~ 9까지 적힌 타일이 주어집니다. (홀수 타일은 검은색 □, 짝수 타일은 흰색 ■)')
    print('3. `COM`의 타일은 랜덤으로 섞고 타일의 뒷면(색상)을 보여줍니다. ')
    print('4. `player`는 타일 뒷면의 색깔을 보고 왼쪽부터 순서대로 숫자를 유추해야합니다. ')
    print('5. `round`는 총 10`round`로 진행되며 승점의 합이 더 높은 쪽이 승리하게 됩니다.')
    print('6. `round`당 하나의 숫자를 입력하고 프로그램이 입력한 수와 `COM`의 해당 타일을 비교합니다.')
    print('7. 타일의 색이 같은 경우 숫자가 높은 쪽이 `score`1점을 획득합니다.')
    print('8. 타일의 색이 다른 경우 숫자가 높은 쪽이 `score`2점을 획득합니다.')
    print('9. 숫자 0은 숫자9를 이길 수 있습니다.')
    print('10. 게임이 끝난 후 `COM`와 `player`의 `score` 차 만큼 `Burrito`를 획득하게 됩니다.')
    print('ex) 10 vs 8로 `player`가 이겼다면 10 - 8 = 2 즉, `Burrito`2개를 획득합니다.')
    answer = input('처음으로 돌아가려면 Enter을 누르세요.')
    while not (answer == ''):
        answer = input('처음으로 돌아가려면 Enter을 누르세요.')
    if answer == '':
        split()

def store_members(members):
    file = open("members.txt","w")
    names = members.keys()
    for name in names:
        passwd, tries, wins, chips = members[name]
        line = name + ',' + passwd + ',' + \
               str(tries) + ',' + str(wins) + "," + str(chips) + '\n'
        file.write(line)
    file.close()

def load_members():
    file = open("members.txt","r")
    members = {}
    for line in file:
        name, passwd, tries, wins, chips = line.strip('\n').split(',')
        members[name] = (passwd,int(tries),float(wins),int(chips))
    file.close()
    return members

def login(members):
    username = input("아이디를 입력해주세요: (최대 16글자) ")
    while len(username) > 16:
        username = input("아이디을 다시 입력해주세요: (최대 16글자) ")
    trypasswd = input("비밀번호를 입력해주세요: ")
    if members.get(username): # username이 members에 존재할 때
        if trypasswd == members[username][0]:   # trypasswd와 username가 일치 할 때
            tries = members[username][1]
            wins = members[username][2]
            chips = members[username][3]
            print('You played ' + str(tries) + ' games and won ' + str(wins) + ' of them.')
            print('Your all-time winning percentage is ' + str(divide(wins,tries)) + ' %')
            if chips >= 0:
                print('You have ' + str(chips) + ' chips.')
            else:
                print('You owe ' + str(abs(chips)) + ' chips.')
            return username, tries, wins, chips, members
        else:   # 비밀번호가 일치하지 않을 때
            return login(members)
    else:   # username이 members에 존재하지 않을 때
        print("This name(", username, ") doesn't register",sep='')
        answerregister = input('Do you want to register?(y/n)')
        if answerregister == 'y':
            print('Your name is', username)
            registerpw()
            if registerpasswd == reregisterpasswd:
                members[username] = (registerpasswd, 0,0,0)
                return username, 0, 0, 0, members
            else:
                registerpw()
        elif answerregister == 'n':
            login(members)
        else:
            answerregister = input('Do you want to register?(y/n)')

def registerpw():
    registerpasswd = input('Enter your password:')
    reregisterpasswd = input('Enter your password again:')

def make_COM_list():
    deck = [[0, '□'], [1, '■'], [2, '□'], [3, '■'], [4, '□'], [5, '■'], [6, '□'] ,[7, '■'], [8, '□'], [9, '■']]
    random.shuffle(deck)
    return deck

def show_top5(members):
    print("-----")
    sorted_members = sorted(members.items(), key= lambda x:x[1][3], reverse = True)
    print("All-time Top 5 based on the number of chips earned")
    if len(sorted_members) < 5:
    	for i in range(len(sorted_members)):
    			if(sorted_list[i][1][3] > 0):
    				print(str(i+1) + '.', sorted_members[i][0] ,":", sorted_members[i][1][3])
    else :
    	for i in range(5):
    		if(sorted_members[i][1][3] > 0):
    			print(str(i+1) + '.', sorted_members[i][0] ,":", sorted_members[i][1][3])



def black_and_white():
    loading()
    load_members()
    split()

    print('게임을 시작하겠습니다.')
    username, tries, wins, chips, members = 0, 0, 0, 0, 0
    play_more = True
    while play_more == True:
        tries += 1
        score_player = 0
        score_com = 0
        print('-----')

        list_com = make_COM_list()
        list_com_color = []
        list_com_number = []
        list_player = [0,1,2,3,4,5,6,7,8,9]
        list_player_sug = []
        for x in list_com:
            list_com_color.append(x[1])

        for round in range(1,10):
            list_com_number.append(list_com[round-1][0])
            print('----------Round:', round,'----------')
            print('현재 점수 현황')
            print('당신점수 - ',score_player ,' : 컴퓨터 점수 - ', score_com)
            print('--------------------')
            for x in list_com_color:
                print(x, end='')

            print('/n')
            if round > 1:
                print(list_com_number[0:round-1])
                print(list_player_sug[0:round-1])
            print('보유한 타일 중 제시할 타일을 입력해주세요 (0~9까지만 입력가능)')
            print('남은 타일:', list_player)
            p = input()
            while not(p.isdigit) or not( 0 <= int(p) <= 9) or p in list_player:
                print('다시 입력해주세요')
                print('남은 타일:', list_player)
                p = input()
            list_player.remove(int(p))
            list_player_sug.append(int(p))
            print('당신은 ', p,'를 제시하셨습니다')
            print('결과는...')
            for x in range(3,0,-1):
                print(x)
                time.sleep(1)
            print('컴퓨터 타일:', list_com_color)
            print('컴퓨터 타일:', list_com_number)
            print('당신의 타일:', list_player_sug)

            time.sleep(1)

            if list_player_sug[round-1] > list_com_number[round-1]:
                if list_player_sug[round-1] % 2 != list_com_number[round-1][0] % 2:
                    print('당신이 2점을 획득하셨습니다!')
                    score_player +=2
                else:
                    print('당신이 1점을 획득하셨습니다!')
                    score_player +=1

            if list_player_sug[round-1] < list_com_number[round-1]:
                if list_player_sug[round-1] % 2 != list_com_number[round-1][0] % 2:
                    print('컴퓨터가 2점을 획득하였습니다!')
                    score_com += 2
                else:
                    print('컴퓨터가 1점을 획득하였습니다!')
                    score_com += 1

            if list_player_sug[round-1] == list_com_number[round-1]:
                print('무승부하였습니다.')

            time.sleep(1)

            if round <9:
                print('다음 라운드로 넘어가겠습니다.')
                time.sleep(1)

        print('#최종결과#')
        if score_player < score_com:
            print('당신점수 - ',score_player ,' : 컴퓨터 점수 - ', score_com,' 으로 당신이 패배하였습니다!')
            print('당신은 ', abs(score_player - score_com), ' 개의 부리또를 잃으셨습니다.')
            chips -= abs(score_player - score_com)
        if score_com < score_player:
            wins += 1
            print('당신점수 - ',score_player ,' : 컴퓨터 점수 - ', score_com,' 으로 당신이 승리하셨습니다!')
            print('당신은 ', abs(score_player - score_com), ' 개의 부리또를 얻으셨습니다.')
            chips += abs(score_player - score_com)
        else:
            wins += 0.5
            print('당신점수 - ',score_player ,' : 컴퓨터 점수 - ', score_com,' 으로 무승부하셨습니다!')

        members[username] = (members[username][0], tries, wins, chips)
        print('현재 당신이 보유한 부리또는 ', chips,'개 입니다.')
        show_top5(members)

        play_more = more('계속해서 플레이 하시겠습니까?')

    store_members(members)
    print('다음에 또 찾아주세요!')


black_and_white()
