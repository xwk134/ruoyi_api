import requests
import json
import jsonpath

class KeyDemo:
    #定义get请求方法
    def get(self, url, headers=None):
        return requests.get(url=url, headers=headers)
    #定义post请求方法
    def post(self, url, headers=None, data=None, files=None):
        if data is not None:
            data = self.json_dumps(data)
        return requests.post(url=url, headers=headers, data=data, files=files)
    #请求参数转换为json格式
    def json_dumps(self, data):
        return json.dumps(data)

    #获取返回值参数文本信息
    def get_text(self, res, key):
        if res is not None:
            try:
                text = json.loads(res)
                value = jsonpath.jsonpath(text, '$..{0}'.format(key))
                if value:
                    if len(value) == 1:
                        return value[0]
                return value
            except Exception as e:
                return e
        else:
            return None

    # 上传支付截图
    def uploadFile(self):
        url = "http://192.168.31.2:9300/uploadFile"
        files = {
            'file': ('timg.jpg', open('../config/timg.jpg', 'rb'), 'image/jpeg')
        }  # => 打开上传文件并且加入文件相关参数
        data = {
            "name": "timg"
        }
        # data传入请求参数dict,files传入待上传文件参数dict
        res = requests.post(url=url, data=data, files=files)
        value = self.get_text(res.text, 'data')
        return value

