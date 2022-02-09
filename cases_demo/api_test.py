import unittest
# 创建一个unittest测试用例管理框架
import configparser
import requests
from ddt import ddt, file_data
from api_key.key_demo import KeyDemo
@ddt
class UnitForTest(unittest.TestCase):
    # 公共部分提取，作为初始化内容
    @classmethod
    def setUpClass(cls) -> None:
        cls.token = None
        conf = configparser.ConfigParser()
        conf.read('../config/config.ini')
        cls.url = conf.get('DEFAULT', 'url')
        conf.read('../config/image.ini')
        cls.image = conf.get('DEFAULT', 'image')
        cls.kd = KeyDemo()

    def setUp(self) -> None:
        pass

    # 用户登录测试用例
    @file_data('../data/order/login/login.yaml')
    def test_login(self, **kwargs):
        # 实例化需要的内容
        url = self.url + kwargs['path']
        # 执行测试
        res = self.kd.post(url=url, headers=kwargs['headers'], data=kwargs['data'])
        print(res.text)
        # 断言校验
        value = self.kd.get_text(res.text, 'code')
        UnitForTest.token = self.kd.get_text(res.text, 'access_token')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 获取用户信息
    @file_data('../data/order/login/userinfo.yaml')
    def test_userinfo(self, **kwargs):
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token
        res = self.kd.get(url=url, headers=kwargs['headers'])
        print(res.text)
        value = self.kd.get_text(res.text, 'userName')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')

    #上传截图接口
    @file_data('../data/order/login/uploadFile.yaml')
    def test_uploadFile(self, **kwargs):
        url = kwargs['url'] + kwargs['path']
        files = {
            'file': ('timg.jpg', open('../config/timg.jpg', 'rb'), 'image/jpeg')
        }  # => 打开上传文件并且加入文件相关参数
        data = {
            "name": "timg"
        }
        # data传入请求参数dict,files传入待上传文件参数dict
        res = requests.post(url=url, data=data, files=files)
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')

    # 员工订单接口
    # 新增员工订单
    @file_data('../data/order/staffOrder/staffOrder.yaml')
    def test_staffOrder_add(self, **kwargs):
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token
        data = kwargs['data']
        data['imageList'][0] = self.image
        res = self.kd.post(url=url, headers=kwargs['headers'], data=data)
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')


if __name__ == '__main__':
    unittest.main()
