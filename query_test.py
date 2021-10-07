import os

# 開発
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
# from django import setup
# setup()

# デプロイ
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
from django import setup
setup()


from slack_work_out.models import User


def insert_user():
    for i in range(5):
        obj, created = User.objects.get_or_create(
            slack_id=f'test_user{i}_id',
            name=f'test_user{i}'
        )
        print(obj, created)


if __name__ == "__main__":
    insert_user()
