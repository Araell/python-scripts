from weibo import APIClient
APP_KEY = '3099336849'
APP_SECRET = 'ee3dfd7e62b095eae75b514209a74eb0'
CALLBACK_URL = 'https://araell.github.io/nothingness/'
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET,
                   redirect_uri=CALLBACK_URL)
access_token = '2.00h6gAlCBGVk4Dc1b6201f6f0zgVhI'
client.set_access_token(access_token, 3600)
print client.statuses.user_timeline.get()
