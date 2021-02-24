import requests

url = "http://jy001:8081/futureloan/mvc/api/member/login"

def test_login_001():
    print("登录成功的脚本1")
    cs = {
        "mobilephone": "15129938629",
        "pwd": 123456,
        "regname": "requests_test"
    }
    r = requests.get(url, params=cs)
    print(r.text)
    assert '10001' in r.text

def test_login_002():
    print("登录成功的脚本2")
    cs = {
        "mobilephone": "15129938666",
        "pwd": 123456123456123456,
        "regname": "requests_test"
    }
    r = requests.get(url, params=cs)
    print(r.text)
    assert '10001' in r.text

def test_login_003():
    print("手机号、密码不能为空")
    cs = {
        "mobilephone": "",
        "pwd": "",
        "regname": "requests_test"
    }
    r = requests.get(url, params=cs)
    print(r.text)
    assert '20103' in r.text

def test_login_004():
    print("手机号不能为空")
    cs = {
        "mobilephone": "",
        "pwd": 123456,
        "regname": "requests_test"
    }
    r = requests.get(url, params=cs)
    print(r.text)
    assert '20103' in r.text

def test_login_005():
    print("密码不能为空")
    cs = {
        "mobilephone": "15129938629",
        "pwd": "",
        "regname": "requests_test"
    }
    r = requests.get(url, params=cs)
    print(r.text)
    assert '20103' in r.text

def test_login_006():
    print("手机号格式不正确")
    cs = {
        "mobilephone": "12345678911",
        "pwd": 123456,
        "regname": "requests_test"
    }
    r = requests.get(url, params=cs)
    print(r.text)
    assert '20111' in r.text

def test_login_007():
    print("密码错误，长度不足6位")
    cs = {
        "mobilephone": "15129938629",
        "pwd": 12345,
        "regname": "requests_test"
    }
    r = requests.get(url, params=cs)
    print(r.text)
    assert '20111' in r.text
    assert '用户名或密码错误' in r.text

def test_login_008():
    print("密码错误，长度超过18位")
    cs = {
        "mobilephone": "15129938629",
        "pwd": 1234561234561234567,
        "regname": "requests_test"
    }
    r = requests.get(url, params=cs)
    print(r.text)
    assert '20111' in r.text
    assert '用户名或密码错误' in r.text