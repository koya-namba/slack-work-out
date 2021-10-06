import os

# 開発
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
# from django import setup
# setup()

# デプロイ
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
from django import setup
setup()


from slack import WebClient

from slack_work_out.models import User

try:
    import slack_information
    OAUTH_TOKEN = slack_information.OAUTH_TOKEN
except:
    OAUTH_TOKEN = os.environ.get('OAUTH_TOKEN')


def insert_user():
    client = WebClient(token=OAUTH_TOKEN)
    res = client.users_list()
    for member in res['members']:
        if member['id'] == 'USLACKBOT' or member['is_bot']:
            continue
        profile = member['profile']
        obj, created = User.objects.get_or_create(
            slack_id=member['id'],
            name=profile['display_name'],
            image_url=profile['image_72'],
            is_bot=member['is_bot']
        )
        print(obj)
        print(created)


if __name__ == "__main__":
    insert_user()

