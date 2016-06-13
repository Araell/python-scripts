A simple python web server
-----

## WSGI
[官方文档中WSGI的定义](https://www.python.org/dev/peps/pep-3333/)

WSGI Server 在 python 2.7 的官方实现:  

/usr/local/Cellar/python/2.7.10_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/wsgiref/

## WSGI的实现和部署
要使用WSGI，需要分别实现server角色和application角色。

Application端的实现一般是由Python的各种框架来实现的，比如Django, web.py等，一般开发者不需要关心WSGI的实现，框架会提供接口让开发者获取HTTP请求的内容以及发送HTTP响应。

Server端的实现会比较复杂一点，这个主要是因为软件架构的原因。一般常用的Web服务器，如Apache和nginx，都不会内置WSGI的支持，而是通过扩展来完成。比如Apache服务器，会通过扩展模块mod_wsgi来支持WSGI。Apache和mod_wsgi之间通过程序内部接口传递信息，mod_wsgi会实现WSGI的server端、进程管理以及对application的调用。Nginx上一般是用proxy的方式，用nginx的协议将请求封装好，发送给应用服务器，比如uWSGI，应用服务器会实现 WSGI 的服务端、进程管理以及对 application 的调用。