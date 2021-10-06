import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
from django import setup
setup()

import datetime as dt
from datetime import date

from django.db.models import Count
import slackweb

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


def create_text(work_out_sort):
    today = date.today()
    text = str(today) + '\n'
    for i, log in enumerate(work_out_sort):
        text += f"第{i+1}位　{log[0]} : {log[1]}回\n"
    return text


def slackPost(message):
    slack = slackweb.Slack(url=SLACKURL)
    slack.notify(text=message)


if __name__ == "__main__":
    topic_data = date_query()
    work_out_sort = sort_query(topic_data)
    text = create_text(work_out_sort)
    slackPost(text)
