import requests
from urllib.parse import urlencode

APP_ID = 6866070
AUTH_URL = 'https://oauth.vk.com/authorize'


aut_data = {
    'client_id': APP_ID,
    'scope': 'friends',
    'response_type': 'token',
    'v': '5.92'
}

print('?'.join((AUTH_URL, urlencode(aut_data))))


class UserVk:
    TOKEN = '4350fa614c729f7bff38b20a105e4855df4395252bf310e39be3859d3ce2bed20ba72e92c0b6ab6c40b84'
    vk_link = 'https://api.vk.com/method/'
    param = {'v': '5.92',
             'access_token': TOKEN}

    @staticmethod
    def get_response(request_link, method):
        return requests.get(f'{request_link}{method}', UserVk.param).json()

    def __init__(self, user_id):
        self.user_id = user_id
        self.link = f'https://vk.com/id{self.user_id}'

    def __and__(self, other):
        UserVk.param['source_uid'] = self.user_id
        UserVk.param['target_uid'] = other.user_id
        method = 'friends.getMutual'
        return list(map(UserVk, UserVk.get_response(UserVk.vk_link, method)['response']))

    def __repr__(self):
        return f'{self.user_id}'

    def __str__(self):
        return f'{self.user_link}'

    def get_user_link(self):
        return self.link

    user_link = property(get_user_link)


if __name__ == "__main__":
    user1 = UserVk(163383369)
    user2 = UserVk(76065479)
    print(user1 & user2)
    print(f'Количество общих друзей равно: {len(user1 & user2)} человек')
    for item in user2 & user1:
        print(item)
    print(user1)
    print(user2)
