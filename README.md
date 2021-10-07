# 懸垂マシンを用いた筋トレLOG

目的は，コロナによって減少してしまった運動習慣を復活させるための支援アプリ  
活用方法は，懸垂マシンを用いる時に自分の名前を選択して記録ボタンをタップするだけ  
次の日に合計で何回懸垂マシンを活用したか通知が来ます  
(アプリ開発以前はノートに名前と時間を記録してもらっていました．このアプリを導入することでデータ分析がしやすくなりました)  
(また，Slackでの通知が行われることでどれくらい活用率が変動するかも今回このアプリを導入した理由です．)

# Overview

このアプリは，研究室で実際に使われているため概要だけ説明します．

---

研究室には，このように懸垂マシンが導入されています．

<img height="500" alt="IMG_1674" src="https://user-images.githubusercontent.com/82089820/136354169-ee4b1802-fc5f-420c-96ea-2b957227b3d8.jpg">


以前は紙で記録を行なっていましたが，これをアプリ化しました．

<img width="525" alt='IMG_1675' src="https://user-images.githubusercontent.com/82089820/136354801-d5b36f6c-959b-43bf-83e3-cbd6b946d281.jpg">

トレーニングする前に名前を選択して，記録ボタンを押すだけでよくなりました．

<img width="525" alt="スクリーンショット 2021-10-07 12 19 53" src="https://user-images.githubusercontent.com/82089820/136354418-483fbfff-850f-4653-9444-ac408a06f7c9.png">

記録は次の日の13時にSlackのrandom-channelに送信されます．  
自分の記録と他の人の記録を比較することでモチベーションUPを図ります．

<img width="514" alt="スクリーンショット 2021-10-07 9 05 59" src="https://user-images.githubusercontent.com/82089820/136354537-06eec3e7-930f-428a-bd0e-2cd198fbfc51.png">

# Future features
 
## 利便性

- [ ] UIの改善
- [ ] 週末に個人ごとに今週のフィードバックを送信

## 研究
- [ ] ランダムにグループを作成して，合計で30回の活用という目標を設定
- [ ] 研究室メンバー全員で100回の活用という目標を設定
 
# Requirement
 
cloudinary==1.26.0  
dj-database-url==0.5.0  
Django==3.1.13  
django-cloudinary-storage==0.3.0  
django-widget-tweaks==1.4.8  
gunicorn==20.1.0  
Pillow==8.1.2  
psycopg2==2.9.1  
whitenoise==5.3.0  
slackweb==1.0.5  
slackclient==2.9.3  

# Installation
 
Dockerを用いて簡単に環境構築を行うことができます．
ただし，Slack APIが必要になります．  

1.  リポジトリをクローン
```bash
git clone https://github.com/koya-namba/slack-work-out.git
```
2. リポジトリを移動
```bash
cd slack-work-out/config/settings/
```
3. local.pyを作成し,SECRET_KEYの作成．そして，以下を記述．
```python
DEBUG = TRUE

ALLOWED_HOSTS = []
```
4. リポジトリを移動
```bash
cd slack-work-out/
```
5. slack_information.pyを作成．そして，以下を記述
```python
SLACKURL = '<slackに通知する際に用いるURL>'
OAUTH_TOKEN = '<slackからUser情報をとってくるときに用いるAPI>'
```
6. query_read.pyを実行．Slackのメンバー全員の情報がデータベースに登録できます．
```bash
python query_read.py
```
7. query.pyを実行．設定したチャンネルに昨日の記録が送信されます．
```bash
python query.py
```
8. コンテナを起動．記録を入力する画面が表示できます．
```bash
docker-compose up
```

# Note
 
 これからは，過去のデータ分析の結果と合わせてユーザの入力なしで自動で記録される仕組みを創ります．  
 また，筋トレ種目や回数の推測結果も同時に送信できるアプリを作成します．
 
# Author
 
* 作成者 ： 難波洸也
* 所属 ： 九州大学システム情報科学府
* E-mail ： namba.koya@arakawa-lab.com
* Portfolio : https://nmbsite.herokuapp.com/

# License
 
"Slack筋トレ通知アプリ" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
