# -*- coding: utf-8 -*-
import urllib2
import re
urlopen = urllib2.urlopen
request = urllib2.Request


def get_content_from_url(url):  # 从url中读取页面内容
    attempts = 0
    content = ''
    while attempts < 10:
        print 'get_content_from_url -- cur attempts : ', attempts
        try:
            content = urlopen(url, data=None, timeout=10).read()
            break
        except Exception, e:
            attempts += 1
            print e
    return content


def get_binary_from_req(req):  # 从请求中获取binary数据
    attempts = 0
    binary = ''
    while attempts < 10:
        print 'get_binary_from_req -- cur attempts : ', attempts
        try:
            binary = urlopen(req, data=None, timeout=5).read()
            break
        except Exception, e:
            attempts += 1
            print e
            raise
    return binary


def extract_img_urls(content):  # 从页面内容中抓出所有图片链接
    imgs = re.findall(
        'img src=[\"|\'](http[s]?://[\d]+.media.tumblr.com/[^\"]+/[^\"]+)[\"|\']', content, re.M | re.S)
    imgs = set(imgs)
    # 抓取photoset页面的链接
    photoset_urls = re.findall(
        '(http[s]*://[\S]+.tumblr.com/post/[\d]+/photoset_iframe/[\S]+)[\"|\']', content, re.M | re.S)
    for photoset in photoset_urls:
        # 获取photoset页面，从页面中抓取图片链接
        photoset_content = get_content_from_url(photoset)
        photos = re.findall(
            'href=[\"|\'](http[s]?://[\d]+.media.tumblr.com/[^\"]+)[\"|\']', photoset_content, re.M | re.S)
        for photo in photos:
            imgs.add(photo)
    return imgs


url = 'http://girlimg-legs.tumblr.com/page/2'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'}
req = request(url, headers=headers)
response = get_binary_from_req(req)
imgset = extract_img_urls(response)
for item in imgset:
    print(item)
