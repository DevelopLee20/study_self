import requests
from bs4 import BeautifulSoup
import ccxt # 바이낸스 API

def get_social(site): # 사회적 거리두기 크롤링
    url = 'http://ncov.mohw.go.kr/regSocdisBoardView.do?brdId=6&brdGubun=68&ncvContSeq=495'

    content = requests.get(url)
    assert content.status_code == 200

    soup = BeautifulSoup(content.text, 'html.parser')

    button = soup.find_all("script")

    data = button[-1]

    data = str(data)

    a = data.split(",")

    social = []

    for i in a:
        if (i.find("DES :")+1):
            text = i[9:]
            want = text[:text.find("계")+1]
            social.append(want)

    for i in social:
        if (i.find(site)+1):
            return str(i)

    return 0

def Fortune(ttie): # 오늘의 운세 (띠별)

    ttie_list = ['뱀띠','쥐띠','소띠','호랑이띠','토끼띠','용띠','말띠','양띠','원숭이띠','닭띠','개띠','돼지띠']

    if ttie not in ttie_list:
        return 0

    url = f'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={ttie}%20운세'

    req = requests.get(url)

    assert req.status_code == 200

    contents = BeautifulSoup(req.text, 'html.parser')

    sign_lst = contents.find("p",{"class":"text _cs_fortune_text"})

    return sign_lst.text

def Note(text, text2, text3, author): # 제안 기능

    if text3 != None:
        text = str(text) +' '+ str(text2) +' '+ str(text3)

    elif text2 != None:
        text = str(text) +' '+ str(text2)

    else:
        text = str(text)

    f = open('read.txt','a', encoding='UTF-8')
    f.write(author+" : "+text+'\n')
    f.close()

def opgg_user(username): # 오피지지 유저 정보 크롤링
    url = f"https://www.op.gg/summoner/userName={username}"

    content = requests.get(url)
    assert content.status_code == 200

    soup = BeautifulSoup(content.text, 'html.parser')

    lst = soup.find("div",{"class":"GameItemList"})
    game_list = lst.find_all("div",{"class":"Content"})

    Game_Type = {'ARAM':'칼바람 나락','Ranked Solo':'솔로랭크','Normal':'일반','Bot':'봇전','Flex 5:5 Rank':'자유랭크','Ultimates':'궁극기모드','One for All':'단일챔피언'}
    Type_List = []; Champion_List = []; Kill_List = []; Death_List = []; Assist_List = []; Win_Loss_List = []
    Win_count = 0; Loss_count = 0

    # ARAM : 칼바람 나락, Ranked Solo : 솔랭, Normal : 일반, Bot : 봇전, Flex 5:5 Rank : 자유랭, Ultimates : 궁극기모드
    for i in game_list:
        game_type_x = i.find("div",{"class":"GameType"})
        champion_x = i.find("div",{"class":"ChampionName"})
        KDA_x = i.find("div",{"KDA"})
        Win_Loss_x = i.find("div",{"class":"GameResult"})
        
        try:
            # 게임  타입
            if game_type_x.get('title') in Game_Type:
                for key, value in zip(Game_Type.keys(), Game_Type.values()):
                    if game_type_x.get('title') == key:
                        Type_List.append(value)
                        break
            else:
                Type_List.append(game_type_x.get('title'))

            # 챔피언 이름
            champion = (champion_x.text)
            champion = champion[1:-1]
            Champion_List.append(champion)

            # KDA
            Kill = KDA_x.find("span",{"class":"Kill"}).text
            Death = KDA_x.find("span",{"class":"Death"}).text
            Assist = KDA_x.find("span",{"class":"Assist"}).text

            Kill_List.append(int(Kill))
            Death_List.append(int(Death))
            Assist_List.append(int(Assist))

            # 승 패 읽기
            result = Win_Loss_x.text.strip()
            if result == 'Victory':
                Win_count += 1
            else:
                Loss_count += 1

            Win_Loss_List.append(result)

        except:
            pass

    # 승률
    Win_Rate = round(Win_count * 5 , 2)
    # 20경기 KDA
    KDA_20Play = round((sum(Kill_List) + sum(Assist_List)) / sum(Death_List) , 2)

    frint = ''
    for a,b,c,d,e,f in zip(Type_List, Champion_List, Win_Loss_List, Kill_List, Death_List, Assist_List):
        frint += f'{a:^7s} | {b:^10s} | {c:^7s} | KDA: {d}/{e}/{f}\n'

    return Win_Rate, KDA_20Play, frint

def Binance_coin_search(coin): # 바이낸스 API 기반 시세 검색
    # 실시간 달러 불러오기
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=달러'
    content = requests.get(url)
    assert content.status_code == 200

    soup = BeautifulSoup(content.text, 'html.parser')

    # 달러 정수로 변환
    daller = list(soup.find('span',{'class':'spt_con'}).find('strong').text)
    daller.remove(',')
    daller.remove('.')
    daller = [int(i) for i in daller]
    chk = 1000
    result = 0
    for i in daller:
        result += chk * i
        chk /= 10

    daller = result

    # 바이낸스 API
    binance = ccxt.binance()
    markets = binance.fetch_tickers() # 전체 코인 목록 딕셔너리

    use_coin = coin.upper()
    coin = use_coin + '/USDT'

    if coin in markets:
        price = float(markets[coin]['close'])
        fin = int(price * daller)
        price = format(price , ',') # 돈처럼 끊어서 출력
        fin = format(fin, ',') # 돈처럼 끊어서 출력
        return f'바이낸스\n{use_coin}의 마지막 거래가격!\n{price} 달러\n{fin} 원'
    else:
        return '그런코인은 존재하지 않아...'

def Weather(text1, text2): # 네이버 날씨 검색 후
    long = text1
    short =''
    if text2 != None:
        short = text2
    url = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={long}+{short}+날씨"

    content = requests.get(url)
    assert content.status_code == 200

    soup = BeautifulSoup(content.text, 'html.parser')

    try:
        sentence = soup.find('div',{'class':'main_info'}).text.strip().split('   ')
        sentence[0] = '온도 : ' + sentence[0]
        sentence[1] = '날씨 :' + sentence[1]
        sentence[2] = '최저/최고 :' + sentence[2]

        site = (long+' '+short).strip()
        return f'{site}의 날씨\n{sentence[0]}\n{sentence[1]}\n{sentence[2]}\n{sentence[3]}'
    except:
        return f'지역을 못찾겠어...'

Weather('서울특별시', None)