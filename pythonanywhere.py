import requests


my_domain = 'TaviTum.pythonanywhere.com'
username = 'TaviTum'
token = '75496cb717c9a5974dc43f26c02a7fea694a77b8'

response = requests.post(
    'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain}/reload/'.format(
        username=username, domain=my_domain
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('All OK')
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))