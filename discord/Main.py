from typing import Text
import discord, asyncio, os, sys
from discord.ext import commands
import random
import Function as func

#변수
sseong = '#2571'
#

def get_token():
    return 'ODcxMjcwNTAwNjY2NTk3Mzc2.YQY34g.soDFY2TmXFIpTT5_v41VNp9MCNo'
    
token = get_token()

game_status = discord.Game("Python") # 상태 변경
bot = commands.Bot(command_prefix='!', status=discord.Status.online, activity=game_status, help_command= None) # 명령어, 상태 선택

@bot.command(aliases=['인사', '안녕', 'hello','ㅎㅇ'])
async def hi(ctx):
    await ctx.send(f'{ctx.author.mention} ㅎㅇ 안녕하세요')

@bot.command(aliases=['모여'])
async def 집합(ctx):
    await ctx.send(f'@everyone 집합')

@bot.command(aliases=['도움','도움말','h'])
async def help(ctx):
    embed = discord.Embed(title='찹살콩팥떡', description="ㅎㅇㅎㅇ")
    embed.add_field(name="1. 인사, 안녕, hello, ㅎㅇ", value="인사 잘해줍니다", inline=False)
    embed.add_field(name="2. 날씨 검색", value="!날씨 경기도 안성시", inline=False)
    embed.add_field(name="3. 거리두기, 사회적거리두기, 그거", value="!거리두기 경기\n경기, 인천, 서울\n강원, 세종, 충북\n충남, 대전, 경북\n전북, 대구, 전남\n광주, 경남, 울산\n부산, 제주", inline=False)
    embed.add_field(name="4. 운세, 오늘의운세, 띠별운세", value="!운세 뱀띠", inline=False)
    embed.add_field(name="5. 기능 제안하기(띄어쓰기 인식 안댐)", value="!제안 뭐만들어줘", inline=False)
    embed.add_field(name="6. 롤 전적 검색", value="!롤전적, !전적, !롤, !전적검색\n유저명 띄어쓰기 없이!", inline=False)
    embed.add_field(name="7. 코인 시세 검색", value="!코인 코인명", inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=['정현'])
async def 김정현(ctx):
    await ctx.send(f'안녕 정현')

@bot.command(aliases=['민서'])
async def 강민서(ctx):
    await ctx.send(f'안녕 민서')

@bot.command(aliases=[])
async def 김민서(ctx):
    await ctx.send(f'형... 김민서 아니라 강민서라니까요..?')

@bot.command(aliases=['민서,예쁘다'])
async def 민서예쁘다(ctx):
    await ctx.send(f'맞아 맞아 민서 예쁘지~~')

@bot.command(aliases=['민서 귀엽다'])
async def 민서귀엽다(ctx):
    await ctx.send(f'맞아 맞아 민서 귀엽지~~')

@bot.command(aliases=['민서 아름답다'])
async def 민서아름답다(ctx):
    await ctx.send(f'맞아 맞아 민서 아름답지~~')

@bot.command(aliases=['민서 스담스담','민서쓰담쓰담'])
async def 민서스담스담(ctx):
    author = ctx.author
    author = str(author)
    get = author[-5:]

    if get == sseong:
        await ctx.send(f'민서 스담스담~~')
    else:
        await ctx.send(f'어허 너는 못써')

@bot.command(aliases=['지현'])
async def 성지현(ctx):
    await ctx.send(f'UC의 랩장님.... 성지현!!!!!!!!!!!')

@bot.command(aliases=['인규'])
async def 이인규(ctx):
    await ctx.send(f'신창 상시 대기중...(장원빌 402호)')

@bot.command(aliases=['용인'])
async def 김용인(ctx):
    await ctx.send(f'저 찹살콩팥떡은 김용인씨의 솔로탈출을 기원합니다')

@bot.command(aliases=['상준'])
async def 전상준(ctx):
    await ctx.send(f'키즈카페의 마스터, 원숭이 공화국의 국왕 그이름은... 전상준.')

@bot.command(aliases=['한뫼','뫼'])
async def 정한뫼(ctx):
    await ctx.send(f'이사람은 대리기사 신고바랍니다.')

@bot.command(aliases=['동의','인정?','ㅇㅈ'])
async def 인정(ctx):
    await ctx.send(f'이건 인정이지..')

@bot.command(aliases=['ㄹㅇㅋ','ㄹㅇㅋㅋ','ㄹㅇ'])
async def 리얼키키(ctx):
    await ctx.send(f'ㄹㅇㅋㅋ 만쳐')

@bot.command(aliases=['더럽'])
async def 더러워(ctx):
    await ctx.send(f'પ નુલુગ લસશ')

@bot.command(aliases=['동균'])
async def 유동균(ctx):
    await ctx.send(f'충성!')

@bot.command(aliases=['거리두기','사회적','그거'])
async def 사회적거리두기(ctx, text):
    content = func.get_social(text)
    if content == 0:
        await ctx.send(f'거기가 어디야?')
    else:
        await ctx.send(f'사회적 거리두기 현황 : {content}')

@bot.command(aliases=['오늘의운세','띠별운세'])
async def 운세(ctx, text):
    content = func.Fortune(text)
    if content == 0:
        await ctx.send(f'그건 무슨 띠야')
    else:
        await ctx.send(f'[{text}]\n{content}')

@bot.command(aliases=['한마디'])
async def 제안(ctx, text, text2=None, text3=None):
    func.Note(text, text2, text3, str(ctx.author))
    await ctx.send(f'ㅇㅋ 확인~ 적었어')

@bot.command(aliases=['전적검색','전적','롤'])
async def 롤전적(ctx, text):
    a, b, c  = func.opgg_user(text)
    await ctx.send(f'{text}의 최근 20경기 통계!\n승률 : {a}%\nKDA : {b} : 1\n{c}')

@bot.command(aliases=['잘자요','꿈'])
async def 잘자(ctx):
    await ctx.send(f'잘자요 {ctx.author.mention}씨 내일 또 봐요~')

@bot.command(aliases=['가상화폐','비트코인'])
async def 코인(ctx, text):
    a = func.Binance_coin_search(text)
    await ctx.send(a)

# 메소드
@bot.command(aliases=['날씨검색'])
async def 날씨(ctx, text1, text2=None):
    a = func.Weather(text1, text2)
    await ctx.send(a)

bot.run(token)