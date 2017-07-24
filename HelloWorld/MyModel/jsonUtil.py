import json
from django.forms.models import model_to_dict


# JSON工具类
class JsonUtil:
    # json化model数组
    @staticmethod
    def json_encode(models):
        return JsonUtil.json_encode_within(models, "")

    # 用选择器json化model数组, selector中是不需要加入的参数
    @staticmethod
    def json_encode_within(models, selector):
        dict_list = []
        keys = selector.split(' ')
        for model in models:
            dic = model_to_dict(model)
            for key in keys:
                try:
                    dic.pop(key)
                except KeyError:
                    pass
            dict_list.append(dic)
        return json.dumps(dict_list, cls=JSONEncoder)


# JSONEncode的处理
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        str_type = str(type(o)).replace('<class \'', '').replace('\'>', '').replace('.', '_')   # 获取类型
        if hasattr(self.EncodeHook, str_type):  # 如果存在函数
            func = getattr(self.EncodeHook, str_type)   # 获得函数
            return func(o)  # 返回特殊处理的值
        return super(JSONEncoder, self).default(o)  # 否则随便返回一个

    # Encode内部钩子
    class EncodeHook:
        # decimal的特殊处理
        @staticmethod
        def decimal_decimal(o):
            return str(o)

        # date特殊处理
        @staticmethod
        def datetime_date(o):
            return o.strftime("%Y-%m-%d")

        # datetime特殊处理
        @staticmethod
        def datetime_datetime(o):
            return o.strftime("%Y-%m-%d %H:%M:%S")


