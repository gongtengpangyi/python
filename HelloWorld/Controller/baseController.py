from django.shortcuts import render
from django.http import HttpResponse
import json
from HelloWorld import view


# 所有controller的基类，描述所有通用操作
class BaseController:
    __context = {}   # 内置模板参数字典

    # 根据controller和action的值显示模板
    def display(self, request):
        return render(request, view.CONTROLLER + '/' + view.ACTION + '.html', self.__context)

    # 回复请求错误信息
    @staticmethod
    def error(msg):
        response = {'result': 'error', 'msg': msg}
        return HttpResponse(json.dumps(response))

    # 回复请求成功信息
    @staticmethod
    def success(msg):
        response = {'result': 'success', 'msg': msg}
        return HttpResponse(json.dumps(response))

    def assign(self, key, value):
        """
        为模板参数字典赋值
        :param key: 字典的键名
        :param value: 字典的值
        """
        self.__context[key] = value

    def set_left(self):
        self.assign('list', {'aaa', 'bbb', 'ccc'})

    @staticmethod
    def response(message):
        return HttpResponse(message)
