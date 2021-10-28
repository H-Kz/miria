# miria_slack
Slack版みりあBot

## About

@nissy氏制作「[みりあやんないよBot for LINE](https://github.com/sfc-icar/miria_line)」を参考に製作した研究会Slack向けbotです。コードに関してはゼロベースで書いています。

## Implementation
#### Outline
[こちら](https://qiita.com/sukesuke/items/1ac92251def87357fdf6)の記事を参考に。2019年12月現在、この記事の通りで動いています。
#### Enviroment
- Python3 (検証: 3.5.2)
- ライブラリ
  - Slackbot (検証: 0.5.6)
  - Subprocess (必要に応じて)

## Feature
現在実装されている機能
#### Listen

当該Botの参加してるチャンネルにて "やって"　を含む発言をしたとき、Slackスタンプにてリアクションする

#### Mention

当該Botをメンションして or DMにてキーワードを含む発言をしたときに動作する

- 指名
  - メンバーリスト(CSVファイル)の中から1人、指名する。なおメンションはしない(当人に関係ないチャンネルに招待することを防ぐため)。

- ping
  - 規定のホストに対してpingを5回実行し（って日本語的に合ってるのか）、結果をSlackに送信する
  
- 味鮮 or 鮮味
  - 中華料理店「[百味鮮](https://goo.gl/maps/TCBQB9ETgMfi5ikn9)」の定食メニューリスト(CSVファイル)の中から、ランダムに選択してSlackに送信する
  
- 自己紹介 or タイプ or 学年 or 身長 or 体重 or 星座 or 血液型 or 利き手 or 出身 or 趣味 or 進捗
  - それぞれ、規定のメッセージを送信する
  
- やって
  - みりあもやるー！
  
