import requests


urls = {
    'get': 'https://httpbin.org/get?title=learn+python+programming',
    'headers': 'https://httpbin.org/headers',
    'ip': 'https://httpbin.org/ip',
    'now': 'https://now.httpbin.org/',
    'user-agent': 'https://httpbin.org/user-agent',
    'UUID': 'https://httpbin.org/uuid',
}


def get_content(title, url):
    resp = requests.get(url)
    print(f'Response for {title}')
    print(resp.json())


for title, url in urls.items():
    get_content(title, url)
    print('-' * 40)
