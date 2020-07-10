# coding=utf-8
class test_middleware(object):
    def __init__(self, old_wsgi_app):
        self.old_wsgi_app = old_wsgi_app

    def __call__(self, environ, start_response):
        # 。。。一些自定义操作
        ret = self.old_wsgi_app(environ, start_response)
        # 。。。一些自定义操作
        return ret
