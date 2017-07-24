from .baseController import BaseController
from MyModel.jsonUtil import JsonUtil
from MyModel.models import TUser
import os
import re


# 测试控制器，反正就是测试用的
class TestController(BaseController):
    def hello(self, request):
        print(request.GET.get('name') or "shabi")
        self.assign('hello', 'welcome to testController!')
        # test1 = TUser(c_name='xxx', c_account='123', c_password='123', c_create_time='2017-03-04 01:01:01')
        # print(JsonUtil.json_encode_within(TUser.objects.all(), ""))
        self.set_left()
        return self.test_render('test.html', {'name': 'test', 'password': 'pass'})

    # def test_response(self, request):
    #     return self.error({'nadu': 'shabi', 'caowen': 'shabi'})

    def test_render(self, template, dict):
        path_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_object = open(path_dir + '/Templates/html/' + template)
        try:
            all_the_text = file_object.read()
        finally:
            file_object.close()
        # print(all_the_text)
        match_obj = re.findall(r'\{\{ [a-z|A-Z]* \}\}', all_the_text, re.M | re.I | re.S)
        if match_obj and len(match_obj) > 0:
            for temp in match_obj:
                key = temp[3: -3]
                value = ''
                if dict.get(key):
                    # print(key + ":" + dict.get(key))
                    value = dict.get(key)
                    # print(temp + "  replace to " + dict.get(key))
                all_the_text = all_the_text.replace(temp, value)
            # print(all_the_text)
        return TestController.response(all_the_text)



