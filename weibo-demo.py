# -*- coding: utf-8 -*-
from weibo import APIClient
import webbrowser
APP_KEY = '3099336849'
APP_SECRET = 'ee3dfd7e62b095eae75b514209a74eb0'
CALLBACK_URL = 'https://araell.github.io/nothingness/'

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET,
                   redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
webbrowser.open(url)
