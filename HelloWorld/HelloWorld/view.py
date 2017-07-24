from django.http import HttpResponse
import sys


# 后台程序入口，根据请求的url来映射对应的controller.action
def index(request):
    # TODO:request预处理（如全部设为utf-8啊，消除跨域访问啊之类的）
    path = request.path.split('/')
    CONTROLLER = 'test'     # 默认Controller
    ACTION = 'hello'        # 默认action
    # 避免对django的附加请求进行处理
    if len(path) > 1 and path[1] == 'favicon.ico':
        return HttpResponse(" ")
    # 为controller赋值
    if len(path) > 1 and path[1] != '':
        CONTROLLER = path[1]
    # 为action赋值
    if len(path) > 2:
        ACTION = path[2]
    global CONTROLLER, ACTION       # 将两个值设为全局变量
    __import__("Controller." + CONTROLLER + "Controller", fromlist=True)    # 导入模块
    a_mod = sys.modules["Controller." + CONTROLLER + "Controller"]      # 获得模块对象
    obj = getattr(a_mod, CONTROLLER.capitalize() + "Controller")        # 获得类
    obj = obj()        # 初始化类
    if hasattr(obj, ACTION):      # 判断对象方法是否存在
        func = getattr(obj, ACTION)        # 获得方法
        return func(request)       # 执行方法并返回值
    else:
        return HttpResponse("404! ")        # 返回404
