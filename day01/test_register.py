'''
pytest命名约束：
    1.文件用test_开头
    2.类用Test开头
    3.函数或方法用test_开头
'''
import requests

url = "http://jy001:8081/futureloan/mvc/api/member/register"

def test_register_001():
    print("注册成功的脚本1")
    cs = {
        "mobilephone": "15129938629",
        "pwd": 123456,
        "regname": "requests_test"
    }
    r = requests.get(url, params=cs)
    print(r.text)
    assert '10001' in r.text

def test_register_002():
    print("注册成功的脚本2")
    cs = {
        "mobilephone": "15129938666",
        "pwd": 123456123456123456,
        "regname": "requests_test"
    }
    r = requests.get(url, params=cs)
    print(r.text)
    assert '10001' in r.text

def test_register_003():
    print("手机号、密码不能为空")
    cs = {
        "mobilephone": "",
        "pwd": "",
        "regname": "requests_test"
    }
    r = requests.get(url, params=cs)
    print(r.text)
    assert '20103' in r.text

def test_register_004():
    print("手机号码不能为空")
    cs = {
        "mobilephone": "",
        "pwd": 123456,
        "regname": "requests_test"
    }
    r = requests.get(url, params=cs)
    print(r.text)
    assert '20103' in r.text


def test_register_005():
    print("密码不能为空")
    cs = {
        "mobilephone": "12345678911",
        "pwd": "",
        "regname": "requests_test"
    }
    r = requests.get(url, params=cs)
    print(r.text)
    assert '20103' in r.text

def test_register_006():
    print("手机号码格式不正确")
    cs = {
        "mobilephone": "12345678911",
        "pwd": 123456,
        "regname": "requests_test"
    }
    r = requests.get(url, params=cs)
    print(r.text)
    assert '20109' in r.text

def test_register_007():
    print("手机号码已被注册")
    cs = {
        "mobilephone": "15129938653",
        "pwd": 123456,
        "regname": "requests_test"
    }
    r = requests.get(url, params=cs)
    print(r.text)
    assert '20110' in r.text

def test_register_008():
    print("密码长度不足6位")
    cs = {
        "mobilephone": "15129938653",
        "pwd": 12345,
        "regname": "requests_test"
    }
    r = requests.get(url, params=cs)
    print(r.text)
    assert '20108' in r.text

def test_register_009():
    print("密码长度超过18位")
    cs = {
        "mobilephone": "15129938653",
        "pwd": 1234567891111111111,
        "regname": "requests_test"
    }
    r = requests.get(url, params=cs)
    print(r.text)
    assert '20108' in r.text


