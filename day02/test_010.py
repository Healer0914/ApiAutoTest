import pytest
import requests

cs = [
    # 手机号、密码均为空
    {"data": {"mobilephone": "", "pwd": ''},
     "except": {"status": 0, "code": '20103', "msg": "手机号不能为空"}},
    # 手机号码格式不正确
    {"data": {"mobilephone": "12345678911", "pwd": '123456'},
     "except": {"status": 0, "code": '20109', "msg": "手机号码格式不正确"}},
    # 手机号码已被注册
    {"data": {"mobilephone": "15129938653", "pwd": '123456'},
     "except": {"status": 0, "code": '20110', "msg": "手机号码已被注册"}}
]


@pytest.fixture(params=cs)
def register_data(request):
    return request.param

def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r =requests.post(url,data=data)
    return r

# 数据驱动的测试模型，
# test_register 测试脚本/测试逻辑，测试数据与测试逻辑分离，相同逻辑的数据放到一起，实现一个脚本即可
# 数据可以放到csv、xml、yaml……去维护

def test_register(register_data):
    print(f"预测数据：{register_data['data']}")
    print(f"预期结果：{register_data['except']}")
    r = register(register_data['data'])
    print(f"实际结果：{r.text}")
    assert r.json()['status'] == register_data['except']['status']
    assert r.json()['code'] == register_data['except']['code']
    assert r.json()['msg'] == register_data['except']['msg']
