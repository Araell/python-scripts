# file encoding
# -*- coding: utf-8 -*-

# to string
numstr = str(3773)

# decode
'test decode'.decode(encoding='UTF-8', errors='strict')

# open url in webbrowser
#import webbrowser
url = 'https://www.google.com'
webbrowser.open(url)

# write file
filename = 'sample'
sample = open(filename + '.txt', 'wb')

# thread
# open url using urllib2
import threading
import urllib2

urlopen = urllib2.urlopen


class demoThread(threading.Thread):
    data = None

    def __init__(self, data):
        threading.Thread.__init__(self)
        self.data = data

    def run(self):
        for url in self.data:
            page_content = urlopen(url, data=None, timeout=10).read()

# convert to set
data = set(data)
demo_t = demoThread(data)

# mock request from browser
request = urllib2.request
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'}
req = request(url, headers=headers)
