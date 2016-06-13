# coding: utf-8
import web

render = web.template.render('templates/')
urls = (
    '/countdown', 'index',
    # '/readme', 'readme'
)
# '/(.*)', 'index'


class index:

    def GET(self):
        # 从url参数中按名称获取参数值 i.e. http://0.0.0.0:8080/?name=joe&rank=33
        i = web.input(name=None, rank=None)
        return render.index(i.name, i.rank)

    # 直接从url参数中获得参数
    # def GET(self, name):
    #     return render.index(name)


class readme:

    def GET(self):
        return render.readme("nonsense")

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
