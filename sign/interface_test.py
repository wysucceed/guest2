import requests
import unittest


class GetEventListTest(unittest.TestCase):
    '''查询发布会接口测试'''


    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/get_event_list/"

    def test_get_event_null(self):
        '''发布会id为空'''
        r = requests.get(self.url,params={'eid':''})
        result = r.json()
        self.assertEqual(result['status'],10021)
        self.assertEqual(result['message'],"parameter error")
    def test_get_event_error(self):
        '''发布会id不存在'''
        r = requests.get(self.url,params={'eid':'901'})
        result = r.json()
        self.assertEqual(result['status'],10022)
        self.assertEqual(result['message'],"query result is empty")

    def test_get_event_success(self):
        #发布会id为1，查询成功

        r = requests.get(self.url,params={'eid':'1'})
        result = r.json()

        #断言接口返回值
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'],"success")
        self.assertIn("发布会",result['data']['name'])
        self.assertEqual(result['data']['address'],"北京国家会议中心")
        self.assertEqual(result['data']['start_time'],"2018-06-01T18:00:00")
if __name__ =='__main__':

    unittest.main() #这行代码作用同以下代码，加载和运行

    '''
    #构造测试集
   
    suite = unittest.TestSuite()
    suite.addTest(GetEventListTest("test_get_event_null"))
    suite.addTest(GetEventListTest("test_get_event_error"))
    suite.addTest(GetEventListTest("test_get_event_success"))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
    '''