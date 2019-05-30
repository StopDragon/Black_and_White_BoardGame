# Black_and_White_BoardGame
### 한양대학교 CSE1017 프로그래밍기초 1학년 1학기 팀프로젝트
#### TEAM_NAME: 절대태보해 @==(^0 ^)@
#### TEAM_MEMBERS: Jung_Ji_Yong, Han_Seung_Woo, Ko_Dong_Woo

## 1. 게임규칙
1. `player`는 `COM`와 게임을 진행합니다.
2. 각자에게 0 ~ 9까지 적힌 타일이 주어집니다. (홀수 타일은 검은색□, 짝수 타일은 흰색■)
3. `COM`의 타일은 랜덤으로 섞고 타일의 뒷면(색상)을 보여줍니다. 
4. `player`는 타일 뒷면의 색깔을 보고 왼쪽부터 순서대로 숫자를 유추해야합니다. 
5. `round`는 총 10`round`로 진행되며 승점의 합이 더 높은 쪽이 승리하게 됩니다.
6. `round`당 하나의 숫자를 입력하고 프로그램이 입력한 수와 `COM`의 해당 타일을 비교합니다.
7. 타일의 색이 같은 경우 숫자가 높은 쪽이 `score`1점을 획득합니다.
8. 타일의 색이 다른 경우 숫자가 높은 쪽이 `score`2점을 획득합니다.
9. 숫자 0은 숫자9를 이길 수 있습니다.
10. 게임이 끝난 후 `COM`와 `player`의 `score` 차 만큼 `Burrito`를 획득하게 됩니다.
<br>*ex) 10 vs 8로 `player`가 이겼다면 10 - 8 = 2 즉, `Burrito`2개를 획득합니다.*

## 2. 개발 계획
### 2.1. 함수 목록
`split()`
>게임 로딩 화면입니다.

`load_members()`
>`members.txt`에서 `player`들의 정보를 `members`에 불러옵니다.

`login(members)`
>`members`에서 아이디와 비밀번호를 비교합니다.<br>
>비밀번호가 틀리면 다시 입력할 수 있습니다.<br>
>존재하지 않는 아이디를 입력하면 `register()`를 호출합니다.

`register()`
>아이디와 비밀번호를 입력받아 `members`에 추가시킵니다.<br>
>비밀번호는 두번 입력받아 사용자가 잘못 입력하는 것을 방지합니다.

`make_COM_list()`
>컴퓨터의 타일을 랜덤으로 섞어줍니다.

`show_tile()`
>튜플로 만들어져있는 `COM_list`를 시각화하여 보여줍니다.<br>
>ex) □■□□□■■■□■

`store_members(members)`
>`members`에 저장된 정보를 `members.txt`에 저장해줍니다.

`show_top5(members)`
>`Burrito`를 가진 상위 5명을 보여줍니다.

`more(message)`
>`player`에게 `y` 또는 `n`을 입력받아 `y`이면 `True`를 `n`이면 `False`를 리턴합니다.

### 2.2. 알고리즘 구상도
![algorithm_1](https://github.com/StopDragon/Black_and_White_BoardGame/blob/master/photo/algorithm_1.jpeg?raw=true)
![algorithm_2](https://raw.githubusercontent.com/StopDragon/Black_and_White_BoardGame/master/photo/algorithm_2.jpeg)

### 2.3. 게임 프로토타입
>[       ROUND 1.        ]
>        □■□□□■■■□■
>COM     145
>player  253 
>
>남은 숫자: 1,4,6,7,8,9,0

## 3. 기타 개발 주의 사항
- 모든 입력값 비교는 문자(str)로 비교한다.<br>
- 조기 게임 종료 조건은 `COM_scoer > player_scoer + (10 - round) * 2`로 한다.<br>
- 편의상 짝수는 `0` 홀수는`1`이라고 칭한다.<br>
- `list_COM`은 튜플로 구성된 리스트로 생성한다.<br>
- 매 `round`가 종료되면 `COM`의 숫자를 공개한다.<br>
<br><br><br>

_Copyright 2019. Jung_Ji_Yong, Han_Seung_Woo, Ko_Dong_Woo All Rights Reserved._
_All Pictures and Code Can Not Be Copied or Used Without Permission._