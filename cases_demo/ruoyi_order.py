import unittest
import requests
# 创建一个unittest测试用例管理框架
# https://tooltt.com/json2yaml/  json转yaml
import configparser
from ddt import ddt, file_data
from api_key.key_demo import KeyDemo
@ddt
#OA订单相关接口
class UnitForTest(unittest.TestCase):
    # 公共部分提取，作为初始化内容
    @classmethod
    def setUpClass(cls) -> None:
        cls.kd = KeyDemo()
        conf = configparser.ConfigParser()
        conf.read('../config/config.ini')
        cls.url = conf.get('DEFAULT', 'url')
        conf.read('../config/image.ini')
        cls.images = conf.get('DEFAULT', 'image')
        # 财务token
        cls.token = None
        # 销售token
        cls.token1 = None
        # 客服token
        cls.token2 = None
        # 仓库token
        cls.token3 = None
        # 员工订单任务id
        cls.taskid = None
        # 寄存订单id
        cls.orid = None
        # 普通订单id
        cls.id1 = None
        # 定金单id
        cls.id2 = None
        # 延迟单id
        cls.id3 = None
        # 待出库订单id
        cls.id4 = None
        # 待出库订单headid
        cls.headid = None

    def setUp(self) -> None:
        pass

    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # 登录财务唐春燕账号
    @file_data('../data/caiwu/login.yaml')
    def test_01(self, **kwargs):
        print("登录财务唐春燕账号")
        # 实例化需要的内容
        url = self.url + kwargs['path']
        # 执行测试
        res = self.kd.post(url=url, headers=kwargs['headers'], data=kwargs['data'])
        print(res.text)
        # 断言校验
        value = self.kd.get_text(res.text, 'code')
        if self.kd.get_text(res.text, 'access_token'):
            UnitForTest.token = self.kd.get_text(res.text, 'access_token')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 获取用户信息
    @file_data('../data/caiwu/userinfo.yaml')
    def test_02(self, **kwargs):
        print("获取用户信息")
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token
        res = self.kd.get(url=url, headers=kwargs['headers'])
        print(res.text)
        value = self.kd.get_text(res.text, 'userName')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # 登录销售经理陈淑珍账号
    @file_data('../data/xiaoshou/login1.yaml')
    def test_03(self, **kwargs):
        # 实例化需要的内容
        print("登录销售经理陈淑珍账号")
        url = self.url + kwargs['path']
        # 执行测试
        res = self.kd.post(url=url, headers=kwargs['headers'], data=kwargs['data'])
        print(res.text)
        # 断言校验
        value = self.kd.get_text(res.text, 'code')
        UnitForTest.token1 = self.kd.get_text(res.text, 'access_token')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 获取用户信息
    @file_data('../data/xiaoshou/userinfo1.yaml')
    def test_04(self, **kwargs):
        print("获取用户信息")
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token1
        res = self.kd.get(url=url, headers=kwargs['headers'])
        print(res.text)
        value = self.kd.get_text(res.text, 'userName')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # 登录客服葛喻账号
    @file_data('../data/kefu/login2.yaml')
    def test_05(self, **kwargs):
        print("登录客服葛喻账号")
        # 实例化需要的内容
        url = self.url + kwargs['path']
        # 执行测试
        res = self.kd.post(url=url, headers=kwargs['headers'], data=kwargs['data'])
        print(res.text)
        # 断言校验
        value = self.kd.get_text(res.text, 'code')
        UnitForTest.token2 = self.kd.get_text(res.text, 'access_token')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 获取用户信息
    @file_data('../data/kefu/userinfo2.yaml')
    def test_06(self, **kwargs):
        print("获取用户信息")
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token2
        res = self.kd.get(url=url, headers=kwargs['headers'])
        print(res.text)
        print(self.taskid)
        value = self.kd.get_text(res.text, 'userName')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # 登录仓库王美星账号
    @file_data('../data/cangku/login3.yaml')
    def test_07(self, **kwargs):
        print("登录仓库王美星账号")
        # 实例化需要的内容
        url = self.url + kwargs['path']
        # 执行测试
        res = self.kd.post(url=url, headers=kwargs['headers'], data=kwargs['data'])
        print(res.text)
        # 断言校验
        value = self.kd.get_text(res.text, 'code')
        UnitForTest.token3 = self.kd.get_text(res.text, 'access_token')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 获取用户信息
    @file_data('../data/cangku/userinfo3.yaml')
    def test_08(self, **kwargs):
        print("获取用户信息")
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token3
        res = self.kd.get(url=url, headers=kwargs['headers'])
        print(res.text)
        value = self.kd.get_text(res.text, 'userName')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # 员工订单任务
    # 新增员工订单任务
    @file_data('../data/caiwu/staffOrderTask.yaml')
    def test_09(self, **kwargs):
        print("新增员工订单任务")
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token
        res = self.kd.post(url=url, headers=kwargs['headers'], data=kwargs['data'])
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 补货任务详情信息
    @file_data('../data/caiwu/staffOrderTask1.yaml')
    def test_10(self, **kwargs):
        print("补货任务详情信息")
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token
        res = self.kd.get(url=url, headers=kwargs['headers'])
        print(res.text)
        value = self.kd.get_text(res.text, 'taskName')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 编辑员工订单信息
    @file_data('../data/caiwu/staffOrderTask2.yaml')
    def test_11(self, **kwargs):
        print("编辑员工订单信息")
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token
        res = self.kd.post(url=url, headers=kwargs['headers'], data=kwargs['data'])
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 查询员工订单任务列表
    @file_data('../data/caiwu/staffOrderTask3.yaml')
    def test_12(self, **kwargs):
        print("查询员工订单任务列表")
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token
        res = self.kd.get(url=url, headers=kwargs['headers'])
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        UnitForTest.taskid = self.kd.get_text(res.text, 'id')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # 上传截图接口
    @file_data('../data/order/uploadFile.yaml')
    def test_13(self, **kwargs):
        print("上传截图接口")
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
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # 员工订单接口
    # 新增员工订单
    @file_data('../data/caiwu/staffOrder.yaml')
    def test_14(self, **kwargs):
        print("新增员工订单")
        upfile = self.kd.uploadFile()
        # 上传支付截图
        print(upfile)
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token
        data = kwargs['data']
        data['imageList'][0] = upfile
        data['taskId'] = self.taskid[0]
        res = self.kd.post(url=url, headers=kwargs['headers'], data=data)
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 查询员工订单列表
    @file_data('../data/caiwu/staffOrder1.yaml')
    def test_15(self, **kwargs):
        print("查询员工订单列表")
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token
        res = self.kd.get(url=url, headers=kwargs['headers'])
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 查询员工订单详细信息
    @file_data('../data/caiwu/staffOrder2.yaml')
    def test_16(self, **kwargs):
        print("查询员工订单详细信息")
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token
        res = self.kd.get(url=url, headers=kwargs['headers'])
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # 新增普通订单
    @file_data('../data/xiaoshou/saveSaleOrder.yaml')
    def test_17(self, **kwargs):
        print("新增普通订单")
        upfile = self.kd.uploadFile()
        print(upfile)        # 上传支付截图
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token1
        data = kwargs['data']
        data['payImages'][0] = upfile
        # data['taskId'] = self.taskid[0]
        res = self.kd.post(url=url, headers=kwargs['headers'], data=data)
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 获取普通订单id
    @file_data('../data/xiaoshou/list1.yaml')
    def test_18(self, **kwargs):
        print("获取普通订单id")
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token1
        res = self.kd.get(url=url, headers=kwargs['headers'])
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        UnitForTest.id1 = self.kd.get_text(res.text, 'id')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 财务审核通过普通订单
    @file_data('../data/caiwu/finance.yaml')
    def test_19(self, **kwargs):
        print("财务审核通过普通订单")
        upfile = self.kd.uploadFile()
        print(upfile)  # 上传支付截图
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token
        data = kwargs['data']
        data['orderId'] = self.id1[0]
        data['viewRemark'] = '财务审核普通订单通过'
        res = self.kd.post(url=url, headers=kwargs['headers'], data=data)
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 经理审核通过普通订单
    @file_data('../data/xiaoshou/manager.yaml')
    def test_20(self, **kwargs):
        print("经理审核通过普通订单")
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token1
        data = kwargs['data']
        data['orderId'] = self.id1[0]
        res = self.kd.post(url=url, headers=kwargs['headers'], data=data)
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 待出库订单查询
    @file_data('../data/cangku/inoutlist.yaml')
    def test_21(self, **kwargs):
        print("待出库订单查询")
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token3
        res = self.kd.get(url=url, headers=kwargs['headers'])
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        UnitForTest.id4 = self.kd.get_text(res.text, 'id')
        UnitForTest.headid = self.kd.get_text(res.text, 'headId')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 普通订单发货
    @file_data('../data/cangku/passOutHead.yaml')
    def test_22(self, **kwargs):
        print("普通订单发货")
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token3
        data = kwargs['data']
        data['orderId'] = self.id1[0]
        data['id'] = self.id4[-1]
        data['headId'] = self.headid[-1]
        res = self.kd.post(url=url, headers=kwargs['headers'], data=data)
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')

    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # 新增寄存订单
    @file_data('../data/xiaoshou/saveSaleOrder1.yaml')
    def test_23(self, **kwargs):
        print("新增寄存订单")
        upfile = self.kd.uploadFile()
        print(upfile)        # 上传支付截图
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token1
        data = kwargs['data']
        data['payImages'][0] = upfile
        # data['taskId'] = self.taskid[0]
        res = self.kd.post(url=url, headers=kwargs['headers'], data=data)
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 查询待审核寄存订单
    @file_data('../data/kefu/orders.yaml')
    def test_24(self, **kwargs):
        print("查询待审核寄存订单")
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token2
        res = self.kd.get(url=url, headers=kwargs['headers'])
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        UnitForTest.orid = self.kd.get_text(res.text, 'id')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 客服审核通过寄存订单
    @file_data('../data/kefu/customer.yaml')
    def test_25(self, **kwargs):
        print("客服审核通过寄存订单")
        upfile = self.kd.uploadFile()
        print(upfile)  # 上传支付截图
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token2
        data = kwargs['data']
        data['pathList'][0] = upfile
        data['orderId'] = self.orid[0]
        res = self.kd.post(url=url, headers=kwargs['headers'], data=data)
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 财务审核通过寄存订单
    @file_data('../data/caiwu/finance.yaml')
    def test_26(self, **kwargs):
        print("财务审核通过寄存订单")
        upfile = self.kd.uploadFile()
        print(upfile)  # 上传支付截图
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token
        data = kwargs['data']
        data['orderId'] = self.orid[0]
        data['viewRemark'] = '财务审核寄存订单通过'
        res = self.kd.post(url=url, headers=kwargs['headers'], data=data)
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
        # 经理审核通过寄存订单
    # 经理审核通过寄存订单
    @file_data('../data/xiaoshou/manager.yaml')
    def test_27(self, **kwargs):
        print("经理审核通过寄存订单")
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token1
        data = kwargs['data']
        data['orderId'] = self.orid[0]
        res = self.kd.post(url=url, headers=kwargs['headers'], data=data)
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # 新增定金单
    @file_data('../data/xiaoshou/saveSaleOrder2.yaml')
    def test_28(self, **kwargs):
        print("新增定金单")
        upfile = self.kd.uploadFile()
        print(upfile)        # 上传支付截图
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token1
        data = kwargs['data']
        data['payImages'][0] = upfile
        # data['taskId'] = self.taskid[0]
        res = self.kd.post(url=url, headers=kwargs['headers'], data=data)
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 获取定金单id
    @file_data('../data/xiaoshou/list1.yaml')
    def test_29(self, **kwargs):
        print("获取定金单id")
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token1
        res = self.kd.get(url=url, headers=kwargs['headers'])
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        UnitForTest.id2 = self.kd.get_text(res.text, 'id')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 财务审核通过定金单
    @file_data('../data/caiwu/finance.yaml')
    def test_30(self, **kwargs):
        print("财务审核通过定金单")
        upfile = self.kd.uploadFile()
        print(upfile)  # 上传支付截图
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token
        data = kwargs['data']
        data['orderId'] = self.id2[0]
        data['viewRemark'] = '财务审核定金单单通过'
        res = self.kd.post(url=url, headers=kwargs['headers'], data=data)
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # 新增延迟单
    @file_data('../data/xiaoshou/saveSaleOrder3.yaml')
    def test_31(self, **kwargs):
        print("新增延迟单")
        upfile = self.kd.uploadFile()
        print(upfile)        # 上传支付截图
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token1
        data = kwargs['data']
        data['payImages'][0] = upfile
        # data['taskId'] = self.taskid[0]
        res = self.kd.post(url=url, headers=kwargs['headers'], data=data)
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 获取延迟单id
    @file_data('../data/xiaoshou/list1.yaml')
    def test_32(self, **kwargs):
        print("获取延迟单id")
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token1
        res = self.kd.get(url=url, headers=kwargs['headers'])
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        UnitForTest.id3 = self.kd.get_text(res.text, 'id')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 财务审核通过延迟单
    @file_data('../data/caiwu/finance.yaml')
    def test_33(self, **kwargs):
        print("财务审核通过延迟单")
        upfile = self.kd.uploadFile()
        print(upfile)  # 上传支付截图
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token
        data = kwargs['data']
        data['orderId'] = self.id3[0]
        data['viewRemark'] = '财务审核延迟单通过'
        res = self.kd.post(url=url, headers=kwargs['headers'], data=data)
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 经理审核通过延迟单
    @file_data('../data/xiaoshou/manager.yaml')
    def test_34(self, **kwargs):
        print("经理审核通过延迟单")
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token1
        data = kwargs['data']
        data['orderId'] = self.id3[0]
        res = self.kd.post(url=url, headers=kwargs['headers'], data=data)
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 待出库订单查询
    @file_data('../data/cangku/inoutlist.yaml')
    def test_35(self, **kwargs):
        print("待出库订单查询")
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token3
        res = self.kd.get(url=url, headers=kwargs['headers'])
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        UnitForTest.id4 = self.kd.get_text(res.text, 'id')
        UnitForTest.headid = self.kd.get_text(res.text, 'headId')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')
    # 延迟订单发货
    @file_data('../data/cangku/passOutHead.yaml')
    def test_36(self, **kwargs):
        print("延迟订单发货")
        url = self.url + kwargs['path']
        kwargs['headers']['Authorization'] = 'Bearer ' + self.token3
        data = kwargs['data']
        data['orderId'] = self.id3[0]
        data['id'] = self.id4[-1]
        data['headId'] = self.headid[-1]
        res = self.kd.post(url=url, headers=kwargs['headers'], data=data)
        print(res.text)
        value = self.kd.get_text(res.text, 'code')
        print('实际结果：', value, '  预期结果：', kwargs['text'])
        self.assertEqual(first=kwargs['text'], second=value, msg='失败')


class UnitForTest1(unittest.TestCase):
    def test_01(self):
        print("OA接口")

if __name__ == '__main__':
    unittest.main()
