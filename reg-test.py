# -*- coding: utf-8 -*-
import re
source_file = 'echo.html'
source = open(source_file, 'r')

# source":"http:\/\/7u2r6o.com2.z0.glb.qiniucdn.com\/m1\/3ea777703d1fad7ab7fc8676bffa844fc2ad65d45c0dbb7be582dac7353558c9dd90df91.m3u8?1449126508
result = re.findall(
    'http:[\S]+.ts', source.read(), re.M | re.S)

print(result)
