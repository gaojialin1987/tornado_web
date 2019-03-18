# 基础包
import os

# 第三方包
from tornado.ioloop import IOLoop
from tornado.options import options, define, parse_command_line
from tornado.web import Application

# 自定义包
import hellotemp

# 定义启动端口
define('port', default=8000, help='项目启动默认端口')

# 部署启动服务
if __name__ == '__main__':
    # 添加命令行识别变量的操作
    parse_command_line()
    # 基础路由
    BASE_URL = os.path.dirname(__file__)
    # 构建web app
    app = Application(
        [
            # 配置路由
            (r'/', hellotemp.IndexHandler),
            # GET传递参数
            (r'/param_get1/', hellotemp.ParamGet1),
            (r'/param_get2/', hellotemp.ParamGet2),
            # POST传递参数
            (r'/param_post/', hellotemp.ParamPost),
            # RESTful传递参数
            (r'/param_rest/(?P<user_id>\d+)/', hellotemp.ParamRest)
        ],
        # 配置网页模板
        template_path=os.path.join(BASE_URL, 'templates'),
        # 配置静态文件
        static_path=os.path.join(BASE_URL, 'static'),
        # 开启调试模式(可以看到更多的报错信息)
        debug=True,
        # 混淆码
        cookie_secret='lianshang5188'
    )
    # 监听默认端口并启动服务器
    app.listen(options.port)
    # 启动IOLoop事件轮询监听
    IOLoop.current().start()
