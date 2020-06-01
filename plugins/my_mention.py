# coding: utf-8

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデ
import subprocess
import csv
import random



"""
# 雛形
@respond_to('メンション') # メンションをつけて'~~~'と言ったときのみ反応する
def mention_func(message):
    message.reply('私にメンションと言ってどうするのだ') # メンション

@listen_to('リッスン')
def mention_func(message):
    message.send('誰かがリッスンと投稿したようだ')      # ただの投稿
    message.reply('君だね？')                           # メンション
"""

@listen_to('やって')
def listen_func(message):
    print(message)
    message.react('miria')
    message.react('yaru')



@respond_to('自己紹介')
def hogehoge(message):
    message.reply('赤城みりあですっ♪　かわいいもの、だーい好き！アイドルってカワイイ服着られて、カワイイ歌とかダンス、やらせてもらえるんだよね？わーいっ！はやくアイドルになって、楽しいこと見つけたいな！')


@respond_to('タイプ')
def mention_func(message):
    message.reply('プロデューサーさんは「みりあはパッションだ」って言ってたよ')


@respond_to('学年')
def mention_func(message):
    message.reply('小学5年生だよ！')


@respond_to('身長')
def mention_func(message):
    message.reply('140cmだよ！')


@respond_to('体重')
def mention_func(message):
    tmp = lottery(10)
    if tmp == 1:
        message.reply('36kgだよ！')
    else:
        message.reply('それはナイショ…！')


@respond_to('星座')
def mention_func(message):
    message.reply('おひつじ座だよ！')


@respond_to('血液型')
def mention_func(message):
    message.reply('AB型だよ！')


@respond_to('利き手')
def mention_func(message):
    message.reply('左利きだよ！')


@respond_to('出身')
def mention_func(message):
    message.reply('みりあ、小さい頃から東京に住んでるんだ！')


@respond_to('趣味')
def mention_func(message):
    message.reply('みりあ、おしゃべりするのが大好き')
    

@respond_to('進捗')
def mention_func(message):
    message.react('miria')
    message.reply('がんばってるみんなを、がんばって応援しちゃうよ♪')


# ping打って教えてくれる機能
@respond_to('ping')
def mention_func(message):
    message.reply('なになに? ping?? はい、はいはいっ! お手伝いしまーすっ☆')
    proc1 = subprocess.run(["ping", "sfc.wide.ad.jp", "-c", "5"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc1 = proc1.stdout.decode('utf-8')
    message.send(' *RG*   from SAKURA Internet (Osaka3) ```' + proc1 + '``` ')

    proc2 = subprocess.run(["ping", "vu.sfc.keio.ac.jp", "-c", "5"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc2 = proc2.stdout.decode('utf-8')
    message.send(' *CNS*   from SAKURA Internet (Osaka3) ```' + proc2 + '``` ')


# 1~maxの整数を抽選
def lottery(max):
    import random
    max -= 1
    max = max * random.random()
    max += 1
    max = max // 1
    max = int(max)
    return max


@respond_to('鮮味')
def mention_func(message):
    select_menu = choice_misen()
    message.reply('うんとね、みりあのおすすめは百味鮮の' + str(select_menu) + 'だよっ！')


@respond_to('味鮮')
def mention_func(message):
    select_menu = choice_misen()
    message.reply('うんとね、みりあのおすすめは' + str(select_menu) + 'だよっ！')


@respond_to('ロガー')
def mention_func(message):
    select_member = choice_member(7)
    print('きょうのログをとってくれるプロデューサーさんは、' + str(select_member) + 'だよっ！')
    message.send('きょうのログをとってくれるプロデューサーさんは、' + str(select_member) + 'だよっ！')


@respond_to('指名')
def mention_func(message):
    member_option = 0
    message_text = message.body['text']
    # 指定のワードが含まれていた場合、メンバー抽選に条件がかかる。member_optionの値はセルの列番号に一致する
    if '卒論' in message_text:
        member_option = 8
    elif 'TERM' in message_text or 'Term' in message_text or 'term' in message_text:
        member_option = 9
    elif 'WIP' in message_text or 'Wip' in message_text or  'wip' in message_text:
        member_option = 10
    elif '新人' in message_text:
        member_option = 5
    elif '旧人' in message_text:
        member_option = 6
    elif 'ログ'in message_text or 'ロガー' in message_text:
        member_option = 7
    select_member = choice_member(member_option)
    print('じゃあ......' + str(select_member) + '！')
    message.send('じゃあ......' + str(select_member) + '！')
    print('=====')


@listen_to('やって')
def menrion_func(message):
    message.react('miria')
    message.react('yaru')
    message.send('みりあもやるー!!')


def choice_misen():
    import csv
    count = 0
    line = 0
    """
    # CSVの行数を数える→lenでできたので不要になった
    with open ('/home/ubuntu/slackbot/data/misen.csv') as misen_csv:
        reader = csv.reader(misen_csv)
        for row in reader:
            #print(str(count) + str(row))
            count += 1
        line = lottery(count)
        #print ('当選番号＝' + str(line))
    """
    # CSVを2次元配列にする
    with open('/home/ubuntu/slackbot/data/misen.csv') as misen_csv:
        reader = csv.reader(misen_csv)
        misen_array = [row for row in reader]
        establish = 0
        while establish == 0:
            # 配列の長さを取得
            count = len(misen_array)
            # 料理を選ぶ(1~countの整数乱数)
            line = lottery(count)
            # print ('当選番号＝' + str(line))
            # 抽選結果の料理を取得
            select_menu_type = misen_array[line][2]
            # print('menu type = ' + str(select_menu_type) + '(1=定食)')
            # 定食かどうかを判定

            if (int(select_menu_type) == 1):
                select_menu = misen_array[line][0]
                select_price = misen_array[line][1]
                select_menu = str(select_menu) + \
                    ' (' + str(select_price) + '円) '
                # print ('うんとね、みりあのおすすめは' + str(select_menu) + 'だよっ！')
                establish = 1
                return select_menu


def choice_member(member_option):
    # import csv
    # count = 0
    # CSVを2次元配列にする
    with open('/home/ubuntu/slackbot/data/icar_member.csv') as member_csv:
        reader = csv.reader(member_csv)
        member_array = [row for row in reader]
        count = len(member_array) # 配列の長さを取得
        establish = 0
        while establish != 1:
            line = lottery(count)  # メンバーを選ぶ(1~countの整数乱数)
            select_member = member_array[line][3]  # 抽選結果のメンバーを取得
            if member_option == 0:  # 抽選対象を制限しないとき、常に抽選は成立している
                print ('抽選対象の条件なし')
                establish = 1
            tmp = int(member_array[line][member_option])
            print('成立条件セル→ ' + str(line) + ',' + str(member_option) +  '   抽選成立(0=不成立)→ ' + str(tmp) + '   当選者→ ' + select_member)  # 指定セル、指名メンバー表示
            if tmp == 1:  # 条件のセルが１の場合、抽選が成立する
                establish = 1
        else:
            print (select_member)
            return select_member

            # 抽選が成立しないときはWhileでループする
        # print (select_member)


