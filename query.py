import os

# 開発
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
# from django import setup
# setup()

# デプロイ
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
from django import setup
setup()


import datetime as dt
from datetime import date
from django.db.models import Count
import json
import random
from urllib import request

from slack_work_out.models import WorkOut


try:
    import slack_information
    SLACKURL = slack_information.SLACKURL
except:
    SLACKURL = os.environ.get('SLACKURL')


def date_query():
    """昨日のデータを取得"""
    today = date.today()
    yesterday = today - dt.timedelta(days=1)
    topic_data = WorkOut.objects.filter(training_at__date=yesterday)
    return topic_data


def sort_query(topic_data):
    """回数が多い順にソート"""
    work_out_count_queries = topic_data.values('user__name').annotate(count=Count('pk'))
    work_out_count = {}
    for work_out_count_query in work_out_count_queries:
        work_out_count[work_out_count_query['user__name']] = work_out_count_query['count']
    work_out_sort = sorted(work_out_count.items(), key=lambda x: x[1], reverse=True)
    return work_out_sort


def create_json(work_out_sort):
    """Slackに送信するjsonを作成"""
    today = date.today()
    yesterday = today - dt.timedelta(days=1)
    yesterday = yesterday.strftime('%Y/%m/%d')
    # タイトルの作成
    title = f":muscle: {yesterday}のトレーニングデータ :muscle:"
    # ランキングの作成
    text = ""
    for i, log in enumerate(work_out_sort):
        text += f"第{i+1}位  {log[0]} : {log[1]}回\n"
    # コメントの作成(筋トレした人数に合わせて変更)
    comment_zero = [
        "昨日は0人でした．．．\n今日こそはトレーニング頑張ってください！",
        "研究室の懸垂マシンは，腹筋・胸筋も鍛えられますよ！",
        "10秒ぶら下がるだけでも，身体が伸びますよ〜",
    ]
    comment_small = [
        "研究室に来たらぜひ活用してください!",
        "昨日はトレーニングした人が少ないですね．．．\n今日はぜひ頑張ってください！",
        "ぶら下がるだけでも，健康に慣れますよ！",
        "食事，睡眠，運動は健康に過ごすために必須です！",
        "デスクワークには，ぶら下がりが1番ですよ〜"
    ]
    comment_medium = [
        "昨日はトレーニングした人が多いですね！\n今日も頑張ってください！",
        "みなさんトレーニング頑張ってますね！",
        "ぶら下がり以外にも懸垂，レッグレイズ，腕立て伏せにもチャレンジしてください！"
    ]
    comment_large = [
        "昨日のトレーニング人数すごいですね！\nぜひ今日も！",
        "とてもいい感じでトレーニングできてますね！",
        "みなさんでトレーニングがんばりましょう！"
    ]
    if len(work_out_sort) == 0:
        comment = random.choice(comment_zero)
    elif len(work_out_sort) <= 5:
        comment = random.choice(comment_small)
    elif len(work_out_sort) <= 10:
        comment = random.choice(comment_medium)
    else:
        comment = random.choice(comment_large)
    # jsonの作成
    headers = {
    'Content-Type': 'application/json; charset=utf-8'
    }
    slack_message = {
        "username": "WorkOut-Log",
        # slackへ送信元のユーザ名
        "attachments": [
            # slackへの本文
            {
                "title": title,
                "text": "\n昨日の懸垂マシンを用いた筋トレ回数ランキングをお知らせします！"
            },
            {
                "text": text,
            },
            {
                "text": comment,
            },
        ]
    }
    req = request.Request(SLACKURL, data=json.dumps(slack_message).encode("utf-8"), headers=headers, method='POST')
    return req


if __name__ == "__main__":
    topic_data = date_query()
    work_out_sort = sort_query(topic_data)
    req = create_json(work_out_sort)

    try:
        res = request.urlopen(req, timeout=5)
    except Exception as e:
        print("Error")
