from tornado.web import RequestHandler


# 定义视图处理类
class IndexHandler(RequestHandler):

    # get处理函数
    def get(self):
        name = '徐楠'
        # users = [
        #     '张小凡',
        #     '金瓶儿',
        #     '陆雪峰',
        #     '鬼王宗',
        # ]
        self.render('index.html', name=name)


class ParamGet1(RequestHandler):

    # 处理get参数
    def get(self):
        # 获取GET数据
        # 获取一个参数对应的数据
        name = self.get_query_argument('name')
        # 获取一个参数对应的多个参数
        # name = self.get_query_arguments('name')
        print('获取到的数据', name)
        self.render('index.html', name=name)


class ParamGet2(RequestHandler):

    # 处理get参数：表单
    def get(self):
        # http://localhost:8000?name=Tom
        # 从查询字符串中获取数据，get_query_argument()
        name = self.get_query_argument('name')
        # 获取cookie中的数据
        self.get_cookie('name')
        print('get表单方式提交的数据：{}'.format(name))
        self.render('index.html', name=name)


class ParamPost(RequestHandler):

    # 处理post参数：表单
    def post(self):
        # POST提交的数据，包含在请求体中，request body
        # 从post中提取数据：get_body_argument()
        name = self.get_body_argument('name')
        # 向cookie中存储数据
        self.set_cookie('name', name, expires_days=10)
        # 向cookie中存储数据
        self.set_secure_cookie('msg_sec', name, expires_days=10)
        print('post请求传递的参数', name)
        self.render('index.html', name=name)


class ParamRest(RequestHandler):

    # 处理RESTful参数
    def get(self, user_id):
        print('Restful传递的参数', user_id)
        self.render('index.html', name=user_id)


'''
GET方式获取客户端提交数据
    get_query_argument()
    get_query_arguments()
    
POST方式获取客户端提交数据
    get_body_argument()
    get_body_arguments()

Python 简洁优雅，通用的获取方式：可以获取GET/POST提交的数据
    get_argument()
    get_arguments()
    
RESTful方式传递参数
    视图中配置正则表达式接受参数数据
    视图处理函数中，定义函数的参数接受用户提交的数据
'''