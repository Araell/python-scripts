# -*- coding: utf-8 -*-
# test utf-8
import re
import urlparse
import threading
import urllib2
urlopen = urllib2.urlopen


def urlEncodeNonAscii(b):
    return re.sub('[\x80-\xFF]', lambda c: '%%%02x' % ord(c.group(0)), b)


def iriToUri(iri):
    parts = urlparse.urlparse(iri)
    return urlparse.urlunparse(
        part.encode('idna') if parti == 1 else urlEncodeNonAscii(
            part.encode('utf-8'))
        for parti, part in enumerate(parts)
    )

url = u'http://bb-love19.tumblr.com/post/138858312081/1월4일-비비커플-맞는걸-좋아하는-비비-정리끝났는데-6개-정도-남았네요'
# url = urllib2.unquote(url)
# url = 'http://www.baidu.com'

uri = iriToUri(url)
print(uri)

page_content = urlopen(uri, data=None, timeout=10).read()

# print(page_content)

# ^ 非
links = re.findall(
    '(https://www.tumblr.com/video/[^\']*)', page_content, re.M | re.S)
print(links)
