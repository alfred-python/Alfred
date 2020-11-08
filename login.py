# Login and get back the request
import requests
from datetime import datetime
from re import findall
from json import dumps
from random import choice

# Return a new header with csrf token
def get_header(csrf):
    head_data = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.instagram.com/accounts/login/",
            "x-csrftoken": csrf,
            "host": 'instagram.com',
        }
    return head_data

# takes user, password and proxy; returns a message indicating success, fail or possible success
def login_check(user, pwd, proxy, TEST=False):
    proxy = {"http": proxy}
    login_url = 'https://www.instagram.com/accounts/login/ajax/'
    time = int(datetime.now().timestamp())
    data = {
    'username': user,
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pwd}',
    'queryParams': {},
    'optIntoOneTap': 'false'
    }

    with requests.Session() as shh:
        # Getting necessary cookies and posting data
        req = requests.get('https://www.instagram.com/accounts/login/', proxies=proxy)
        if req.status_code != 200:
            return "no" 
        cookie = req.cookies['csrftoken']
        csrf = findall(r"csrf_token\":\"(.*?)\"", req.text)[0]
        posted = shh.post(login_url, data=data, proxies=proxy, headers=get_header(csrf))

    # Check the return value
    resp = posted.text
    if TEST:
        return resp
    else:
        if '\"authenticated\": true' in resp:
            return "yes"
        elif "Please wait a few" in resp:
            return "wait"
        elif 'user: false' in resp:
            return "invalid_user"
        elif "checkpoint_required" in resp:
            return "maybe"
        else:
            return "no"