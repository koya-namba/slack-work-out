import os

from slack import WebClient


try:
    import slack_information
    OAUTH_TOKEN = slack_information.OAUTH_TOKEN
except:
    OAUTH_TOKEN = os.environ.get('OAUTH_TOKEN')


def collect_user():
    client = WebClient(token=OAUTH_TOKEN)
    res = client.users_list()
    for member in res['members']:
        print(member['id'])
        profile = member['profile']
        print(profile['display_name'])


if __name__ == "__main__":
    collect_user()

