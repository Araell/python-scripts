# -*- coding: utf-8 -*-
from weibo import APIClient
import codecs
APP_KEY = '3099336849'
APP_SECRET = 'ee3dfd7e62b095eae75b514209a74eb0'
CALLBACK_URL = 'https://araell.github.io/nothingness/'
# code = '6ecedd0bc47d568634ef5346b6a515d8'
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET,
                   redirect_uri=CALLBACK_URL)
r = client.request_access_token(code)
access_token = r.access_token  # 新浪返回的token，类似abc123xyz456
# token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
expires_in = r.expires_in
# TODO: 在此可保存access token
ac_file = open(access_token + '.txt', 'wb')
client.set_access_token(access_token, expires_in)
