# -*- coding: utf-8 -*-
# html parser
import sys
import threading
import urllib2
import re
import urlparse
from bs4 import BeautifulSoup

urlopen = urllib2.urlopen

# bb-love19
blogname = sys.argv[1]
if blogname == None:
    print('Invalid blogname!')
    sys.exit()

print(blogname)


def soup_analyze(blogname):
    # w+ 如果不存在文件，则创建新文件
    link_file = open(blogname + '.txt', 'w+')

    soup = BeautifulSoup(read_html_source(blogname), "lxml")
    for link in soup.find_all('a'):
        # link_href = link.get('href').encode('utf-8')
        if blogname in link_href:
            # print(link_href)
            link_file.write(link_href + '\n')
            link_file.write(get_page_content(link.get('href')))

    link_file.close()


def read_html_source(blogname):
    origin_file = open('html_source/' + blogname + '.html', 'r')
    html_content = origin_file.read()
    origin_file.close()
    return html_content


def get_page_content(url):
    attempts = 0
    page_content = ''
    while attempts < 10:
        print 'cur attempts : ', attempts
        try:
            page_content = urlopen(iriToUri(url), data=None, timeout=10).read()
            break
        except Exception, e:
            attempts += 1
            print e
    return page_content


def extract_video_url(page_content):
    pass


# convert non ascii url to uri
def urlEncodeNonAscii(b):
    return re.sub('[\x80-\xFF]', lambda c: '%%%02x' % ord(c.group(0)), b)


def iriToUri(iri):
    parts = urlparse.urlparse(iri)
    return urlparse.urlunparse(
        part.encode('idna') if parti == 1 else urlEncodeNonAscii(
            part.encode('utf-8'))
        for parti, part in enumerate(parts)
    )

soup_analyze(blogname)
